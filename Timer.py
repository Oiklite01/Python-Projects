import threading as th
from playsound import playsound
from pynput.keyboard import Listener,KeyCode,Key
inp=True
def player():
     global inp
     def on_press(key):
          if key==KeyCode(char='s'):
               listener.stop()
     with Listener(on_press=on_press) as listener:
         listener.join()
     inp=False
def sound():
     th.Thread(target=player,args=(),daemon=True).start()
     while inp:
         while True:
            try:
                playsound('alarm.wav')
            except:
                print("sound error")
                break
def countdown(tmp):
     def time_format(inp):
          import os
          m,s=divmod(inp,60)
          os.system('cls')
          if(len(str(m))>1):
               if(len(str(s))>1):
                    print("{}:{}".format(m,s))
               elif(len(str(s))==1):
                    print("{}:0{}".format(m,s))
          else:
               if(len(str(s))>1):
                    print("0{}:{}".format(m,s))
               elif(len(str(s))==1):
                    print("0{}:0{}".format(m,s))
     from time import time,sleep
     if(":" in tmp):
          a=[int(x) for x in tmp.split(":")]
     else:
          a=[int(x) for x in tmp.split()]
     if(len(a)==1):
          t=int(*a)-1
          time_format(t)
     elif(len(a)==2):
          t=(a[0]*60+a[1])-1
          time_format(t)
     while(t>0):
          t-=1
          sleep(1)
          time_format(t)
     print("Time up")
     print("Press >S< to stop")
     sound()
     return 0
def main():
     print("Welcome to Timer")
     x=input("enter time (mins sec or mins:sec)")
     countdown(x)
if __name__=="__main__":
     main()
