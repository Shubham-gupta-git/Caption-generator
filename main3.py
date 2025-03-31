# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3
import time

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to process audio from a microphone
def process_microphone():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = r.listen(source)
        return audio

# Function to process audio from a file
def process_audio_file(file_path):
    with sr.AudioFile(file_path) as source:
        print("Processing audio file...")
        duration = source.DURATION  # Get the duration of the audio file
        start_time = time.time()
        audio = r.record(source)
        elapsed_time = time.time() - start_time
        remaining_time = max(0, duration - elapsed_time)
        print(f"Estimated remaining time: {remaining_time:.2f} seconds")
        return audio

# Main loop
while True:
    try:
        # Ask the user for the input source
        choice = input("Enter 'mic' to use the microphone or 'file' to use an audio file: ").strip().lower()

        if choice == 'mic':
            audio = process_microphone()
        elif choice == 'file':
            file_path = input("Enter the path to the audio file: ").strip()
            audio = process_audio_file(file_path)
        else:
            print("Invalid choice. Please enter 'mic' or 'file'.")
            continue

        # Recognize the audio
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()

        print("Did you say:", MyText)
        SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")
