import librosa
import soundfile as sf
import os



def preprocess_audio(input_path, output_path="outputs/processed_audio.wav"):
    """
    Load, normalize and save the audio.
    """

    os.makedirs("outputs", exist_ok=True)

    # Load audio
    y, sr = librosa.load(input_path, sr=16000)

    # Normalize audio
    y = librosa.util.normalize(y)

    # Save processed audio
    sf.write(output_path, y, sr)

    return output_path