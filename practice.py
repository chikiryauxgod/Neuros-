import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

def gen_signal(max):
    seq = np.arange(0, max)
    bits = ''.join(f"{i:08b}" for i in seq)  
    signal = np.array([int(bit) for bit in bits])  
    return signal

def print_signal(signal, name):
    plt.figure(figsize=(12, 6))
    plt.plot(signal, drawstyle="steps-pre", label=name)
    plt.title(name)
    plt.xlabel("Values")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()
    plt.show()

def filter_signal(signal):
    b = [1/3, 1/3, 1/3, 1/3]
    a = 1
    filtered_signal = lfilter(b, a, signal)  
    return filtered_signal

def noise_signal(signal):
    lvl = 0.1
    noise = np.random.normal(loc = 0, scale = lvl * np.std(signal), size=len(signal))
    noisy_signal = signal + noise
    return noisy_signal

def normalize_signal(signal):
    print("Hello World!")
    

max = 256
signal = gen_signal(max)
print_signal(signal, "Generated Signal")

filtered_signal = filter_signal(signal)
print_signal(filtered_signal, "Filtered Signal")

noisy_signal = noise_signal(signal)
print_signal(noisy_signal, "Noisy Signal")

