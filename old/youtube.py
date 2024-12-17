#import yt_dlp
#video_url = input("Enter video URL : ")

#ydl_opts = {}

#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 ##   ydl.download([video_url])

#print("Download complete")
#import yt_dlp

# Get video URL from user input
#video_url = input("Enter video URL: ")

# Specify options for yt-dlp
#ydl_opts = {
 #   'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select 720p video and best audio
 #   'merge_output_format': 'mp4',  # Merge video and audio into MP4
 #   'outtmpl': '%(title)s.%(ext)s',  # Set output file naming pattern
#}

# Download the video
#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 #   ydl.download([video_url])

#print("Download complete")
import yt_dlp

while True:
    # Get video URL from user input
    video_url = input("Enter video URL (or type 'exit' to quit): ")
    
    # Exit the loop if the user types 'exit'
    if video_url.lower() == 'exit':
        print("Exiting the downloader. Goodbye!")
        break

    # Specify options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select 720p video and best audio
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'outtmpl': '%(title)s.%(ext)s',  # Set output file naming pattern
    }

    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

print("All tasks completed.")
