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
    #buffer = mic.record(numframes=spb)
    data = mic.record(numframes=spb)
    first = True
   #ecount = 0
    print ("Waiting for sync...")
    scanstart= 0
    scanend = spb - 32
    while True:
        starttime = time.perf_counter()
        #for startpoint in range (0,spb-32):
        for startpoint in range (scanstart,scanend):
            #count = count + 1
            endpoint = startpoint + 32
            sliced_data = data[startpoint:endpoint]
            signal = energy(1000,sliced_data,44100)[0]
            #noisiness = np.average(np.absolute(sliced_data))
            #ssnr = signal / noisiness
            if (signal > 0.01): # signal > 0.01 or ssnr > 
                #lspings = lspings + 
                #print (startpoint,endpoint, signal)
                if first:
                    fsp = startpoint
                    scanstart = fsp - 1024 # fixme!
                    scanend = fsp + 1024
                    print ("Sync get!", fsp,"samples!")
                    print ("Resetting scan area to",scanstart, "to", scanend)
                    first = False
                else:
                    delta = startpoint - fsp
                    #oldpos = position
                    position = delta * (c/44100)
                    #change = (position - oldposition)
                    if position > 10:
                        #ecount = ecount + 1
                        print (str(round(position,2)).rjust(7),str(delta).rjust(7))
                    elif position < 0:
                        #ecount = ecount + 1
                        print (str(round(position,2)).rjust(7),str(delta).rjust(7))
                    else:
                        #ecount = 0
                        blok = " " * int(position*10) + "X"
                        print (str(round(position,2)).rjust(7),str(delta).rjust(7),blok) #str(round(time.time(),2)).rjust(6)
                if startpoint == 0: # this is very scuffed, yes! the alternative caused a memory leak. Too bad!
                    print ("Sync ERROR! Please restart")
                    print ("Check audio levels?")
                    print ("Mic gain may be too high or background too noisy")
                    sys.exit()                
                break
            
        
        data = mic.record(numframes=spb)

        
        

