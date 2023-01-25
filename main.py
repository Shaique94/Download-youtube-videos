from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
#funtions

def select_path():
    path = filedialog.askdirectory() #allow user to select folder from system to store the downloaded video
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected
    user_path = path_label.cget("text")
    screen.title('Downloading')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip =VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title('Download Complete! Download another file')




screen = Tk()
title = screen.title("YouTube Download")
canvas = Canvas(screen,width=500,height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file='youtube-logo.png')

# resize logo image
logo_img =logo_img.subsample(2,2)

canvas.create_image(250,80,image=logo_img)

#link field
link_field = Entry(screen,width=50)
link_label = Label(screen,text="Enter Download link ",font=('Arial',15))

#Select path for saving the file
path_label = Label(screen,text="Select path for download",font=('Arial',15))
select_btn = Button(screen,text="Select",command=select_path)
#Add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

# Add widgets to the window or make visible the link field

canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)

#Download buttons

download_button = Button(screen,text="Download File",command=download_file)
canvas.create_window(250,390,window=download_button)


screen.mainloop()