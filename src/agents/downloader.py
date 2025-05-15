# from pytube import YouTube

# def download_audio(video_url, filename="audio.mp4"):
#     yt = YouTube(video_url)
#     stream = yt.streams.filter(only_audio=True).first()
#     audio_path = stream.download(filename=filename)
#     return audio_path


# from pytube import YouTube
# import os

# def download_audio(youtube_url: str, output_path: str = "downloads") -> str:
#     yt = YouTube(youtube_url)
#     audio_stream = yt.streams.filter(only_audio=True).first()
#     os.makedirs(output_path, exist_ok=True)
#     audio_file = audio_stream.download(output_path=output_path)
#     return audio_file


# def download_audio(youtube_url: str, output_path: str = "downloads") -> str:
#     yt = YouTube(youtube_url)
#     audio_stream = yt.streams.filter(only_audio=True).first()
#     if audio_stream is None:
#         raise ValueError("No audio stream available for this video.")

#     os.makedirs(output_path, exist_ok=True)
#     audio_file = audio_stream.download(output_path=output_path)
#     return audio_file


import yt_dlp
import os

def download_audio(youtube_url: str, output_path: str = "downloads") -> str:
    os.makedirs(output_path, exist_ok=True)
    output_template = os.path.join(output_path, "%(title)s.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'ffmpeg_location': 'D:/ffmpeg/bin',  # <-- Adjust this path to where ffmpeg.exe is
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)
        base, _ = os.path.splitext(filename)
        return base + ".mp3"