from pytubefix import YouTube

import os
from audio_extract import extract_audio

link = input(">>>")

yt = YouTube(link)

#os.system("start "+yt.thumbnail_url)

stream=yt.streams.get_audio_only()
i=0
name=str(i)
while os.path.exists("mp4\\"+name+".mp4"):
    i+=1
    name=str(i)
stream.download("mp4",str(i)+".mp4")


def MP4ToMP3(mp4, mp3):
    extract_audio(input_path=mp4, output_path=mp3)


VIDEO_FILE_PATH = "mp4\\"+str(i)+".mp4"
AUDIO_FILE_PATH = "mp3\\"+str(i)+".mp3"
MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
# MoviePy - Writing audio in /Full/File/Path/ToSong.mp3
# MoviePy - Done.    
os.rename(AUDIO_FILE_PATH, "mp3\\"+yt.title+".mp3")
