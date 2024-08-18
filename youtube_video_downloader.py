# pip install yt-dlp

import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully")
 
    except Exception as e:
        print(f"An error occurred: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")

    if not video_url.startswith("https://www.youtube.com/"):
        print("Invalid YouTube URL.")
    else:
        save_dir = open_file_dialog()

        if save_dir and os.path.isdir(save_dir):
            print("Started download...")
            download_video(video_url, save_dir)
        else:
            print("Invalid save location.")
