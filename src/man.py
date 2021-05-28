from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Man(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

root_widget = Builder.load_file('manager.kv')
