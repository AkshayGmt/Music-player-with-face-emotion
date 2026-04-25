import streamlit as st
import numpy as np
import cv2
import random
from PIL import Image

st.set_page_config(page_title="Emotion Music Recommender")

st.title("🎧 Emotion-Based Music Recommender")

# ✅ Emotion list (mock)
emotions = ["happy", "sad", "angry", "neutral"]

# ✅ Music mapping
music_map = {
    "happy": ["🎵 Happy Song 1", "🎵 Party Vibes", "🎵 Dance Track"],
    "sad": ["🎧 Lo-fi Chill", "🎧 Soft Piano", "🎧 Calm Mood"],
    "angry": ["🎼 Relaxing Music", "🎼 Meditation", "🎼 Instrumental"],
    "neutral": ["🎶 Random Mix", "🎶 Indie Songs", "🎶 Focus Music"]
}

# ✅ Upload Image
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Emotion"):
        # ❗ Mock prediction (no model needed)
        pred = random.choice(emotions)

        st.success(f"Detected Emotion: {pred}")

        # Show songs
        st.subheader("🎵 Recommended Songs:")
        for song in music_map[pred]:
            st.write(f"- {song}")
