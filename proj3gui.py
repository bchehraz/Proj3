import kivy 

from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button 
from kivy.base import runTouchApp 
from kivy.uix.togglebutton import ToggleButton

Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 300)

Builder.load_file('soundcontrols.kv')
Builder.load_file('sound.kv')
Builder.load_file('soundanalysis.kv')

tuningmenu = {'E Standard': ['E', 'A', 'D', 'G', 'B', 'E'] , 
                'Drop D': ['D', 'A', 'D', 'G', 'B', 'E'], 
                'Half Step Down': ['Eb', 'Ab', 'Db', 'Gb', 'Bb', 'Eb'], 
                'Drop Db': ['Db', 'Ab', 'Db', 'Gb', 'Bb', 'Eb'], 
                'D Standard': ['E', 'A', 'D', 'G', 'B', 'E'], 
                'Drop C': ['C', 'G', 'C', 'F', 'A', 'D'], 
                'C Standard': ['C', 'F', 'B', 'E', 'G', 'C']}

dropdown = DropDown()

class Project(AnchorLayout):
    pass

class ProjectApp(App):
    def build(self): 
        return Project()


for tuning in tuningmenu:
    btn = Button(text=str(tuning), size_hint_y=None, height=32)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)

mainbutton = Button(text='E Standard', size_hint=(.2, .05), pos=(300, 100))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


for notes in range(6):
    notes=ToggleButton(text='B_' + str(notes), size_hint_y=None, height=44)

runTouchApp(notes)


if __name__=="__main__": 
    ProjectApp().run()





