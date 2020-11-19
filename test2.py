#import everything needed  
from tkinter import *
import tkinter.font as font
import easygui
from pytube import YouTube
import pathlib




#saving the clip
def save_video(Video):
  save_path=easygui.filesavebox()
  easygui.msgbox(msg=" Video Downloading...",title="downloading")
  print("downloading")
  if save_path != None:
   select_path = pathlib.Path(save_path)
   file_name=pathlib.Path(save_path).name
   location_stored=select_path.parent
   Video.download(output_path=location_stored,filename=file_name)
   

  else:
    easygui.msgbox("process terminated...", "Error!")
    print("process terminated...")

Video=" "
def find_video(url,ttag):
 try:
 #creating Youtube object of the video 
   global Video 
   yt_obj = YouTube(url) 
   Video= yt_obj.streams.get_by_itag(ttag)
   quit()
   if Video != None:
    save_video(Video)
    easygui.msgbox(" Video Downloadeing successfully")
    print("downloaded")
   
   else :
    easygui.msgbox(msg="Video is not Available in that Quality :",title="Warning")  
 except:
  easygui.msgbox("Video Not Found", "Warning!")
  print("Video Not Found") 
 
def _1080px():
  print_url(37)

def _720px():
  print_url(22)

def _480px():
  print_url(83)

def _360px():
  print_url(18)

root = Tk()
#tk is a toolkit..it is set of tool,especially one kept in a bag or box  and used to purticular purpose
root.geometry("600x350")
user=" "
tag=" "
def quit():
    root.destroy()
def print_url(itag): 
    global user
    global tag
    tag=itag
    user=enter.get() 


root.resizable(0,0)
root.configure(bg="white")
myFont= font.Font(family="helvetica",size=10,weight="bold")
root.title("downloader")

enter=Entry(root,font=('helvetica',13),bg="white",fg="black",borderwidth=5,width=30)
enter.pack(side=TOP,pady=70)
enter.insert(0,"paste the link")

Label(root, text = "    Enter URL:",bg="white",font=('helvetica 15 bold')).place(x = 5,y = 73)
Label(root, text = "    Quality:",bg="white",font=('helvetica 15 bold')).place(x = 20,y = 200)


def Download():
    user=enter.get() 
    if ':' in user: 
     https,link=user.strip().split(":")
     if ('https'== https) and (tag!=" "):
         
         find_video(user,tag)
         
     else:
         if 'https'!=https:
          easygui.msgbox(msg="url seems to be wrong",title="warning")
         elif tag==" ":
          easygui.msgbox(msg="no stream selected",title="warning") 
    else:
     easygui.msgbox(msg="no url provided",title="warning")



button= Button(root,text="Download",bg="green",fg="white",command=Download,borderwidth=5)
button['font']=myFont
button.pack(side=BOTTOM,pady=30)




but1=Button(root,text="360",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=_360px,activebackground="#4444ff",borderwidth=5)
but1['font']=myFont
but1.pack(side=RIGHT,padx=43)
 

but2=Button(root,text="480",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=_480px,activebackground="#4444ff",borderwidth=5)
but2['font']=myFont
but2.pack(side=RIGHT,padx=18)

but3=Button(root,text="720",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command=_720px,activebackground="#4444ff",borderwidth=5)
but3['font']=myFont
but3.pack(side=RIGHT,padx=22)

but4=Button(root,text="1080",font=("calibre",10),padx=10,fg="white",bg="#ff5733",command= _1080px,activebackground="#4444ff",borderwidth=5)
but4['font']=myFont
but4.pack(side=RIGHT,padx=35)


  

root.mainloop()

