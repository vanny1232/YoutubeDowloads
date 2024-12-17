import yt_dlp
import os

# Prompt user to input folder name
try:
    download_folder = input("Enter folder name to save the videos: ").strip()

    # Create the folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Folder '{download_folder}' created successfully!")
    else:
        print(f"Folder '{download_folder}' already exists.")

    def download_video(video_urls, folder):
        """
        Downloads videos using yt-dlp given a list of URLs and a folder.
        Automatically uses the title of the video as the file name.
        """
        for index, url in enumerate(video_urls, start=1):
            print(f"\nDownloading video {index} of {len(video_urls)}: {url}")
            
            # yt-dlp options with title as the file name
            ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select 720p video and best audio
                'merge_output_format': 'mp4',  # Merge video and audio into MP4
                'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),  # Use video title as file name
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(f"Download complete! Video saved as '{url.split('=')[-1]}.mp4' in '{folder}'.")
            except Exception as e:
                print(f"An error occurred with URL '{url}': {e}")

    # Ask user for input type: link or file
    choice = input("\nEnter 'link' or 'l' to input a video URL manually or 'file' or 'f' to load from a text file: ").strip().lower()

    if choice == "link" or choice == "l":
        # Download a single video URL manually
        video_url = input("Enter video URL: ").strip()
        download_video([video_url], download_folder)

    elif choice == "file" or choice == "f":
        FileLinkName = input("Enter the name of the file containing video links (e.g., links.txt): ").strip()
        # Check if the specified file exists
        if os.path.exists(FileLinkName):
            with open(FileLinkName, "r") as file:
                urls = [line.strip() for line in file if line.strip()]  # Read all non-empty lines
            if urls:
                print(f"\nFound {len(urls)} video URLs in '{FileLinkName}'. Starting downloads...")
                download_video(urls, download_folder)
            else:
                print(f"The file '{FileLinkName}' is empty. Please add video links and try again.")
        else:
            print(f"The file '{FileLinkName}' does not exist. Please check the file name and try again.")
    else:
        print("Invalid choice. Please restart the script and enter 'link' or 'file'.")

    print("\nAll tasks completed.")
except KeyboardInterrupt:
    print("\n\nProgram interrupted. Exiting the downloader.")