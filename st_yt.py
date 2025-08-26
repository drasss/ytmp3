from pytubefix import YouTube
import streamlit as st

import os

import io
from moviepy.editor import *

link = st.text_input("link")


if st.button("Download"):
    if link=="":
        link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt = YouTube(link)

    #os.system("start "+yt.thumbnail_url)

    stream=yt.streams.filter(only_audio=True).get_audio_only()

    # Convert the audio to MP3 format using moviepy.editor
    audio = AudioFileClip(stream.url)
    audio.write_audiofile("output.mp3")
    with open("output.mp3", "rb") as f:
                byte_content = f.read()
                st.download_button(
                    label="Download MP3",
                    data=byte_content,
                    file_name="output.mp3",
                    mime="audio/mpeg",
                )
    # buf = io.BytesIO()

    # stream.stream_to_buffer(buf)

    # buf.seek(0)

    # data = buf.read()


    # video_clip = VideoFileClip(data)
    # audio_clip = video_clip.audio
    # # Créer un objet IO pour le fichier MP3
    # mp3_io = io.BytesIO()

    # # Écrire le fichier MP3 dans l'objet IO
    # audio_clip.write_audiofile(mp3_io, codec='mp3')

    # # Revenir au début de l'objet IO
    # mp3_io.seek(0)
    # dat=mp3_io.read()
    
    i=0
    name=str(i)
    while os.path.exists("videos\\"+name+".mp4"):
        i+=1
        name=str(i)
    try : stream.download("videos")
    except :stream.download("videos",str(i)+".mp4")

