from pytube import YouTube

def Download(link):
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"Downloaded: {percentage:.2f}%")

    youtubeObject = YouTube(link)
    youtubeObject.register_on_progress_callback(on_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        video_title = youtubeObject.title
        print(f"Downloading video: {video_title}")
        youtubeObject.download(filename='temp')
        print("Download completed successfully")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

link = input("Enter the YouTube video URL: ")
Download(link)
