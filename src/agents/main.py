# from downloader import download_audio
# from transcriber import transcribe
# from summarizer import summarize
# from src.agents.blog_generator import write_blog
# from title_generator import generate_title

# def generate_blog_from_youtube(video_url):
#     print("[1] Downloading audio...")
#     audio_path = download_audio(video_url)

#     print("[2] Transcribing audio...")
#     transcript = transcribe(audio_path)

#     print("[3] Summarizing transcript...")
#     summary = summarize(transcript)

#     print("[4] Writing blog post...")
#     blog_post = write_blog(summary)

#     print("[5] Generating title...")
#     title = generate_title(summary)

#     return title, blog_post

# if __name__ == "__main__":
#     url = input("Enter YouTube video URL: ")
#     title, blog_post = generate_blog_from_youtube(url)
#     print(f"\n--- Blog Title ---\n{title}")
#     print(f"\n--- Blog Post ---\n{blog_post}")

from downloader import download_audio
from transcriber import transcribe_audio
from summarizer import summarize_text
from blog_generator import format_blog
from utils import get_video_title
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def youtube_to_blog(youtube_url: str, output_path="output"):
    print("Downloading audio...")
    audio_file = download_audio(youtube_url)

    print("Transcribing audio...")
    transcript = transcribe_audio(audio_file)

    print("Summarizing transcript...")
    blog_content = summarize_text(transcript)

    print("Formatting blog...")
    title = get_video_title(youtube_url)
    blog_post = format_blog(title, blog_content)

    # Save blog post
    # os.makedirs(output_path, exist_ok=True)
    # with open(f"{output_path}/{title}.md", "w", encoding="utf-8") as f:
    #     f.write(blog_post)

    # print(f"Blog saved to {output_path}/{title}.md")

     # Instead of saving to a file:
    return blog_post

# Example usage
if __name__ == "__main__":
    youtube_to_blog("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
   
