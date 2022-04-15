import numpy as np
import soundcard as sc
import time
# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()


print(default_speaker)
print(default_mic)
start = time.time()
# record and play back one second of audio:
with default_mic.recorder(samplerate=44100,blocksize=44100) as mic, default_speaker.player(samplerate=44100) as sp:
    buffer = mic.record(numframes=4410)
    for _ in range(100):
        data = mic.record(numframes=4410)
        #time.sleep(0.1)
        print (time.time()-start)
        start = time.time()
        buffer = np.concatenate((buffer,data),axis=0)
        print (len(buffer))
    while True:        
        sp.play(buffer)
        
