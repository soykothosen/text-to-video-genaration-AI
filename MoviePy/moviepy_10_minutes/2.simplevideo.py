from moviepy import TextClip

# Create a text clip with the text "Hello MoviePy"
text_clip = TextClip("Hello, MoviePy!", fontsize=70, color='white', size=(640, 480), bg_color='black')

# Set the duration of the clip
text_clip = text_clip.set_duration(5)  # 5 seconds duration

# Export the video
text_clip.write_videofile("output_video.mp4", fps=24)
