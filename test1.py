#Import everything needed  
from moviepy.editor import *
from tkinter import *
import easygui
import pafy 
import youtube_dl

def save_video(clip):
#saving the clip 
 save_path=easygui.filesavebox()
 clip.write_videofile(save_path) 

def find_video(url):
 try:
#creating pafy object of the video 
    video = pafy.new(url)    
    # getting best stream 
    stream = video.streams 
    for i in stream: 
        print(i) 
    i = len(stream)
    best = video.streams[i-1]

    # loading video from net
    clip = VideoFileClip(best.url) 

    save_video(clip)

 except:
    print("Video Not Found") 
 
root = Tk()
#tk is a toolkit..it is set of tool,especially one kept in a bag or box  and used to purticular purpose
root.geometry("500x300")
user=" "

def print_url(): 
    global user
    user=enter.get()  
    print(user)
    find_video(user)

enter=Entry(root,font=('calibre',10))
enter.pack(side=TOP,pady=30)
enter.insert(0,"paste the link")
button= Button(root,text="download",font=("cabrie"),command=print_url)
button.pack(side=TOP)
root.mainloop()





