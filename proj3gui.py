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
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button 
from kivy.base import runTouchApp 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.core.window import Window 

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



Window.size=(700, 400)

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
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)#output

class Project(AnchorLayout):
    string1text = StringProperty(str("E"))
    string2text = StringProperty(str("A"))
    string3text = StringProperty(str("D"))
    string4text = StringProperty(str("G"))
    string5text = StringProperty(str("B"))
    string6text = StringProperty(str("E"))

    freqText = StringProperty(str("Target Freq"))
    inputText = StringProperty(str("Sound Input"))

    tunings = gettuning.getTunings("E Standard")

    playing = False

    def __init__(self, **kwargs):
        super(Project, self).__init__(**kwargs)

        recordAudioThread = Thread(None, self.recordAudio)
        recordAudioThread.daemon = True
        recordAudioThread.start()

        for tuning in tuningmenu:
            tunings = Button(text=str(tuning), size_hint_y=None, height=24)
            tunings.bind(on_release=lambda tunings: dropdown.select(tunings.text))
            tunings.bind(on_press=lambda tunings: self.dropdownselect(tunings.text))
            dropdown.add_widget(tunings)

        mainbutton = Button(text='E Standard', size_hint=(.2, .05), pos_hint=(650, 75))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)

        # print("X")
        # recordingthread.start()
        # recordingthread.join()

    def dropdownselect(self, selection):
        #self.string1.text = tuningmenu[selection].get(0)
        #print (tuningmenu[selection])
        self.string1text = str(tuningmenu[selection][0])
        self.string2text = str(tuningmenu[selection][1])
        self.string3text = str(tuningmenu[selection][2])
        self.string4text = str(tuningmenu[selection][3])
        self.string5text = str(tuningmenu[selection][4])
        self.string6text = str(tuningmenu[selection][5])
        self.tunings = gettuning.getTunings(selection)

    def string1Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[0]))
        newthread.daemon = True
        newthread.start()

    def string2Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[1]))
        newthread.daemon = True
        newthread.start()

    def string3Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[2]))
        newthread.daemon = True
        newthread.start()

    def string4Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[3]))
        newthread.daemon = True
        newthread.start()

    def string5Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[4]))
        newthread.daemon = True
        newthread.start()

    def string6Callback(self):
        newthread = Thread(None, outputaudio.play_tone, args=(stream,self.tunings[5]))
        newthread.daemon = True
        newthread.start()

    def changeFreqText(self, index):
        self.freqText = str(self.tunings[index])

    def changeInputText(self, input):
        self.inputText = str(input)

    def Pitch(self, signal):
        signal = np.fromstring(signal, 'Int16');
        crossing = [math.copysign(1.0, s) for s in signal]
        index = find(np.diff(crossing));
        f0=round(len(index) *RATE /(2*np.prod(len(signal))))
        return f0;

    def recordAudio(self):
    
        audio = pyaudio.PyAudio()
        
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print ("* Recording audio...")
            
        frames = []
        
        while True:
            data = stream.read(CHUNK)
            self.changeInputText(self.Pitch(data))
            frames.append(data)

class ProjectApp(App):
    def build(self): 
        return Project()

if __name__=="__main__": 
    ProjectApp().run()