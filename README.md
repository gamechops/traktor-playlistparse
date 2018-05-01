# traktor-playlistparse
A simple utility to take Traktor Playlist HTML documents and convert them into Cue Sheets and text documents. 

This utility was used by Dj CUTMAN to generate time links for YouTube and Cue Sheets for MP3s on Patreon for his recorded sets for This Week In Chiptune.  

This is a command line utility written in Python, and as such, assumes you know how to navigate a shell in your respective OS. 

## Requirements
Python 2
BeautifulSoup 4

## Installation
* Ensure python2 is installed
* Install dependencies
  * On Linux/macOS/Unix: `pip install -r requirements.txt`
  * On Windows: `python -m pip install -r requirements.txt`
  
## Instructions
* Export a playlist to an HTML document.
* Run the script

## Output
Script will output two flies:
* `playlist.txt` - A text file with timestamps, track name and artist, designed for use with YouTube
* `playlist.cue` - A Cue sheet designed to be bundled with an MP3. 
