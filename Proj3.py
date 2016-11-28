import scipy
import pyaudio
import wave
import os, sys
import SWHear

class Streamobj():

	CHUNK = 4096
	wavefile = 666
	maxPCM=0
	maxFFT=0
	s1 = 666
	stream1 = 666
	ffreq = SWHear.SWHear()
	ffreq.stream_start()
	def __init__(self):
		'''
		filepath = input('Input file name: ')
		self.wavfile = wave.open(filepath, 'rb') <<ADD IN LATER
		'''
		self.wavfile = wave.open("09 Darling, Mommy is Dead.wav", 'rb')
		self.s1 = pyaudio.PyAudio()
		self.stream1 = self.s1.open(format=self.s1.get_format_from_width(self.wavfile.getsampwidth()),
						channels=self.wavfile.getnchannels(),
						rate=self.wavfile.getframerate(),
						output=True)
	#Play
	def play(self):
		data = self.wavfile.readframes(self.CHUNK)
		while len(data) > 0:
			self.stream1.write(data)
			data = self.wavfile.readframes(self.CHUNK)
		#Terminate
		self.stream1.stop_stream()
		self.stream1.close()
		self.ffreq.close()
	def update(self):
			if not self.ffreq.data is None and not self.ffreq.fft is None:
				pcmMax=np.max(np.abs(self.ffreq.data))
				if pcmMax>self.maxPCM:
					self.maxPCM=pcmMax
					#self.grPCM.plotItem.setRange(yRange=[-pcmMax,pcmMax])
				if np.max(self.ear.fft)>self.maxFFT:
					self.maxFFT=np.max(np.abs(self.ffreq.fft))
					#self.grFFT.plotItem.setRange(yRange=[0,self.maxFFT])
				self.pbLevel.setValue(1000*pcmMax/self.maxPCM)
				#pen=pyqtgraph.mkPen(color='b')
				#self.grPCM.plot(self.ear.datax,self.ear.data,
								#pen=pen,clear=True)
				#pen=pyqtgraph.mkPen(color='r')
				#self.grFFT.plot(self.ear.fftx[:500],self.ear.fft[:500],
								#pen=pen,clear=True)
			QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat"""

ifile = Streamobj()
#ifile.open()
ifile.play()
