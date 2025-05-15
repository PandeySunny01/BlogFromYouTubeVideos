import streamlit as st
import os
import sys
import re
import yt_dlp
from PIL import Image
import openai
import base64
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Create the OpenAI client
client = openai.OpenAI(api_key=api_key)
# Ensure you use the new openai v1 API client
#client = openai.OpenAI()
# Add root to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.agents.main import youtube_to_blog  # Your blog generator function


# ------------------------
# Utility Functions
# ------------------------
def is_valid_youtube_url(url: str) -> bool:
    pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(pattern, url) is not None

def is_youtube_video_accessible(url: str) -> bool:
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            ydl.extract_info(url, download=False)
        return True
    except Exception:
        return False


def insert_images_from_keywords(blog_text):
    keywords = ["AI", "Machine Learning", "Data", "Robotics"]
    images = {
        "AI": "https://source.unsplash.com/800x400/?artificial-intelligence",
        "Machine Learning": "https://source.unsplash.com/800x400/?machine-learning",
        "Robotics": "https://source.unsplash.com/800x400/?robot",
        "Data": "https://source.unsplash.com/800x400/?data"
    }

    for keyword in keywords:
        if keyword.lower() in blog_text.lower():
            st.image(images[keyword], caption=keyword, use_container_width =True)



def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url


def generate_summary(paragraph):
    # Using OpenAI GPT-3 to summarize each paragraph (alternative: simple heuristics)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        #prompt=f"Summarize this paragraph in a few words: {paragraph}",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates short, engaging titles for blog sections based on their content."},
            {"role": "user", "content": f"Create a blog section heading for the following paragraph:\n\n{paragraph}"}
        ],
        temperature=0.5,
        max_tokens=30
    )
    #return response.choices[0].text.strip()
    return response.choices[0].message.content



# def display_blog(content):
#     sections = content.split("\n\n")  # Split blog into sections by blank lines

#     for section in sections:
#         if section.startswith("#"):  # Check if it's a heading (markdown style)
#             # Display headings (e.g., # Heading, ## Subheading)
#             st.markdown(f"<h2 style='color:#4CAF50;'>{section}</h2>", unsafe_allow_html=True)
#         else:
#             # Display paragraphs (normal text)
#             st.markdown(f"<p style='font-size:16px;color:#555'>{section}</p>", unsafe_allow_html=True)

def display_blog(content):
    sections = content.split("\n\n")  # Split blog into sections by blank lines

    for i,section in enumerate(sections, 1):
        if section.startswith("#"):  # If it's a heading
            # Display the heading as is
            st.markdown(f"<h2 style='color:#4CAF50;'>{section}</h2>", unsafe_allow_html=True)
        else:
            # For paragraphs, generate a summary heading
            summary = generate_summary(section)  # Generate summary for paragraph
            st.markdown(f"<h4 style='color:#3e3e3e'>{i}.{summary}</h4>", unsafe_allow_html=True)  # Display summary as subheading
            st.markdown(f"<p style='font-size:16px;color:#555'>{section}</p>", unsafe_allow_html=True)  # Display paragraph content

# ------------------------
# Streamlit UI
# ------------------------

st.set_page_config(page_title="YouTube to Blog", layout="wide")

# ---- Header ----
st.markdown("""
    <h1 style='text-align: center;'>📹 YouTube to Blog ✍️</h1>
    <p style='text-align: center; font-size: 18px;'>
        Convert YouTube videos into structured, readable blog posts using AI.
    </p>
    <hr>
""", unsafe_allow_html=True)

# ---- Input ----
st.markdown("### 🔗 Paste your YouTube video link below:")
youtube_url = st.text_input("", placeholder="e.g. https://www.youtube.com/watch?v=...")

col1, col2 = st.columns([1, 5])
with col1:
    generate = st.button("🚀 Generate Blog")

# ---- Result ----
if generate:
    if not youtube_url or not is_valid_youtube_url(youtube_url):
        st.warning("⚠️ Please enter a valid YouTube URL.")
    elif not is_youtube_video_accessible(youtube_url):
        st.error("❌ This video is either unavailable, private, or region-restricted.")
    else:
        with st.spinner("⏳ Processing video and generating blog..."):
            try:
                blog = youtube_to_blog(youtube_url)
                st.success("✅ Blog generated successfully!")
                st.markdown("## 📝 Blog Content")
                st.markdown("---")
                img_url = generate_image(blog)
                st.image(img_url, caption="Generated by DALL·E 3")
                # Nicely formatted output
                # st.markdown(f"<div style='background-color:#f9f9f9;padding:20px;border-radius:10px;'>"
                #             f"{blog.replace('\n', '<br>')}"
                #             f"</div>", unsafe_allow_html=True)
                display_blog(blog)
                #st.markdown(blog, unsafe_allow_html=False)
                st.markdown("---")
                #insert_images_from_keywords(blog)
                #import streamlit as st

                #st.title("🖼️ Test Image Display")

                #st.image("https://source.unsplash.com/800x400/?artificial-intelligence", caption="Artificial Intelligence", use_container_width =True)
                # from PIL import Image

                # img = Image.open("Images/AI.jpg")
                # st.image(img, caption="Local Image Test", use_container_width=True)
                st.download_button("💾 Download Blog as Markdown", blog, file_name="blog_post.md")
                # img_url = generate_image(blog)
                # st.image(img_url, caption="Generated by DALL·E 3")
            except Exception as e:
                st.error(f"🚫 Error: {str(e)}")


   