# import whisper

# model = whisper.load_model("base")

# def transcribe(audio_path):
#     result = model.transcribe(audio_path)
#     return result["text"]

# import openai
# import os
# from dotenv import load_dotenv
# load_dotenv()  # Load .env variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def transcribe_audio(audio_path: str) -> str:
#     with open(audio_path, "rb") as f:
#         transcript = openai.Audio.transcribe("whisper-1", f)
#     return transcript["text"]

import openai
import os
from dotenv import load_dotenv
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text