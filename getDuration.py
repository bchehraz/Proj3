'''
Course: CST 205 
Date: December 11, 2016 
Authors: Babak Chehraz, Shaikh Sultani, Quentin Minor 
Abstract: 
'''

from kivy.core.audio import SoundLoader

def getDuration(filename):
	sound = SoundLoader.load(filename)
	if sound:
		return sound.length
	else
		print ("-- get duration failed - file not found")
		return -1
