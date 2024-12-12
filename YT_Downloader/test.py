# importing modules
from pytube import YouTube

def download_video(url):
    youtube_link = YouTube(url)
    youtube_link - youtube_link.streams.get_highest_resolution()
    
    try:
        youtube_link.download()
    
    except:
        print("An error occurred while downloading the video.")
    print("Download has connected successfully")

url = input("Enter link here: ")
download_video(url)