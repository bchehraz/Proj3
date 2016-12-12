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
        DropDownLayout = AnchorLayout(orientation='horizontal')
        for tuning in tuningmenu:
            tunings = Button(text=str(tuning), size_hint_y=None, height=32)
            tunings.bind(on_release=lambda btn: dropdown.select(tunings.text))
            tunings.bind(on_press=dropdownselect(tunings.text))
            dropdown.add_widget(tunings)

        mainbutton = Button(text='E Standard', size_hint=(.2, .05), pos=(300, 100))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        DropDownLayout.add_widget(mainbutton)
        string1 = ToggleButton(text='1', size_hint=(.2, .05))
        string2 = ToggleButton(text='2')
        string3 = ToggleButton(text='3')
        string4 = ToggleButton(text='4')
        string5 = ToggleButton(text='5')
        string6 = ToggleButton(text='6')
        return DropDownLayout
    def dropdownselect(selection):
        print (self.selection)
        # for i in range(0, 6):
        #     tuningmenu(selection)


# for notes in tuningmenu:
#     notes=ToggleButton(text='B_' + str(tuningmenu.values), size_hint_y=None, height=44)

# runTouchApp(notes)


if __name__=="__main__": 
    ProjectApp().run()





