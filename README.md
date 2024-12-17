# YouTubeDownloads

A simple script for downloading videos from YouTube using **yt-dlp**. This tool allows you to:

- Download single video URLs.
- Batch download videos from a text file.
- Save videos with the original video title.
- Specify a custom folder to save the videos.

## Features

1. **Save Videos with Titles**:
   - Videos are automatically named using their YouTube titles.
2. **Custom Download Folder**:
   - You can specify a folder where the videos will be saved.
3. **Single or Batch Download**:
   - Input a single URL manually or provide a `link.txt` file with multiple URLs.
4. **Quality**:
   - Downloads are limited to 720p for video and best available audio, merged into MP4 format.

---

## Installation

Follow these steps to install and run the script:

### 1. Clone the Repository
```bash
git clone https://github.com/vanny1232/YoutubeDowloads.git
cd YoutubeDowloads
```

### 2. Install Required Dependencies
Make sure you have **Python 3.8+** installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python YoutubeDowloads.py
```

---

## Usage

### Option 1: Download a Single Video
1. Run the script.
2. Select the **'link'** option.
3. Paste the video URL.
4. The video will be saved in the folder you specify.

### Option 2: Batch Download from a File
1. Create a text file (e.g., `links.txt`) and add video URLs, one per line.
2. Run the script.
3. Select the **'file'** option.
4. Provide the name of the text file containing the video links.

---

## Example Execution

### **Input**
**links.txt**:
```text
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=3JZ_D3ELwOQ
```

### **Commands**
```bash
python YoutubeDowloads.py
```

### **Output**
```
Enter folder name to save the videos: MyVideos
Folder 'MyVideos' created successfully!

Enter 'link' to input a video URL manually or 'file' to load from a text file: file
Enter the name of the file containing video links (e.g., links.txt): links.txt

Found 2 video URLs in 'links.txt'. Starting downloads...

Downloading video 1 of 2: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[download] Destination: MyVideos/RickRoll.mp4
Download complete! Video saved as 'RickRoll.mp4'.

Downloading video 2 of 2: https://www.youtube.com/watch?v=3JZ_D3ELwOQ
[download] Destination: MyVideos/CoolVideo.mp4
Download complete! Video saved as 'CoolVideo.mp4'.

All tasks completed.
```

### Folder Structure
After downloads are completed, the folder will look like this:
```
YoutubeDowloads/
│
├── links.txt
├── YoutubeDowloads.py
├── requirements.txt
└── MyVideos/
    ├── RickRoll.mp4
    ├── CoolVideo.mp4
```

---

## Dependencies
- **yt-dlp**: A fork of youtube-dl for downloading videos.
- **os**: For folder and file management.

To install dependencies manually:
```bash
pip install yt-dlp
```

---

## Notes
- Make sure you have a stable internet connection for downloading videos.
- Videos are downloaded at 720p (if available) and saved as MP4.

---

## License
This project is licensed under the MIT License.

---

## Author
- **Vanny** - [GitHub Profile](https://github.com/vanny1232)

---

Enjoy downloading your favorite videos easily! 😊
