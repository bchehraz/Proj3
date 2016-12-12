'''
Course: CST 205 
Date: December 11, 2016 
Authors: Babak Chehraz, Shaikh Sultani, Quentin Minor 
Abstract: The file will output the tones for the tuner to work when wanting to tune by ear. 
'''

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
	if note == 'C' or note == 0: # C
		return 16.351
	elif note == 'C#' or note == 'Db' or note == 1: # C#/Db
		return 17.324
	elif note == 'D' or note == 2: # D
		return 18.354
	elif note == 'D#' or note == 'Eb' or note == 3: # D#/Eb
		return 19.445
	elif note == 'E' or note == 4: # E
		return 20.601
	elif note == 'F' or note == 5: # F
		return 21.827
	elif note == 'F#' or note == 'Gb' or note == 6: # F#/Gb
		return 23.124
	elif note == 'G' or note == 7: # G
		return 24.499
	elif note == 'G#' or note == 'Ab' or note == 8: # G#/Ab
		return 25.956
	elif note == 'A' or note == 9: # A
		return 27.5
	elif note == 'A#' or note == 10: # A#/Bb
		return 29.135
	elif note == 'B' or note == 11: # B
		return 30.868
	else:
		return "Nothing found"
			
def play_tone(stream, note, octave, length=2, rate=44100):
	chunks = []
	frequency = get_freq(note)
	chunks.append(sine(frequency*(2^octave), length, rate))

	chunk = numpy.concatenate(chunks) * 0.25

	stream.write(chunk.astype(numpy.float32).tostring())

# if __name__ == '__main__':
# 	p = pyaudio.PyAudio()
# 	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)