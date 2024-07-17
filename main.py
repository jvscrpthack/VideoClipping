from moviepy.editor import VideoFileClip
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()
full_video = askopenfilename()
print(full_video)

PartDuration = int(input('По сколько секунд видео:'))
FullDuration = VideoFileClip(full_video).duration
StartTime = 0
i = 1 

while True:
    EndPos = StartTime + PartDuration

    if EndPos > FullDuration:
        EndPos = FullDuration

    clip = VideoFileClip(full_video).subclip(StartTime, EndPos)

    part_name = "part_"+str(i)+".mp4"
    clip.to_videofile(part_name, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    print("clip ",i,"done")
    i += 1
    
    StartTime = EndPos
    
    if StartTime >= FullDuration:
        break