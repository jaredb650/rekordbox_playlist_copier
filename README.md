# Rekordbox Playlist Copier

**Easily copy all tracks from a Rekordbox playlist into a folder - no clicking 80+ times!**

This script automatically extracts all tracks from any Rekordbox playlist and copies them to a folder on your computer, with files numbered in the correct playlist order.

---

## What You'll Need

- A Mac or Windows computer
- Rekordbox installed
- Python 3 (comes pre-installed on Mac, Windows users may need to install it)

---

## Step-by-Step Instructions

### Step 1: Export Your Rekordbox Collection to XML

1. Open **Rekordbox**
2. Go to **File → Export Collection in XML format**
3. Save the file somewhere easy to find (like your Desktop or Documents folder)
   - **Important:** If the filename has spaces, consider renaming it to remove spaces (e.g., `rekordbox_library.xml`)

### Step 2: Download the Script

Download the `rekordbox_playlist_copier.py` file and save it somewhere easy to find (like your Downloads folder or Desktop).

---

## For Mac Users

### Step 3: Open Terminal

1. Press **Cmd + Space** to open Spotlight
2. Type `Terminal` and press Enter
3. A black or white window will open - this is Terminal

### Step 4: Navigate to Where You Saved the Script

Type this command and press Enter (adjust the path if you saved it somewhere else):

```bash
cd ~/Downloads
```

Or if you saved it to your Desktop:

```bash
cd ~/Desktop
```

### Step 5: Make the Script Executable

Copy and paste this command, then press Enter:

```bash
chmod +x rekordbox_playlist_copier.py
```

This is a one-time step that allows the script to run.

### Step 6: Run the Script

Type this command and press Enter:

```bash
python3 rekordbox_playlist_copier.py
```

---

## For Windows Users

### Step 3: Open Command Prompt

1. Press **Windows Key + R**
2. Type `cmd` and press Enter
3. A black window will open - this is Command Prompt

### Step 4: Navigate to Where You Saved the Script

Type this command and press Enter (adjust the path if needed):

```bash
cd Downloads
```

Or if you saved it to your Desktop:

```bash
cd Desktop
```

### Step 5: Run the Script

Type this command and press Enter:

```bash
python rekordbox_playlist_copier.py
```

**Note:** If this doesn't work, you may need to install Python first. Download it from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation.

---

## Using the Script

Once the script is running, you'll see:

### 1. Enter Path to Rekordbox XML File

The script will ask: `Enter path to Rekordbox XML file:`

**Easy method (recommended):**
- Simply **drag and drop** your XML file from Finder (Mac) or File Explorer (Windows) into the Terminal/Command Prompt window
- The path will automatically appear
- Press **Enter**

**Manual method:**
- Type the full path to your XML file
- If the filename or path has spaces, put quotes around it:
  ```
  "/Users/yourname/Documents/rekordbox library.xml"
  ```

### 2. Choose Your Playlist

The script will show you all available playlists, numbered like this:

```
1. Crate 1
2. House Music
3. ROOT/Summer 2024
4. ROOT/Favorites/Deep House
```

**IMPORTANT:** Some playlists are inside folders and show as `ROOT/Folder Name/Playlist Name`

When selecting a playlist:

**Option A - Enter the number:**
- Just type the number (e.g., `3`) and press Enter

**Option B - Type the full name:**
- You **must** type the COMPLETE name exactly as shown, including `ROOT/` and any folder names
- ✅ Correct: `ROOT/Summer 2024`
- ❌ Wrong: `Summer 2024` (this won't work!)

### 3. Choose Output Folder (Optional)

The script will ask where to save the files.

**Easy option:**
- Just press **Enter** to save to your Desktop
- The folder will be automatically named after your playlist

**Custom option:**
- Type the full path where you want to save the files
- Example: `/Users/yourname/Music/MyPlaylist`

### 4. Done!

The script will:
- Copy all tracks from your playlist
- Number them in the correct order (001, 002, 003, etc.)
- Name them like: `001 - Artist - Track Name.mp3`
- Show you progress as it copies

When finished, you'll see a summary showing how many tracks were copied successfully.

---

## Troubleshooting

### "File not found" error when entering XML path
- Make sure the XML file actually exists where you think it is
- Try dragging and dropping the file instead of typing the path
- If the filename has spaces, make sure you put quotes around the entire path

### "Playlist not found" error
- Make sure you're typing the FULL playlist name exactly as shown
- Include `ROOT/` and any folder names if they appear in the list
- The name is case-sensitive, so `House Music` is different from `house music`

### "python3: command not found" (Mac)
- Try using `python` instead of `python3`

### "python: command not found" (Windows)
- You need to install Python from [python.org](https://www.python.org/downloads/)
- During installation, check the box that says "Add Python to PATH"

### Script runs but no tracks are copied
- Make sure the tracks still exist on your computer at their original location
- The script can only copy files that Rekordbox knows about and can find

---

## Example Session

Here's what a complete run looks like:

```
Rekordbox Playlist Copier
============================================================

Enter path to Rekordbox XML file: /Users/john/Desktop/rekordbox.xml

Scanning XML file...

Found 15 playlist(s):

  1. House Classics
  2. Techno Bangers
  3. ROOT/Summer Mix 2024
  4. ROOT/Favorites/Deep Cuts

------------------------------------------------------------

Enter playlist number or name: 3

Enter output folder (press Enter for Desktop): 

Searching for playlist: ROOT/Summer Mix 2024

Found 80 tracks in playlist

  ✓ Track 1: Artist Name - Song Title
  ✓ Track 2: Another Artist - Another Song
  ...
  ✓ Track 80: Final Artist - Final Song

============================================================
Summary:
  Successfully copied: 80 tracks
  Failed: 0 tracks
  Output folder: /Users/john/Desktop/Rekordbox - ROOT/Summer Mix 2024
============================================================
```

---

## Tips

- **Preserve playlist order:** The script automatically numbers files (001, 002, etc.) so the playlist order is maintained
- **Share with friends:** You can now zip up the output folder and share it easily
- **Multiple playlists:** Just run the script again to copy another playlist
- **File names:** If track names are too long or have weird characters, they'll be cleaned up automatically
