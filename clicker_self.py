from time import sleep
import threading as th
from pynput.mouse import Button,Controller
from pynput.keyboard import Listener, KeyCode


class ClickMouse(th.Thread):
     def __init__(self,delay,button):
          super().__init__()          
          self.delay = delay
          self.button = button
          self.running = False
          self.program = True
     def StartClickking(self):
          self.running=True
     def StopClicking(self):
          self.running = False
     def Exit(self):
          self.StopClicking()
          self.program = False
     def run(self):
          while (self.program):
               while self.running:
                    mouse.click(self.button)
                    sleep(self.delay)


     
def on_press(key):
     if(key==k1):
          if clicking.running:
               clicking.StopClicking()
          else:
               clicking.StartClickking()
     elif(key==k2):
          clicking.Exit()
          listener.stop()
delay= 0.001
button= Button.left
k1 = KeyCode(char='s')
k2 = KeyCode(char='d')
mouse = Controller()
clicking=ClickMouse(delay,button)
clicking.start()
with Listener (on_press=on_press) as listener:
     listener.join()
