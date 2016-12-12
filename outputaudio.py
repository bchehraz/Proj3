import scipy, numpy, os, sys, pyaudio, struct, wave
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


"""def play_tone(stream, frequency, length=2, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())"""
def get_freq(note):
	frequency = None
	if int(note) < 12:
		if note == 0: # C
			frequency = 16.351
		if note == 1: # C#/Db
			frequency = 17.324
		if note == 2: # D
			frequency = 18.354
		if note == 3: # D#/Eb
			frequency = 19.445
		if note == 4: # E
			frequency = 20.601
		if note == 5: # F
			frequency = 21.827
		if note == 6: # F#/Gb
			frequency = 23.124
		if note == 7: # G
			frequency = 24.499
		if note == 8: # G#/Ab
			frequency = 25.956
		if note == 9: # A
			frequency = 27.5
		if note == 10: # A#/Bb
			frequency = 29.135
		if note == 11: # B
			frequency = 30.868
		return frequency
	else:
		print("Error! Invalid value for note!  Note must be an integer between 1 & 12")
			
def play_tone(stream, note, octave, length=2, rate=44100):
	chunks = []
	frequency = get_freq(note)
	chunks.append(sine(frequency*(2^octave), length, rate))

	chunk = numpy.concatenate(chunks) * 0.25

	stream.write(chunk.astype(numpy.float32).tostring())

# if __name__ == '__main__':
# 	p = pyaudio.PyAudio()
# 	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
	
