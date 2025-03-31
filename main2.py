import whisper

model = whisper.load_model("base")
result = model.transcribe("en_samples\\audio.wav")
print(result["text"])