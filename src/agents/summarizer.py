# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize(text, chunk_size=1000):
#     chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
#     summary = " ".join(
#         summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
#         for chunk in chunks
#     )
#     return summary



# import openai


# def summarize_text(text: str, style: str = "blog") -> str:
#     prompt = (
#         f"Convert the following transcript into a well-structured {style} article:\n\n"
#         f"{text}\n\nBlog:"
#     )
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7
#     )
#     return response.choices[0].message["content"]


import openai
import os

def summarize_text(text: str, style: str = "blog") -> str:
    prompt = (
        f"Convert the following transcript into a well-structured {style} article:\n\n"
        f"{text}\n\nBlog:"
    )

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content