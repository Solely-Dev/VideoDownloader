#import everything needed  
from tkinter import *
import tkinter.font as font
import easygui
from pytube import YouTube
import pathlib

#saving the clip
def save_video(tag,yt_obj):
  save_path=easygui.filesavebox()
  if save_path != None:
   select_path = pathlib.Path(save_path)
   file_name=pathlib.Path(save_path).name
   location_stored=select_path.parent
   yt_obj.streams.get_by_itag(tag).download(output_path=location_stored,filename=file_name)
  else:
    easygui.msgbox("process terminated...", "Error!")
    print("process terminated...")

#video in 360px
def _360px(yt_obj):
  itag=18
  save_video(itag,yt_obj)

def _720px(yt_obj):
  itag=22
  save_video(itag,yt_obj)  

def find_video(url):
 try:
  
 #creating Youtube object of the video 
   yt_obj = YouTube(url)    
   _360px(yt_obj)

 except:
  easygui.msgbox("Video Not Found", "Warning!")
  print("Video Not Found") 
 
root = Tk()
#tk is a toolkit..it is set of tool,especially one kept in a bag or box  and used to purticular purpose
root.geometry("600x350")
user=" "
def quit():
    root.destroy()
def print_url(): 
    global user
    user=enter.get() 
    print(user)
    quit() 
    find_video(user)

root.resizable(0,0)

root.configure(bg="white")

myFont= font.Font(family="helvetica",size=10,weight="bold")

root.title("downloader")


def sri():
    lowest=360
    print(lowest)

def devi():
    low=480
    print(low)

def sampath():
    high=720
    print(high)

def reshma():
    highest=1080
    print(highest)    







enter=Entry(root,font=('helvetica',15),bg="white",fg="black",borderwidth=5)
enter.pack(side=TOP,pady=70)
enter.insert(0,"paste the link")

Label(root, text = "    Enter URL:",bg="white",font=('helvetica 15 bold')).place(x = 25,y = 73)
Label(root, text = "    Quality:",bg="white",font=('helvetica 15 bold')).place(x = 39,y = 200)

#w=Label(root,text="Enter url",justify=RIGHT,padx=10)
#w.pack(side=LEFT)

button= Button(root,text="Download",font=("cabrie"),bg="green",fg="white",command=print_url,borderwidth=5)
button['font']=myFont
button.pack(side=BOTTOM,pady=30)

but1=Button(root,text="360",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=sri,activebackground="#4444ff",borderwidth=5)
but1['font']=myFont
but1.pack(side=RIGHT,padx=43)
 

but2=Button(root,text="480",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=devi,activebackground="#4444ff",borderwidth=5)
but2['font']=myFont
but2.pack(side=RIGHT,padx=18)

but3=Button(root,text="720",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=sampath,activebackground="#4444ff",borderwidth=5)
but3['font']=myFont
but3.pack(side=RIGHT,padx=18)

but4=Button(root,text="1080",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=reshma,activebackground="#4444ff",borderwidth=5)
but4['font']=myFont
but4.pack(side=RIGHT,padx=20)






root.mainloop()

