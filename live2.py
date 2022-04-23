import numpy as np
import soundcard as sc
import time
from scipy.fftpack import fft
import soundfile as sf
import sys
beep, samplerate = sf.read('kilobeep.wav') 

c = 320

# soundcard is a wrapper for pulseaudio and i am using some of their default code

default_speaker = sc.default_speaker()
default_mic = sc.default_microphone()

print(default_speaker)
print(default_mic)
spb = 44100 # samples to pull from soundcard at a time

def energy(freq,data,rate): # and you would not believe how long it took to nail this down
    rate = 44100
    fft_out = fft(data)[0:len(data)//2]
    scaling_factor = len(data) / rate
    return (np.abs(fft_out[int(freq*scaling_factor)]))


with default_mic.recorder(samplerate=44100,blocksize=44100,channels=[0]) as mic, default_speaker.player(samplerate=44100) as sp:
    # before main loop
    rawdata = mic.record(numframes=spb) # this happens here for optimisation
    while True:
        # main loop - runs until program ends
        buffer = buffer + rawdata
        rawdata = mic.record(numframes=spb)
        

        

