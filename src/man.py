from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Man(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Lost(Popup):
    def __init__(self, **kwargs):
        super(Lost, self).__init__(**kwargs)

class Won(Popup):
    pass

class GameScreen(Screen):
    dt = 1
    flag = False
    prop = 1
    timer = None

    def restart(self):
        for child in self.children[0].children:
            child.background_color = (1,1,1,1)
            child.state = 'normal'

    def change_flag(self):
        self.flag = True
        self.game_loop()

    def game_loop(self):
        if(self.flag):
            self.timer = Clock.schedule_interval(self.randomizer, self.dt)

    def randomizer(self, interval):
        print ('Tak')

    def check(self, instance):
        act = int(self.get_id(instance))
        if(act == self.prop):
            self.dt -= .2
            self.timer.cancel()
            if(self.dt == 0.2):
                won = Won()
                won.open()
            else:
                self.timer = Clock.schedule_interval(self.randomizer,self.dt)
        else:
            lost = Lost()
            lost.open()

    def get_id(self,  instance):
        for child in instance.parent.children:
            if child.__self__ == instance:
                return child.text

root_widget = Builder.load_file('manager.kv')
