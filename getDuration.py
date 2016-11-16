from kivy.core.audio import SoundLoader

def getDuration(filename):
	sound = SoundLoader.load(filename)
	if sound:
		return sound.length;