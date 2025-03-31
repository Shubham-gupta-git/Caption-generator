from moviepy import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

# Step 1: Extract audio from video
video = VideoFileClip("hindi_sample.mp4")
audio_path = "audio.wav"
video.audio.write_audiofile(audio_path)

# Step 2: Convert audio to text using SpeechRecognition
recognizer = sr.Recognizer()
audio = AudioSegment.from_file(audio_path, format="wav")
audio.export("processed_audio.wav", format="wav")  # Ensure correct format

with sr.AudioFile("processed_audio.wav") as source:
    audio_data = recognizer.record(source)
    captions = recognizer.recognize_google(audio_data)

# Step 3: Output the captions
print("Generated Captions:")
print(captions)
