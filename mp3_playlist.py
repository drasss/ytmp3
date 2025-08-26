import pytubefix as pt
import os
from audio_extract import extract_audio
import time

link = input(">>>")
yt = pt.Playlist(link)


lim = 15 #  max duration in minutes

lim*=60
#os.system("start "+yt.thumbnail_url)
print("Playlist title:", yt.title)
print("Number of videos in playlist:", len(yt.videos))

if not os.path.exists("playlist"):
    os.mkdir("playlist")
if not os.path.exists("playlist\\"+yt.title):
    os.mkdir("playlist\\"+yt.title)

nbd=len(os.listdir("playlist\\"+yt.title))
print("Number of videos already downloaded:", nbd)

start=input("Start from video number (default ="+str(nbd)+")))): ")

ts=time.time()
if start == "":
    start = nbd
else:
    start = int(start)
skip=[]
for vid in range(start,len(yt.videos)):

    if vid < start:
        continue

    video = yt.videos[vid]
    print(f"    Downloading video {vid + 1}/{len(yt.videos)}: {video.title}")

    # Download the video
    stream = video.streams.get_audio_only()
    i = vid + 1  # Use the video index as the file name
    if video.length > lim:
        skip.append(video.title)
        print(f"    Skipping {video.title} due to length ({video.length} seconds > {lim} seconds)")
        continue
  
    name = str(i)
    
    stream.download("playlist\\"+yt.title, str(i)+".mp4")

    def MP4ToMP3(mp4, mp3):
        extract_audio(input_path=mp4, output_path=mp3)

    VIDEO_FILE_PATH = "playlist\\"+yt.title+"\\"+str(i)+".mp4"
    AUDIO_FILE_PATH = "playlist\\"+yt.title+"\\"+str(i)+".mp3"
    MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
    try:
        os.rename(AUDIO_FILE_PATH, "playlist\\"+yt.title+"\\"+video.title+".mp3")
    except :
        os.rename(AUDIO_FILE_PATH, "playlist\\"+yt.title+"\\"+str(i)+".mp3")
    os.remove(VIDEO_FILE_PATH)
print("--"*20)
print("videos downloaded and converted to MP3.")
print("Skipped videos due to length:")
for title in skip:
    print(f"    {title}")
print(f"Total time taken: {time.time() - ts:.2f} seconds")
