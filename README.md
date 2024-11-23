# findBPM 🎵

> A Python script that fetches and sorts BPM (Beats Per Minute) for your Spotify tracks in ascending order.

## Prerequisites
- Python 3.6+
- Active Spotify account
- Internet connection

## Quick Start Guide

### 1. Create Your Track List
1. Create a new playlist on Spotify with your desired tracks
2. Visit [Exportify](https://exportify.net/#playlists)
3. Export your playlist
4. Copy the track name column
5. Paste into Notepad
6. Save as `mixer.txt`

### 2. Set Up Spotify API
1. Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create an App"
4. Accept the terms of service
5. From settings menu, copy:
   - Client ID
   - Client Secret

### 3. Install & Run
1. Install required package:
```bash
pip install spotipy
```

2. Update credentials in the script:
```python
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
```

3. Run in your Python IDE:
```bash
python findBPM.py
```

## Output Example
```
Tracks sorted by BPM (ascending):

No.  Track Name                  Artist(s)               BPM     
-----------------------------------------------------------
1    Love Me                    Artist1                 85
2    Fear Of Heights            Artist3                 120       
3    Done To Me                 Amés                    122     
  

Summary:
Lowest BPM: 85 (Love Me)
Highest BPM: 120 (Fear Of Heights)
Average BPM: 100.0
```

## Features
- ✨ Reads from exported Spotify playlists
- 📊 Sorts tracks by BPM
- 📈 Provides summary statistics
- 🔄 Error handling included

## Troubleshooting
- **Authentication Error**: Verify your Client ID and Secret
- **Tracks Not Found**: Check for typos in mixer.txt
- **Script Crashes**: Ensure you have Python 3.6+ and spotipy installed

## Contributing
Feel free to fork, improve, and submit pull requests!

---
Made with ❤️ for music lovers
