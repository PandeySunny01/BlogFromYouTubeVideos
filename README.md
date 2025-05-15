🧠 Project: Blog from YouTube Videos
This project automates the process of converting YouTube videos into well-structured blog posts using audio transcription, language models, and a Streamlit UI. It enables users to generate content-rich, SEO-friendly blog articles from educational or informative videos in just a few clicks.

🚀 Key Features
🔗 Accepts any public YouTube video URL.

🔊 Extracts and transcribes audio using OpenAI Whisper.

🧠 Summarizes and reformats transcripts into blog-style content using OpenAI GPT models.

📝 Generates titled sections with headings and summaries for readability.

🖼️ Adds relevant AI-generated images or Unsplash-sourced visuals to support blog sections.

🌐 Displays the output in a clean Streamlit web interface.


🧱 Project Structure

BlogFromYouTubeVideos/
│
├── .env                       # API keys and secrets
├── requirements.txt           # Dependencies
├── README.md                  # Project description
│
├── src/
│   ├── agents/
│   │   ├── main.py            # Main pipeline: YouTube to blog
│   │   ├── utils.py           # Helper functions: title extraction, audio, formatting
│   │   └── streamlitapp.py    # Streamlit front-end
│   │
│   └── output/                # (Optional) Saved blog files (if needed)
│
└── blogenv/                   # Python virtual environment


⚙️ Workflow Overview
YouTube URL Input
The user provides a YouTube video link via the Streamlit app.

Video Metadata
The system extracts the video’s title and basic info using pytube.

Audio Extraction
Uses yt-dlp to download audio and ffmpeg to convert it to .mp3 format.

Transcription
OpenAI Whisper (via openai.Audio.transcribe) transcribes the audio into text.

Content Summarization
The transcript is broken into chunks. Each chunk is sent to GPT-3.5 or GPT-4:

Summarized into paragraph form.

Assigned a custom heading and a short section summary.

Image Generation (Optional)
For each section, a relevant image is generated using OpenAI's image model or fetched from Unsplash.

Blog Display
The final content is rendered as a beautifully formatted Streamlit webpage with:

Section titles

Paragraphs

Supporting images


📦 Technologies Used
Python 3.10+

Streamlit – UI framework

yt-dlp / pytube – YouTube audio extraction

ffmpeg – Audio conversion

OpenAI API – Transcription + Content generation

dotenv – Environment management

Requests / PIL – Optional image handling


📌 Future Improvements
✅ Image upload/download and storage in local or cloud

🔍 SEO optimization of blog posts

🧠 Multi-language support

🧾 Export to .md, .html, or CMS integration