import yt_dlp
import tkinter as tk
from tkinter import messagebox
import os

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return

    # Ensure the download folder exists
    download_folder = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save in "downloads" folder
            'postprocessors': [{
                'key': 'FFmpegMerger',  # Merge video and audio
            }],
            'ffmpeg_location': r'C:\ffmpeg\bin',  # Path to FFmpeg
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Download completed! File saved in: {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Design
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter YouTube Video URL:", font=("Arial", 12))
label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video, bg="#4CAF50", fg="white", font=("Arial", 12))
download_button.pack(pady=20)

root.mainloop()