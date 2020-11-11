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

# saving the clip 
 clip.write_videofile("video.mp4")

except:
    print("Video Not Found")

 
