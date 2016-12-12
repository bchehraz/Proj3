import scipy, numpy, os, sys, pyaudio, struct, wave
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

def get_note(freq):#Returns the musical note played
	n = round((math.log(freq/220)/math.log(pow(2, 1/12))),1) #Get Semitones away from A3(220Hz)
	while n >= 12:#Get n in terms of 0-11 semitones
		n -= 12
	while n < 0
		n += 12
	return n

def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;

def recordAudio():
	
	audio = pyaudio.PyAudio()
	
	stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	

	print ("* Recording audio...")
		
	frames = []
	
	while True:
		data = stream.read(CHUNK)
		print (Pitch(data))
		frames.append(data)
		
print(get_note(27.5))