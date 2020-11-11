#Import everything needed  
from moviepy.editor import *
import easygui

#loading a video 
video_path = easygui.fileopenbox()
clip = VideoFileClip(video_path) 

#saving the clip 
clip.write_videofile("sample.mp4") 
 
