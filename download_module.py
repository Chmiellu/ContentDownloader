import os
from pytube import YouTube

def download_video(url_entry, download_location_entry, resolution, status_label):
    url = url_entry.get()
    download_location = download_location_entry.get()
    choice = resolution.get()

    try:
        yt = YouTube(url)
        if choice == "Video (MP4)":
            stream = yt.streams.get_highest_resolution()
            download_path = os.path.join(download_location, f"{yt.title}.mp4")
            stream.download(output_path=download_location, filename=yt.title)
            old_file_path = os.path.join(download_location, f"{yt.title}.")
            os.rename(old_file_path, download_path)
            os.rename(download_path, os.path.join(download_location, f"{yt.title}.mp4"))
            status_label.config(text=f"SUCCESS! Video saved as: {download_path}")
            return download_path
        elif choice == "Audio (MP3)":
            stream = yt.streams.filter(only_audio=True).first()
            download_path = os.path.join(download_location, f"{yt.title}.mp3")
            stream.download(output_path=download_location, filename=yt.title)
            old_file_path = os.path.join(download_location, f"{yt.title}.")
            os.rename(old_file_path, download_path)
            os.rename(download_path, os.path.join(download_location, f"{yt.title}.mp3"))
            status_label.config(text=f"SUCCESS! Audio saved as: {download_path}")
            return download_path
        #download_path = os.path.join(download_location, stream.default_filename)
        #stream.download(output_path=download_location)
        #status_label.config(text=f"SUCCESS! File saved as: {download_path}")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")