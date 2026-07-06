import librosa
import matplotlib.pyplot as plt

def plot_waveform(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    fig, ax = plt.subplots(figsize=(10,3))

    ax.plot(y)

    ax.set_title("Audio Waveform")

    ax.set_xlabel("Samples")

    ax.set_ylabel("Amplitude")

    return fig