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

if __name__ == '__main__':
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
	
	# E Standard Tuning
	play_tone(stream, 329.63)  #E
	play_tone(stream, 440.00) #A
	play_tone(stream, 587.33) #D 
	play_tone(stream, 783.99) #G 
	play_tone(stream, 987.77) #B 
	play_tone(stream, 1318.51) #E
	
	"""not sure how to implement these tunings, but here they are
	#Drop D
	play_tone(stream, 293.66)  #D
	play_tone(stream, 440.00) #A
	play_tone(stream, 587.33) #D 
	play_tone(stream, 783.99) #G 
	play_tone(stream, 987.77) #B 
	play_tone(stream, 1318.51) #E
	
	#Half Step Down
	play_tone(stream, 311.13) #Eb
	play_tone(stream, 415.30) #Ab
	play_tone(stream, 554.37) #Db
	play_tone(stream, 739.99) #Gb
	play_tone(stream, 932.33) #Bb
	play_tone(stream, 1244.51) #Eb
	
	#Drop Db
	play_tone(stream, 277.18) #Db
	play_tone(stream, 415.30) #Ab
	play_tone(stream, 554.37) #Db
	play_tone(stream, 739.99) #Gb
	play_tone(stream, 932.33) #Bb
	play_tone(stream, 1244.51) #Eb
	
	#D Standard
	play_tone(stream, 293.66) #D
	play_tone(stream, 392.00) #G
	play_tone(stream, 523.25) #C
	play_tone(stream, 698.46) #F 
	play_tone(stream, 880.00) #A 
	play_tone(stream, 1174.66) #D
	
	#Drop C
	play_tone(stream, 261.63)  #C
	play_tone(stream, 392.00) #G
	play_tone(stream, 523.25) #C
	play_tone(stream, 698.46) #F 
	play_tone(stream, 880.00) #A 
	play_tone(stream, 1174.66) #D
	
	#C Standard
	play_tone(stream, 261.63) #C
	play_tone(stream, 349.23) #F
	play_tone(stream, 493.88) #B
	play_tone(stream, 659.25) #E 
	play_tone(stream, 783.99) #G 
	play_tone(stream, 1046.50) #C

	"""
