from kivy.core.audio import SoundLoader

def getDuration(filename):
	sound = SoundLoader.load(filename)
	if sound:
		return sound.length
	else
		print ("-- get duration failed - file not found")
		return -1
