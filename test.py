import ollama
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "image.jpg"


encoded_image = encode_image(image_path)


full_prompt = "Describe the contents of this image."


response = ollama.chat(
    model="llava",
    messages=[
        {"role": "system", "content": "You are an AI that interprets images."},
        {"role": "user", "content": full_prompt, "images": [encoded_image]},
    ],
    options={"num_ctx": 8192}
)


print(response["message"]["content"])
