from pytubefix import YouTube


import os



link = input(">>>")

yt = YouTube(link)

#os.system("start "+yt.thumbnail_url)

yt.streams.filter(only_video=True)
stream = yt.streams.get_highest_resolution()
i=0
name=str(i)
while os.path.exists("images\\"+name+".mp4")or os.path.exists("images\\"+name+".avi"):
    i+=1
    name=str(i)
try : stream.download("images")
except :stream.download("images",str(i)+".mp4")
        
