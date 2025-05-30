#!/usr/bin/env python3
"""
YouTube Downloader with yt-dlp and cookie support.
"""

import os
from yt_dlp import YoutubeDL
from utils import print_colored, Color

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url.strip()
        self.download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(self.download_dir, exist_ok=True)
        self.cookie_path = os.path.join(os.getcwd(), "cookies.txt")  # Put your cookie file here

    def download_video(self):
        """Download the best quality video and audio combined."""
        ydl_opts = {
            'cookiefile': self.cookie_path,
            'outtmpl': os.path.join(self.download_dir, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'quiet': False
        }

        try:
            print_colored("Starting video download with yt-dlp...", Color.YELLOW)
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            print_colored("Download complete!", Color.GREEN)
        except Exception as e:
            print_colored(f"Error downloading video: {e}", Color.RED)

    def download_audio(self):
        """Download audio only and convert to MP3."""
        ydl_opts = {
            'cookiefile': self.cookies.txt,
            'outtmpl': os.path.join(self.download_dir, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False
        }

        try:
            print_colored("Starting audio download with yt-dlp...", Color.YELLOW)
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            print_colored("Audio download complete!", Color.GREEN)
        except Exception as e:
            print_colored(f"Error downloading audio: {e}", Color.RED)
