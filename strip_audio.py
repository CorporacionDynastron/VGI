from moviepy import VideoFileClip
import os

videos = [
    r"C:\Dynastron_Code\VGI\05-formacion\VIDEO 2.mp4", 
    r"C:\Dynastron_Code\VGI\05-formacion\VIDEO 5.mp4"
]

for v in videos:
    if os.path.exists(v):
        clip = VideoFileClip(v)
        clip_without_audio = clip.without_audio()
        tmp = v.replace(".mp4", "_noaudio.mp4")
        clip_without_audio.write_videofile(tmp, codec="libx264", logger=None)
        clip.close()
        clip_without_audio.close()
        os.remove(v)
        os.rename(tmp, v)
        print(f"Removed audio from {v}")
    else:
        print(f"Could not find {v}")

