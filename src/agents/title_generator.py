from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_title(summary):
    prompt = f"Generate a catchy blog post title for the following content:\n{summary}"
    title = generator(prompt, max_length=15, num_return_sequences=1)[0]["generated_text"]
    return title.strip()

# import yt_dlp

# def get_video_title(youtube_url: str) -> str:
#     with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
#         info = ydl.extract_info(youtube_url, download=False)
#         return info.get("title", "Untitled Video")


