from pytubefix import YouTube


import os



link = input(">>>")

yt = YouTube(link)

os.system("start "+yt.thumbnail_url)

        
