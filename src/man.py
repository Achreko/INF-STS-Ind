from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

class Man(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Message(Popup):
    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)

class GameScreen(Screen):
    def restart(self):
        for child in self.children[0].children:
            child.background_color = (1,1,1,1)
            child.state = 'normal'

root_widget = Builder.load_file('manager.kv')
