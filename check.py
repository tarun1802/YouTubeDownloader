from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=BH7D2aLPekc")
stream=yt.streams.all()
print(stream)