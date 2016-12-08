import scipy, numpy, os, sys, pyaudio, struct, wave
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency, length=2, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())

if __name__ == '__main__':
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
	
	# E Standard Tuning
	play_tone(stream, 82.41)  #E
	play_tone(stream, 110.00) #A
	play_tone(stream, 146.83) #D 
	play_tone(stream, 196.00) #G 
	play_tone(stream, 246.94) #B 
	play_tone(stream, 329.63) #E
	
	
	

