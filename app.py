import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="AI Image Studio", page_icon="🎨")

st.title("🎨 AI Image Studio")
st.write("Create stunning AI-generated artwork with customizable styles.")

# ---------------- Sidebar ----------------
st.sidebar.header("Settings")

art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Realistic",
        "Anime",
        "Watercolor",
        "Oil Painting",
        "Pixel Art",
        "Cyberpunk",
        "Fantasy"
    ]
)

width = st.sidebar.slider("Width", 256, 1024, 512, step=64)
height = st.sidebar.slider("Height", 256, 1024, 512, step=64)

magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")

# ---------------- Prompt ----------------
prompt = st.text_input(
    "Enter your image prompt",
    placeholder="A dragon flying over a futuristic city"
)

generate = st.button("🎨 Generate Image")
surprise = st.button("🎲 Surprise Me!")

# Creative prompts
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon working as a barista in a cozy cafe",
    "A floating castle above the clouds at sunset",
    "A giant jellyfish illuminating an underwater city"
]

# ---------------- Image Generation ----------------
if generate or surprise:

    if surprise:
        prompt = random.choice(surprise_prompts)
        st.info(f"Surprise Prompt: **{prompt}**")

    if prompt.strip():

        full_prompt = f"{prompt}, {art_style} style"

        if magic_enhance:
            full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

        encoded_prompt = urllib.parse.quote(full_prompt)

        url = (
            f"https://image.pollinations.ai/prompt/"
            f"{encoded_prompt}?width={width}&height={height}"
        )

        with st.spinner("Generating masterpiece..."):
            response = requests.get(url)

        if response.status_code == 200:

            st.image(
                response.content,
                caption=f"{art_style} Style",
                use_container_width=True
            )

            st.download_button(
                "⬇️ Download Image",
                data=response.content,
                file_name=f"{art_style.lower().replace(' ', '_')}_image.png",
                mime="image/png"
            )

        else:
            st.error("Image generation failed. Please try again.")

    else:
        st.warning("Please enter a prompt.")