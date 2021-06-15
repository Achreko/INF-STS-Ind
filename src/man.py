from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from random import randint as rand

class Man(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Lost(Popup):
    pass

class Won(Popup):
    pass

class GameScreen(Screen):
    dt = 1.5
    flag = False
    prop = 1
    timer = None

    def restart(self):
        self.timer = Clock.schedule_interval(self.randomizer, self.dt)
        for child in self.children[0].children:
            # child.background_color = (1,1,1,1)
            child.state = 'normal'

    def change_flag(self):
        self.flag = True
        self.game_loop()

    def game_loop(self):
        if(self.flag):
            self.timer = Clock.schedule_interval(self.randomizer, self.dt)

    def randomizer(self, interval):
        for child in self.children[0].children:
            # child.background_color = (1,1,1,1)
            child.state = 'normal'
        ran = rand(0, 8)
        self.prop = ran
        self.children[0].children[ran].state = 'down'

    def check(self, instance):
        act = int(self.get_id(instance))
        if(act == self.prop):
            self.timer.cancel()
            print(self.dt)
            self.dt -= .1
            if(self.dt <= .7):
                won = Won()
                won.open()
            else:
                self.timer = Clock.schedule_interval(self.randomizer,self.dt)
        else:
            self.timer.cancel()
            lost = Lost()
            lost.open()

    def get_id(self,  instance):
        for child in instance.parent.children:
            if child.__self__ == instance:
                return child.text

root_widget = Builder.load_file('manager.kv')
