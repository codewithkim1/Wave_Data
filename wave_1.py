import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

def create_pulse_signal(duration, start_frequency, end_frequency):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    frequencies = np.linspace(start_frequency, end_frequency, len(t))
    signal = 0.5 * np.sin(2 * np.pi * frequencies * t)
    return signal

def create_continuous_sound(pulse_signal, delay):
    continuous_signal = np.array([])
    for i in range(len(pulse_signal)):
        continuous_signal = np.append(continuous_signal, pulse_signal[i])
        continuous_signal = np.append(continuous_signal, np.zeros(int(delay * 44100)))
    return continuous_signal

pulse_signal = create_pulse_signal(0.001, 16000, 22000)
continuous_signal = create_continuous_sound(pulse_signal, 0.05)

def export_data(signal, file_name):
    signal = signal / np.max(np.abs(signal))
    signal = signal.astype(np.float32)
    with wave.open(file_name, 'w') as wav_file:
        n_samples = len(signal)
        sample_width = 4
        sample_rate = 44100
        n_channels = 1
        wav_file.setparams((n_channels, sample_width, sample_rate, n_samples, "NONE", "not compressed"))
        for sample in signal:
            wav_file.writeframes(struct.pack('f', sample))

export_data(continuous_signal, "continuous_sound.wav")
