import librosa
import numpy as np

def extract_audio_features(audio_path):
    """
    Extract audio features using Librosa.
    """

    y, sr = librosa.load(audio_path, sr=None)

    duration = librosa.get_duration(y=y, sr=sr)

    # RMS Energy
    rms = librosa.feature.rms(y=y)[0]
    avg_rms = float(np.mean(rms))

    # Silence Detection
    intervals = librosa.effects.split(
        y,
        top_db=30
    )

    speech_duration = sum(
        (end - start) / sr
        for start, end in intervals
    )

    pause_duration = duration - speech_duration

    pause_ratio = (
        pause_duration / duration
        if duration > 0 else 0
    )

    # Tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    tempo = np.asarray(tempo).squeeze().item()
    # Estimated Speaking Rate
    speaking_rate = len(intervals) / duration if duration > 0 else 0

    return {
        "Duration": round(duration, 2),
        "Average RMS": round(avg_rms, 4),
        "Pause Ratio": round(pause_ratio, 2),
        "Tempo": round(tempo, 2),
        "Speaking Rate": round(speaking_rate, 2)
    }