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
    ct = 0
    it = 0
    flag = False
    prop = 0
    timer = None

    def restart(self):
        self.ct = 0
        self.it = 0
        self.dt = 1.5
        self.timer = Clock.schedule_interval(self.randomizer, self.dt)
        for child in self.children[0].children:
            child.state = 'normal'

    def change_flag(self):
        self.flag = True
        self.game_loop()

    def game_loop(self):
        if(self.flag):
            self.timer = Clock.schedule_interval(self.randomizer, self.dt)

    def randomizer(self, interval):
        if(self.ct != self.it):
            self.loss()
        self.it+= 1
        for child in self.children[0].children:
            child.background_color = (0,0,0,0)
            child.color = (0,0,0,0)
            child.state = 'normal'
        ran = rand(0, 8)
        self.prop = ran
        self.children[0].children[ran].state = 'down'
        self.children[0].children[ran].background_color = (1,1,1,1)
        self.children[0].children[ran].color = (1,1,1,1)


    def check(self, instance):
        self.ct+= 1
        act = int(self.get_id(instance))
        if(act == self.prop):
            self.timer.cancel()
            self.dt -= .1
            if(self.dt <= .5):
                won = Won()
                won.open()
            else:
                self.timer = Clock.schedule_interval(self.randomizer,self.dt)
        else:
            self.loss()

    def get_id(self,  instance):
        for child in instance.parent.children:
            if child.__self__ == instance:
                return child.text

    def loss(self):
        self.timer.cancel()
        lost = Lost()
        lost.open()

root_widget = Builder.load_file('manager.kv')
