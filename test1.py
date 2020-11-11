#Import everything needed  
from moviepy.editor import *
import easygui
import pafy 
import youtube_dl

# url of the video 
url = " "

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

def save_video(clip):
#saving the clip 
 save_path=easygui.filesavebox()
 clip.write_videofile(save_path) 

 
