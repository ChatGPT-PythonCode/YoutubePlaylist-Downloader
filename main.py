import tkinter as tk
from tkinter import filedialog
import youtube_dl

def download_playlist():
    playlist_url = playlist_url_entry.get()
    save_folder = filedialog.askdirectory()

    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{save_folder}/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([playlist_url])

# GUI setup
root = tk.Tk()
root.title("YouTube Playlist Downloader")

# Playlist URL Entry
playlist_url_label = tk.Label(root, text="Playlist URL:")
playlist_url_label.pack(pady=10)
playlist_url_entry = tk.Entry(root, width=40)
playlist_url_entry.pack(pady=10)

# Save Folder Button
save_folder_button = tk.Button(root, text="Select Save Folder", command=download_playlist)
save_folder_button.pack(pady=10)

# Download Button
download_button = tk.Button(root, text="Download Playlist", command=download_playlist)
download_button.pack(pady=10)

# Run the GUI
root.mainloop()