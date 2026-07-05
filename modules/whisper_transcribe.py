import whisper
from modules.audio_preprocess import preprocess_audio

model = whisper.load_model("base")

def transcribe(file_path):
    audio_file = preprocess_audio(file_path)
    result = model.transcribe(audio_file)
    return result["text"]
