import vosk
import wave
import json

# Set the model path
model_path = "vosk-model-small-hi-0.22"
# Initialize the model with model-path
model = vosk.Model(model_path)

# Specify the path to the audio file
audio_file_path = "output_audio.wav"

# Open the audio file
with wave.open(audio_file_path, "rb") as wf:
    # Check if the audio file has the correct format
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        raise ValueError("Audio file must be WAV format mono PCM with a sample rate of 16000 Hz.")
    
    # Create a recognizer
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    
    # Specify the path for the output text file
    output_file_path = "p5.txt"
    
    # Open a text file in write mode using a 'with' block
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        print("Processing audio file...")
        
        # Read audio data in chunks and recognize speech
        while True:
            data = wf.readframes(4096)  # Read in chunks of 4096 frames
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):  # Accept waveform of input audio
                # Parse the JSON result and get the recognized text
                result = json.loads(rec.Result())
                recognized_text = result['text']
                
                # Write recognized text to the file
                output_file.write(recognized_text + "\n")
                print(recognized_text)
