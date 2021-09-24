from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','350')


class TimerWidget(Widget):
    
    count = StringProperty()
    r_color = NumericProperty()

    count_hr = StringProperty()
    count_min = StringProperty()
    count_sec = StringProperty()
    is_counting = BooleanProperty(False)
    init_count = 0
    
    def __init__(self,**kwargs):
        self.update_time(0)
        super(TimerWidget,self).__init__(**kwargs)

    def start_countdown(self):
        if(not self.is_counting and int(self.convert_to_sec()) > 0):
            self.is_counting = True
            self.init_count = self.convert_to_sec()
            Clock.schedule_interval(self.countdown,1)

    def set_countdown(self,mod):
        if(not self.is_counting):
            self.update_time(self.convert_to_sec()+int(mod))

    def stop_countdown(self):
        if(self.is_counting):
            self.is_counting = False
            Clock.unschedule(self.countdown)

    def reset_countdown(self):
        if(self.is_counting):
            self.update_time(self.init_count)
        else:
            self.update_time(0)
        self.stop_countdown()

    def countdown(self,dt):
        current_time = str(self.convert_to_sec()-1)
        if(int(current_time)<=0):
            self.update_time(0)
            self.stop_countdown()
        self.update_time(current_time)

    def convert_to_sec(self):
        return int(self.count_hr)*3600+int(self.count_min)*60+int(self.count_sec)
    
    def update_time(self,totalSeconds):
        totalSeconds = int(totalSeconds)
        if(totalSeconds<0):
            return False
        hr = str(int(totalSeconds/3600))
        min = str(int((totalSeconds%3600)/60))
        sec = str(int((totalSeconds%3600)%60))

        self.count_hr =  hr.zfill(2)
        self.count_min = min.zfill(2)
        self.count_sec = sec.zfill(2)
        self.count = f'{hr.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}'
        
class TimerApp(App):
    def __init__(self,**kwargs):
        super(TimerApp,self).__init__(**kwargs)
        self.title = 'Timer window'

if  __name__=='__main__':
    TimerApp().run()



