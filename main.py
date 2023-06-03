from pytube import YouTube

def download(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print("something went wrong")


download(link="https://youtu.be/7KSNmziMqog")
