import kivy 

from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
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

if __name__=="__main__": 
	ProjectApp().run()



