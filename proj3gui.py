import kivy 

from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('soundcontrols.kv')
Builder.load_file('sound.kv')
Builder.load_file('import.kv')
Builder.load_file('soundanalysis.kv')

class Project(AnchorLayout):
	pass

class ProjectApp(App):
	def build(self):
		return Project()

if __name__=="__main__": 
	ProjectApp().run()



