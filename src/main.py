import kivy
kivy.require("2.0.0")

from kivy.app import App
from man import root_widget


class Keybored(App):
    def build(self):
        return root_widget

Keybored().run()
