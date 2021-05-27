import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
kivy.require("2.0.0")

class GameScreen(GridLayout):
       pass

class Keybored(App):
    def build(self):
        return GameScreen()
Keybored().run()
