"""
影片片段下載教學（yt-dlp + ffmpeg）
示範如何使用 **yt-dlp 搭配 ffmpeg 後端**，
下載線上影片中的「指定時間片段」，作為後續 **OpenCV 影片處理** 的前處理步驟。
(1)到https://www.gyan.dev/ffmpeg/builds/  下載   ffmpeg-release-essentials.zip
(2)將檔案解壓縮 把整個資料夾搬到：C:\ffmpeg\
Download a specific video segment using yt-dlp + ffmpeg.

This script demonstrates how to:
- call yt-dlp via Python
- specify ffmpeg location (Windows-friendly)
- download only a selected time segment
"""

import subprocess
import sys

 """
    參數說明
    ----------
    video_url : str
        影片網址
    time_range : str
        影片時間區段，格式為 "*HH:MM:SS-HH:MM:SS"
    ffmpeg_path : str | None
        ffmpeg 執行檔所在資料夾（可選，Windows 建議填寫）
    """
def download_video_clip(
    video_url: str,
    time_range: str,
    ffmpeg_path: str | None = None,
):
   
 """
    參數說明
    ----------
    sys.executable, "-m", "yt_dlp","--download-sections",
    這一行等價於:  python -m yt_dlp
    """
    cmd = [
        sys.executable, "-m", "yt_dlp","--download-sections",
        time_range,
    ]


 """
    參數說明
    ----------
    cmd.extend(["--ffmpeg-location", ffmpeg_path])
    等價於 CLI：   --ffmpeg-location C:\path\to\ffmpeg\bin
    明確告訴 yt-dlp： ffmpeg 在這個位置
    """
    if ffmpeg_path:
        cmd.extend(["--ffmpeg-location", ffmpeg_path])

    cmd.append(video_url)

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    # 範例設定（請自行修改）
    VIDEO_URL = "https://www.ted.com/talks/john_mills_how_we_built_watch_duty_the_lifesaving_wildfire_alert_app"
    TIME_RANGE = "*00:00:03-00:01:43"

    # Windows 使用者可指定 ffmpeg 路徑
    FFMPEG_PATH = r"C:\Users\TMP-214\Downloads\ffmpeg\bin"
    # 範例：
    # FFMPEG_PATH = r"C:\\path\\to\\ffmpeg\\bin"

    download_video_clip(
        video_url=VIDEO_URL,
        time_range=TIME_RANGE,
        ffmpeg_path=FFMPEG_PATH,
    )



# cmd = [
#     sys.executable, "-m", "yt_dlp",
#     "--ffmpeg-location", r"C:\Users\TMP-214\Downloads\ffmpeg\bin",
#     "--download-sections", "*00:00:03-00:01:43",
#     "https://www.ted.com/talks/john_mills_how_we_built_watch_duty_the_lifesaving_wildfire_alert_app"
# ]
# subprocess.run(cmd, check=True)
