from pynput.keyboard import Key, Listener,KeyCode
from playsound import playsound
from time import sleep
  
def show(key):
     if(key!=KeyCode(char='s')):
         playsound('alarm.wav')
         show(key)
     elif(key==KeyCode(char='s')):
          return False
          
    # by pressing 'delete' button 
    # you can terminate the loop 
show('s')
# Collect all event until released
with Listener(on_press = show) as listener:
     listener.join()
