import streamlit as st
from multiapp import MultiApp
from apps import home, yt_video_downloader

app = MultiApp()

st.markdown(""" Youtube Video Downloader """)

st.text("Use The Drop Down Menu Below To Navigate Between Homepage & Video Downloader.")

# Add all your application here

app.add_app("Home", home.app)
app.add_app("yt_video_downloader", yt_video_downloader.clickdownload)

# The main app
app.run()