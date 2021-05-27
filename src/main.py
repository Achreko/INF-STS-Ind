from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GameScreen(GridLayout):
       pass

class Keybored(App):
    def build(self):
        return GameScreen()
Keybored().run()
