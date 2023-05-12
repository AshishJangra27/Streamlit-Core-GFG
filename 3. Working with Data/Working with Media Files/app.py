import streamlit as st
from PIL import Image

# Image from Path
st.title('1. Image from Path')
img = Image.open('/Users/ashishzangra/Documents/Streamlit/Models.jpeg')
st.image(img)

# Image from Link
st.title('2. Image from Link')
st.image('https://media.geeksforgeeks.org/gfg-gg-logo.svg', width = 700)

# Video
st.title('3. Video')
video_file = open('/Users/ashishzangra/Documents/Streamlit/video.mp4','rb')
st.video(video_file, start_time = 20)

# Audio
st.title('4. Audio')
audio_file = open('/Users/ashishzangra/Documents/Streamlit/sample.mp3','rb')
st.audio(audio_file.read())
