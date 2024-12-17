import yt_dlp
import os

# Prompt user to input folder name
download_folder = input("Enter folder name to save the videos: ").strip()

# Create the folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Folder '{download_folder}' created successfully!")
else:
    print(f"Folder '{download_folder}' already exists.")

while True:
    # Get video URL from user input
    video_url = input("Enter video URL (or type 'exit'  or q to quit ): ")
    
    # Exit the loop if the user types 'exit'
    if video_url.lower() == 'exit' or video_url.lower() =="q":
        print("Exiting the downloader. Goodbye!")
        break

    # Specify options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select 720p video and best audio
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save to user-defined folder
    }

    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Download complete! Video saved to '{download_folder}' folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("All tasks completed.")
