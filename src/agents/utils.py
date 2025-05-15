# from pytube import YouTube

# def get_video_title(youtube_url: str) -> str:
#     return YouTube(youtube_url).title

import yt_dlp

def get_video_title(youtube_url: str) -> str:
    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info.get("title", "Untitled Video")