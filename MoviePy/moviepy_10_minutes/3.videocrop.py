from moviepy import VideoFileClip

# Loading video (ensure video file is in the same directory or provide the full path)
clip = VideoFileClip("video1.mp4") 

# Clip the video to the first 10 seconds
clip = clip.subclipped(0, 10) 

# Rotate video by 180 degrees
clip = clip.rotated(180) 

# Reduce the audio volume by 50% (volume x 0.5)
#clip = clip.audio.volumex(0.5) 

# Preview the video (for non-Jupyter environments)
clip.preview()  # Use this instead of ipython_display()

# Optionally, write the edited clip to a new file
clip.write_videofile("edited_video.mp4", fps=24)
