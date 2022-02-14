import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('vlaaieep.wav')

fft_out = fft(data)[0:len(data)//2]
scaling_factor = len(data) / rate

xaxis = range(0,len(fft_out))
xaxis = [i /  scaling_factor for i in xaxis]

def scaledfft(freq):
    #pos = int(freq * scaling_factor)
    #val = fft_out[pos]
    #absed = np.abs(val)
    #return (absed)
    return (np.abs(fft_out[int(freq*scaling_factor)]))

#plt.plot(xaxis, np.abs(fft_out))
#plt.show()

def detect(freq,data,rate):
    fft_out = fft(data)[0:len(data)//2]
    scaling_factor = len(data) / rate
    return (np.abs(fft_out[int(freq*scaling_factor)]))

'''
def fftime(freq,data,rate):
    winsize = 200
    prev_val = False
    startpoint = 0
    #while startpoint < (len(data)-winsize):
    while startpoint < (70 * 44100):        
    #for startpoint in range (0,len(data)-winsize):
        startpoint = startpoint + 44
        endpoint = startpoint + winsize
        chopped_data = data[startpoint:endpoint]
        val = detect(freq,chopped_data,rate)
        noisiness = np.average(np.absolute(chopped_data))
        #print (startpoint/rate,val,noisiness,val/noisiness)
        #print (noisiness)
        denoise = val / noisiness
        if denoise > 100:
            print(startpoint,endpoint,startpoint/rate)
            startpoint = int(startpoint + (0.8*rate))
            #print (startpoint)
            #return ((startpoint+winsize/2)/rate)
'''
def fftime(freq,temp,rate):
    winsize = 200
    prev_val = False
    startpoint = 0
    while startpoint < (len(data)-winsize):
    #while startpoint < (70 * 44100):        
    #for startpoint in range (0,len(data)-winsize):
        startpoint = startpoint + 441
        endpoint = startpoint + winsize
        chopped_data = data[startpoint:endpoint]
        val = detect(freq,chopped_data,rate)
        noisiness = np.average(np.absolute(chopped_data))
        #print (startpoint/rate,val,noisiness,val/noisiness)
        denoise = val / noisiness
        if denoise > 100:
            print(startpoint,endpoint,startpoint/rate)
            startpoint = int(startpoint + (0.8*rate))
            #print (startpoint)
            #return ((startpoint+winsize/2)/rate)
print(fftime(1000,data,rate))
