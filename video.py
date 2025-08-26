from pytubefix import YouTube


import os



link = input(">>>")

yt = YouTube(link)

#os.system("start "+yt.thumbnail_url)

yt.streams.filter()
stream = yt.streams.get_highest_resolution()
i=0
name=str(i)
while os.path.exists("videos\\"+name+".mp4"):
    i+=1
    name=str(i)
try : stream.download("videos")
except :stream.download("videos",str(i)+".mp4")
        
