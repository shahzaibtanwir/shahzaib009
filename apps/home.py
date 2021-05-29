import streamlit as st
from PIL import Image

def app():
    st.subheader(""" Youtube Video Downloader """)
    image = Image.open('yt_project.png')
    st.image(image)
    