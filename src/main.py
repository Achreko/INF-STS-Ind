from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Keybored(App):
    def build(self):
        fl = FloatLayout()
        for i in range(0,9):
            fl.add_widget(Button(
                background_color = (0,0,0,0)))

        return fl

if __name__ == "__main__":
    Keybored().run()
