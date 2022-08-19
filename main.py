import time
from pytube import YouTube
link = str(input("Enter the vid you want: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Video was downloaded!")
time.sleep(5)
