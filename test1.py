#Import everything needed  
from tkinter import *
import easygui
from pytube import YouTube

#saving the clip
def save_video(tag,yt_obj):
  title=yt_obj.title
  save_path=easygui.filesavebox(default=title)
  yt_obj.streams.get_by_itag(tag).download(save_path)

#video in 360px
def _360px(yt_obj):
  itag=18
  save_video(itag,yt_obj)

def _720px(yt_obj):
  itag=22
  save_video(itag,yt_obj)  

try:
 #main function   
 def find_video(url):
#creating Youtube object of the video 
  yt_obj = YouTube(url)    
  _720px(yt_obj)

except:
 print("Video Not Found") 
 
root = Tk()
#tk is a toolkit..it is set of tool,especially one kept in a bag or box  and used to purticular purpose
root.geometry("500x300")
user=" "
def quit():
    root.destroy()
def print_url(): 
    global user
    user=enter.get() 
    quit() 
    find_video(user)
enter=Entry(root,font=('calibre',10))
enter.pack(side=TOP,pady=30)
enter.insert(0,"paste the link")
button= Button(root,text="download",font=("cabrie"),command=print_url)
button.pack(side=TOP)
root.mainloop()





