import moviepy.editor

from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import os

def text_to_video(text, output_file="output_video.mp4", video_duration=10, font="Arial", font_size=50, text_color="white", bg_color="black", fps=24):
    """
    Generates a video from text.

    Args:
        text (str): The text to display in the video.
        output_file (str): The name of the output video file.
        video_duration (int): Duration of the video in seconds.
        font (str): Font to use for the text.
        font_size (int): Font size of the text.
        text_color (str): Color of the text.
        bg_color (str): Background color of the video.
        fps (int): Frames per second for the video.

    Returns:
        None
    """
    try:
        # Create a text clip
        text_clip = TextClip(
            text,
            font=font,
            fontsize=font_size,
            color=text_color,
            size=(1280, 720),  # Video resolution (width x height)
            method="caption"
        ).set_duration(video_duration)

        # Create a background color clip
        bg_clip = ColorClip(
            size=(1280, 720),  # Resolution
            color=bg_color  # Background color
        ).set_duration(video_duration)

        # Overlay text on the background
        video = CompositeVideoClip([bg_clip, text_clip.set_position("center")])

        # Write the video file
        video.write_videofile(output_file, fps=fps)
        print(f"Video saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_text = "Welcome to Python Video Generation!"
    text_to_video(input_text, output_file="text_video.mp4", video_duration=5)
