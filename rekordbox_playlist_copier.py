#!/usr/bin/env python3
"""
Rekordbox Playlist Copier
Extracts tracks from a Rekordbox playlist and copies them to a folder.
"""

import os
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET


def decode_rekordbox_path(location):
    """
    Decode Rekordbox file location to actual file path.
    Rekordbox stores paths as file:// URLs that need to be decoded.
    """
    # Remove 'file://localhost' or 'file://' prefix
    if location.startswith('file://localhost'):
        path = location[16:]
    elif location.startswith('file://'):
        path = location[7:]
    else:
        path = location
    
    # URL decode the path
    path = unquote(path)
    
    return path


def get_playlists(xml_file):
    """Parse XML and return all playlist names."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    playlists = {}
    playlists_node = root.find('.//PLAYLISTS')
    
    if playlists_node is None:
        print("No playlists found in XML file")
        return playlists
    
    def parse_playlist_node(node, prefix=""):
        """Recursively parse playlist nodes."""
        for child in node:
            if child.tag == 'NODE':
                node_type = child.get('Type')
                name = child.get('Name')
                
                if node_type == '0':  # Folder
                    # Recursively parse folder contents
                    parse_playlist_node(child, prefix=f"{prefix}{name}/")
                elif node_type == '1':  # Playlist
                    full_name = f"{prefix}{name}"
                    playlists[full_name] = child
    
    parse_playlist_node(playlists_node)
    return playlists


def get_tracks_from_playlist(xml_file, playlist_name):
    """Extract all track file paths from a specific playlist."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # First, build a dictionary of all tracks by their TrackID
    tracks = {}
    collection = root.find('COLLECTION')
    if collection is not None:
        for track in collection.findall('TRACK'):
            track_id = track.get('TrackID')
            location = track.get('Location')
            name = track.get('Name', 'Unknown')
            artist = track.get('Artist', 'Unknown')
            if location:
                tracks[track_id] = {
                    'location': decode_rekordbox_path(location),
                    'name': name,
                    'artist': artist
                }
    
    # Get all playlists
    playlists = get_playlists(xml_file)
    
    if playlist_name not in playlists:
        print(f"\nPlaylist '{playlist_name}' not found!")
        print("\nAvailable playlists:")
        for name in sorted(playlists.keys()):
            print(f"  - {name}")
        return []
    
    # Get tracks from the selected playlist
    playlist_node = playlists[playlist_name]
    track_list = []
    
    for track_node in playlist_node.findall('TRACK'):
        key = track_node.get('Key')
        if key in tracks:
            track_list.append(tracks[key])
    
    return track_list


def copy_playlist_tracks(xml_file, playlist_name, output_folder):
    """Copy all tracks from a playlist to the output folder."""
    
    # Get tracks from playlist
    print(f"\nSearching for playlist: {playlist_name}")
    tracks = get_tracks_from_playlist(xml_file, playlist_name)
    
    if not tracks:
        print("No tracks found in playlist")
        return
    
    print(f"\nFound {len(tracks)} tracks in playlist")
    
    # Create output folder
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Copy tracks
    successful = 0
    failed = 0
    
    for i, track in enumerate(tracks, 1):
        source_path = Path(track['location'])
        
        if not source_path.exists():
            print(f"  ✗ Track {i}: File not found - {source_path}")
            failed += 1
            continue
        
        # Create numbered filename to preserve order
        file_extension = source_path.suffix
        # Sanitize filename
        safe_name = f"{track['artist']} - {track['name']}"
        safe_name = "".join(c for c in safe_name if c.isalnum() or c in (' ', '-', '_', '.')).strip()
        dest_filename = f"{i:03d} - {safe_name}{file_extension}"
        dest_path = output_path / dest_filename
        
        try:
            shutil.copy2(source_path, dest_path)
            print(f"  ✓ Track {i}: {track['artist']} - {track['name']}")
            successful += 1
        except Exception as e:
            print(f"  ✗ Track {i}: Failed to copy - {e}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Successfully copied: {successful} tracks")
    print(f"  Failed: {failed} tracks")
    print(f"  Output folder: {output_path.absolute()}")
    print(f"{'='*60}\n")


def main():
    print("\n" + "="*60)
    print("Rekordbox Playlist Copier")
    print("="*60 + "\n")
    
    # Get XML file
    if len(sys.argv) > 1:
        xml_file = sys.argv[1]
    else:
        xml_file = input("Enter path to Rekordbox XML file: ").strip()
    
    if not os.path.exists(xml_file):
        print(f"Error: File not found - {xml_file}")
        return
    
    # Show available playlists
    print("\nScanning XML file...")
    playlists = get_playlists(xml_file)
    
    if not playlists:
        print("No playlists found in XML file")
        return
    
    print(f"\nFound {len(playlists)} playlist(s):\n")
    playlist_list = sorted(playlists.keys())
    for i, name in enumerate(playlist_list, 1):
        print(f"  {i}. {name}")
    
    # Get playlist selection
    print("\n" + "-"*60)
    if len(sys.argv) > 2:
        playlist_name = sys.argv[2]
    else:
        selection = input("\nEnter playlist number or name: ").strip()
        
        # Check if it's a number
        try:
            idx = int(selection) - 1
            if 0 <= idx < len(playlist_list):
                playlist_name = playlist_list[idx]
            else:
                print("Invalid selection")
                return
        except ValueError:
            # It's a name
            playlist_name = selection
    
    # Get output folder
    if len(sys.argv) > 3:
        output_folder = sys.argv[3]
    else:
        default_output = os.path.join(os.path.expanduser("~"), "Desktop", f"Rekordbox - {playlist_name}")
        output_folder = input(f"\nEnter output folder (press Enter for Desktop): ").strip()
        if not output_folder:
            output_folder = default_output
    
    # Copy tracks
    copy_playlist_tracks(xml_file, playlist_name, output_folder)


if __name__ == "__main__":
    main()
