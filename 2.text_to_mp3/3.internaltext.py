from gtts import gTTS

def text_to_mp3(text, output_file="output.mp3", language="en"):
    """
    Converts the given text to an MP3 file.

    Args:
        text (str): The text to convert to speech.
        output_file (str): The name of the output MP3 file.
        language (str): Language for text-to-speech. Default is 'en' (English).

    Returns:
        None
    """
    try:
        # Generate speech
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save the audio file
        tts.save(output_file)
        print(f"MP3 file saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_text = "Hello! Welcome to the world of Python programming."
    text_to_mp3(input_text, output_file="welcome.mp3")

# Example usage
# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         input_text = file.read()
#     text_to_mp3(input_text, output_file="output.mp3")


