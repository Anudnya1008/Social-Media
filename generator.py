from openai import OpenAI
import base64
import os
from dotenv import load_dotenv
from sympy import re
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_image(username, prompt, n, size):
    user_name = username.replace(" ", "_")
    OUTPUT_DIR = os.path.join("generated_images", user_name)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=n,
        size=size,
    )

    image_files = []

    for i, img in enumerate(response.data):
        image_base64 = img.b64_json
        image_bytes = base64.b64decode(image_base64)
        file_path = os.path.join(OUTPUT_DIR, f"image_{i+1}.png")
        file_name = f"image_{i+1}.png"
        with open(file_path, "wb") as f:
            f.write(image_bytes)

        image_files.append(os.path.join("generated_images", user_name, file_name))

    return image_files


def generate_captions(prompt:str, n):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                   "You are a professional social media content writer.\n"
                   "Follow the user's instructions exactly.\n"
                   f"Write exactly {n} captions.\n"
                   
                   "Do NOT use '---'. Do NOT number captions.\n"
                   "Return only the captions with the delimiter, nothing else."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7, 
    )
   
    value = response.choices[0].message.content.strip()
    captions = extract_captions(value, n)
    return captions[:n]


def extract_captions(value: str, n: int):
    value = (value or "").strip()
    if not value:
        return []

    blocks = [b.strip() for b in re.split(r"\n\s*\n", value) if b.strip()]

    captions = []
    i = 0

    while i < len(blocks):
        b = blocks[i]

        if b.lstrip().startswith("#"):
            if captions:
                captions[-1] = captions[-1].rstrip() + "\n" + b
            i += 1
            continue

        if i + 1 < len(blocks) and blocks[i + 1].lstrip().startswith("#"):
            captions.append(b + "\n" + blocks[i + 1])
            i += 2
        else:
            captions.append(b)
            i += 1

        if len(captions) >= n:
            break

    return captions[:n]