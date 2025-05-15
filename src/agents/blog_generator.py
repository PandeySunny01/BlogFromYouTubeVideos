# from transformers import pipeline

# generator = pipeline("text-generation", model="gpt2")

# def write_blog(summary):
#     prompt = f"Write a professional and engaging blog post based on the following summary:\n\n{summary}\n\nBlog Post:"
#     result = generator(prompt, max_length=500, num_return_sequences=1)[0]["generated_text"]
#     return result

def format_blog(title: str, content: str) -> str:
    blog = f"# {title}\n\n{content}"
    return blog