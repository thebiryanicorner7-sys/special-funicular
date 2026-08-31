import io
import requests
import streamlit as st

st.set_page_config(page_title="Neural Canvas AI", page_icon="🎨", layout="centered")

st.title("🎨 Neural Canvas AI")
st.write("Generate breathtaking images instantly using AI.")

prompt = st.text_area("Describe your vision...", placeholder="A cyberpunk cityscape at twilight, neon-soaked streets...")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": "Bearer hf_your_free_api_key_here"}

def generate_image(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content

if st.button("GENERATE MAGIC"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Creating your masterpiece... (Takes 10-20 seconds)"):
            image_bytes = generate_image({"inputs": prompt})
            try:
                image = io.BytesIO(image_bytes)
                st.image(image, caption=f"Generated for: '{prompt}'", use_column_width=True)
                st.success("Image generated successfully!")
            except Exception:
                st.error("API is currently loading the model or limit reached. Please try again in a moment.")
