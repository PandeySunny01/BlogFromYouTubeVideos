import streamlit as st
import requests
from PIL import Image
from io import BytesIO

url = "https://httpbin.org/image/png"

response = requests.get(url)
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="Loaded from httpbin.org", use_container_width = False, width=300)
else:
    st.error(f"Failed to load image. Status code: {response.status_code}")