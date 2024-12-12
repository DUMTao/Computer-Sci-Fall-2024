#Importing the Modules
from pytube import YouTube
from tkinter import *
import tkinter as ttk
#############################################


window = ttk.Tk()
window.title("YouTube Downloader")
        
window.geometry("700x350") # Defines the size of the window


def downloader():
    global quality # global variable to access the quality variable from the class
    t = text.get() # gets the text from the entry field
    video = YouTube(t)
        
    # Checking the quality of the video
    if quality1.get() == 18:
        quality1 = 18
        
    elif quality2.get() == 22:
        quality2 = 22
        
    elif quality3.get() == 37:
        quality3 = 37
    
    video_streams = video.streams.filter(file_extension='mp4').get_by_itag(quality) # Specifies the video quality of the video
    video_streams.download(filename='Untitled', output_path="video_path")
    
    ttk.Label(window, text="Downloaded Successfully", font=("Arial", 15)).pack()    
    
    
# Creating the lables
ttk.Label(window, text="YouTube Downloader", font=("Arial", 20), pady=15).pack() # Creates widget on the GUI window that displays the text
ttk.Label(window, text="Enter the YouTube Video URL", font=("Arial", 15)).pack()
text = StringVar(window)
        
# Assigining entry field for the link
ttk.Entry(window, textvariable=text, width=50).pack() # Creates an entry widget on the window
text = StringVar(window, value='Youtube URL')
quality1 = IntVar()
quality2 = IntVar()
quality3 = IntVar()

# Creating quality buttons
ttk.Checkbutton(text='360p', onvalue=18, offvalue=0, variable=quality1).pack() # Creates a checkbutton widget on the window
ttk.Checkbutton(text='720p', onvalue=22, offvalue=0, variable=quality2).pack()
ttk.Checkbutton(text='1080p', onvalue=37, offvalue=0, variable=quality3).pack()
        
# Creating download button
ttk.Button(window, text="Download", bg='red', command=downloader).pack() # Creates a button widget on the window





window.mainloop()


