from pytubefix import YouTube
import io
def extraction(link):
    yt = YouTube(link)
    yt.streams.filter()
    stream = yt.streams.get_highest_resolution()
    image=yt.thumbnail_url
    yt.streams.filter()
    stream = yt.streams.get_highest_resolution()
    buf = io.BytesIO()
    stream.stream_to_buffer(buf)
    buf.seek(0)
    data = buf.read()
    return data, image, yt.title

