"""
Download a specific video segment using yt-dlp + ffmpeg.

This script demonstrates how to:
- call yt-dlp via Python
- specify ffmpeg location (Windows-friendly)
- 
- download only a selected time segment
"""

import subprocess
import sys


def download_video_clip():
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--ffmpeg-location", r"C:\Users\TMP-214\Downloads\ffmpeg\bin",
        "--download-sections", "*00:00:03-00:01:43",
        "https://www.ted.com/talks/john_mills_how_we_built_watch_duty_the_lifesaving_wildfire_alert_app",
    ]

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    download_video_clip()
