import scipy
import pyaudio
import wave
import os, sys
import SWHear

CHUNK = 1024

wavfile = wave.open("09 Darling, Mommy is Dead.wav", 'rb')
s1 = pyaudio.PyAudio()
stream1 = s1.open(format=s1.get_format_from_width(wavfile.getsampwidth()),
                channels=wavfile.getnchannels(),
                rate=wavfile.getframerate(),
                output=True)
data = wavfile.readframes(CHUNK)
#Play
while len(data) > 0:
    stream1.write(data)
    data = wavfile.readframes(CHUNK)
	
#Terminate
stream.stop_stream()
stream.close()

