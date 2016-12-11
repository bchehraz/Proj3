import scipy
from scipy.io import wavfile
import numpy
import pyaudio
#import wave
import os, sys
import SWHear
import struct

class Streamobj():

	CHUNK = 4096
	rate = None
	data = None
	s1 = 666
	stream1 = 666
	
	def __init__(self):
		'''
		filepath = input('Input file name: ')
		self.wavfile = wave.open(filepath, 'rb') <<ADD IN LATER
		'''
		self.rate, self.data = wavfile.read("09 Darling, Mommy is Dead.wav")
		self.s1 = pyaudio.PyAudio()
		self.stream1 = self.s1.open(format=self.s1.get_format_from_width(self.wavfile.getsampwidth()),
						channels=self.wavfile.getnchannels(),
						rate=self.wavfile.getframerate(),
						output=True)
	#Play
	def play(self):
		wavdata = self.wavfile.readframes(self.CHUNK)
		while len(wavdata) > 0:
			self.stream1.write(wavdata)
			data = struct.unpack("<h", wavdata)
			freq = SWHear.getFFT(data, self.wavfile.getframerate())
			wavdata = self.wavfile.readframes(self.CHUNK)
		#Terminate
		self.stream1.stop_stream()
		self.stream1.close()
		
ifile = Streamobj()
ifile.play()
