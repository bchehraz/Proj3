'''
Course: CST 205 
Date: December 11, 2016 
Authors: Babak Chehraz, Shaikh Sultani, Quentin Minor 
Abstract: This is the GUI. This file will take all the sound files that were made prior to add the sound listening, frequencies,
output, and tones to the GUI. It also formats the gui for how we want it too look. 
'''
import kivy 
import gettuning 
import outputaudio
import recordaudio

import pyaudio
import os
from threading import Thread
from multiprocessing import Process
from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button 
from kivy.base import runTouchApp 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.core.window import Window 
from kivy.core.image import Image 
from kivy.graphics import Color, Rectangle
from kivy.base import EventLoop

import scipy, numpy, os, sys, pyaudio, struct, wave
from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

#### Record Audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
#######

Window.size=(600, 350)

tuningmenu = {  'E Standard': ['E', 'A', 'D', 'G', 'B', 'E'], 
                'Drop D': ['D', 'A', 'D', 'G', 'B', 'E'], 
                'Half Step Down': ['Eb', 'Ab', 'Db', 'Gb', 'Bb', 'Eb'], 
                'Drop Db': ['Db', 'Ab', 'Db', 'Gb', 'Bb', 'Eb'], 
                'D Standard': ['E', 'A', 'D', 'G', 'B', 'E'], 
                'Drop C': ['C', 'G', 'C', 'F', 'A', 'D'],
                'C Standard': ['C', 'F', 'B', 'E', 'G', 'C']}

dropdown = DropDown()
p = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()
outputstream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)#outputting audio
inputstream = p2.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)#inputstream
class Project(RelativeLayout):
    string1text = StringProperty(str("E"))
    string2text = StringProperty(str("A"))
    string3text = StringProperty(str("D"))
    string4text = StringProperty(str("G"))
    string5text = StringProperty(str("B"))
    string6text = StringProperty(str("E"))

    freqText = StringProperty(str("Target Freq"))
    inputText = StringProperty(str("Sound Input"))
    octaveLevelText = StringProperty(str("Octave: 4"))

    currentSelection = "E Standard"
    tunings = gettuning.getTunings(currentSelection)

    playing = False
    octave = 4
    outputAudioThread = Thread()
    

    def __init__(self, **kwargs):
        super(Project, self).__init__(**kwargs)

        recordAudioThread = Thread(None, self.recordAudio)
        recordAudioThread.daemon = True
        recordAudioThread.start()

        for tuning in tuningmenu:
            tunings = Button(text=str(tuning), size_hint_y=None, height=30)
            tunings.bind(on_release=lambda tunings: dropdown.select(tunings.text))
            tunings.bind(on_press=lambda tunings: self.dropdownselect(tunings.text))
            dropdown.add_widget(tunings)

        mainbutton = Button(text='E Standard', size_hint=(.2, .08), pos=(300, 75))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)

    def dropdownselect(self, selection):
        self.currentSelection = selection
        self.string1text = str(tuningmenu[selection][0])
        self.string2text = str(tuningmenu[selection][1])
        self.string3text = str(tuningmenu[selection][2])
        self.string4text = str(tuningmenu[selection][3])
        self.string5text = str(tuningmenu[selection][4])
        self.string6text = str(tuningmenu[selection][5])
        self.tunings = gettuning.getTunings(selection)

    def stringPlay(self, index):
        #outputAudioThread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[index],))
        self.outputAudioThread = Thread(None, outputaudio.play_tone, args=(outputstream,tuningmenu[self.currentSelection][index],self.octave))
        self.outputAudioThread.daemon = True
        self.playing = True
        self.outputAudioThread.start()


    def changeFreqText(self, index):
        self.freqText = str(self.tunings[index])

    def changeInputText(self, input):
        self.inputText = str(input)
        self.octaveLevelText = "Octave: " + str(self.octave)

    def increaseOctave(self):
        self.octave += 1
        self.octaveLevelText = "Octave: " + str(self.octave)

    def decreaseOctave(self):
        self.octave -= 1

    def Pitch(self, signal):
        signal = np.fromstring(signal, 'Int16');
        crossing = [math.copysign(1.0, s) for s in signal]
        index = find(np.diff(crossing));
        f0=round(len(index) *RATE /(2*np.prod(len(signal))))
        return f0;

    def get_note(self, freq):#Returns the musical note played
        n = round((math.log(freq/220.0)/math.log(pow(2.0, 1.0/12.0))),1) #Get Semitones away from A3(220Hz)
        while n >= 12:#Get n in terms of 0-11 semitones
            n -= 12
        while n < 0:
            n += 12
        
        if n == 0:
            return 'C'
        elif n == 1:
            return 'C#/Db'
        elif n == 2:
            return 'D'
        elif n == 3:
            return 'D#/Eb'
        elif n == 4:
            return 'E'
        elif n == 5:
            return 'F'
        elif n == 6:
            return 'F#/Gb'
        elif n == 7:
            return 'G'
        elif n == 8:
            return 'G#/Ab'
        elif n == 9:
            return 'A'
        elif n == 10:
            return 'A#'
        elif n == 11:
            return 'B'
        else:
            return ''
    def recordAudio(self):

        print ("* Recording audio...")
            
        frames = []
        
        while True:
            data = inputstream.read(CHUNK)
            freq = self.Pitch(data)
            self.changeInputText(str(self.get_note(freq))+"-"+str(freq)+"-")
            frames.append(data)

class ProjectApp(App):
    def build(self): 
        return Project()

if __name__=="__main__": 
    ProjectApp().run()