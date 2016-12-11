import kivy 

from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button 
from kivy.base import runTouchApp 

Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 300)

Builder.load_file('soundcontrols.kv')
Builder.load_file('sound.kv')
Builder.load_file('soundanalysis.kv')

class Project(AnchorLayout):
    pass

class ProjectApp(App):
    def build(self): 
       return Project()

dropdown = DropDown()
tuningmenu = ['E Standard', 'Drop D', 'Half Step Down', 'Drop Db', 'D Standard', 'Drop C', 'C Standard']
for tuning in tuningmenu:
    btn = Button(text=str(tuning), size_hint_y=None, height=44)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)

mainbutton = Button(text='E Standard', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

'''runTouchApp(mainbutton)'''

if __name__=="__main__": 
    ProjectApp().run()





