import soundcard as sc # pip install soundcard
import numpy
import soundfile as sf
import time

data, samplerate = sf.read('beep2.wav') 
#dprint (len(data),samplerate)

default_speaker = sc.default_speaker()
default_mic = sc.default_microphone()

# data = default_mic.record(samplerate=48000, numframes=48000)

# default_speaker.play(data/numpy.max(data), samplerate)

with default_speaker.player(samplerate=samplerate,blocksize=samplerate) as sp:
    # we set blocksize = samplerate so it waits after sending the first block
    for x in range (0,60):
        tstart = time.time()
        sp.play(data)
        tstop = time.time()
        print (tstop - tstart)
        #time.sleep(1.01)
        #print ("finished") 


