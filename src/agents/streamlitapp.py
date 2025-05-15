import streamlit as st
import sys
import os
import re
import yt_dlp

# Add the root directory to sys.path (2 levels up from this file)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
st.set_page_config(page_title="YouTube to Blog", layout="centered")

from src.agents.main import youtube_to_blog  # adjust path as needed

##Add a YouTube URL validator with regex
def is_valid_youtube_url(url: str) -> bool:
    # Basic pattern to check for YouTube URLs
    youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(youtube_regex, url) is not None



##Check actual video availability using yt-dlp
def is_youtube_video_accessible(url: str) -> bool:
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            ydl.extract_info(url, download=False)
        return True
    except Exception:
        return False


st.title("📹 YouTube to Blog 📝")
st.markdown("Convert a YouTube video into a readable blog post.")

youtube_url = st.text_input("Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Blog"):
    if not youtube_url or not is_valid_youtube_url(youtube_url):
        st.warning("Please enter a valid YouTube URL.")
    elif not is_youtube_video_accessible(youtube_url):
        st.error("The video is unavailable or restricted.")
    else:
        with st.spinner("Generating blog..."):
            try:
                blog = youtube_to_blog(youtube_url)
                st.success("Blog generated!")
                st.markdown("### ✍️ Blog Content")
                st.markdown(blog)
                st.download_button("Download as Markdown", blog, file_name="blog_post.md")
            except Exception as e:
                st.error(f"Error: {str(e)}")


    