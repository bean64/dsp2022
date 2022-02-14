import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import soundcard as sc # pip install soundcard
import soundfile as sf
import time
beep, samplerate = sf.read('beep.wav') 

def detect(freq,data,rate):
    fft_out = fft(data)[0:len(data)//2]
    scaling_factor = len(data) / rate
    return (np.abs(fft_out[int(freq*scaling_factor)]))

def fftime(freq,data,rate):
    winsize = 200
    prev_val = False
    for startpoint in range (0,len(data)-winsize):
        endpoint = startpoint + winsize
        chopped_data = data[startpoint:endpoint]
        val = detect(freq,chopped_data,rate)
        if val > 10**10 and not prev_val:
            #print(startpoint,endpoint,val)
            return ((startpoint+winsize/2)/rate)
            
beep, samplerate = sf.read('beep2.wav') 
#dprint (len(data),samplerate)

default_speaker = sc.default_speaker()
default_mic = sc.default_microphone()

# data = default_mic.record(samplerate=48000, numframes=48000)

# default_speaker.play(data/numpy.max(data), samplerate)

with default_speaker.player(samplerate=samplerate,blocksize=samplerate) as sp:
    # we set blocksize = samplerate so it waits after sending the first block
    for x in range (0,60):
        sp.play(beep)
        rec = default_mic.record(samplerate=48000,numframes=1024)


