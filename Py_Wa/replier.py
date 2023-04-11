import pyautogui as pt
from time import sleep
import openai
import pyperclip
ar="okieokkkkokayoka"
f = open("influence.txt",'r')
def resp(s:str)->str:
    import random
    openai.api_key="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"
    eng = "text-davinci-003"
    global ar , f
    ques="answer in simple hindi&english mixed using roman script as truthfully as possible to"+s
    if(ques.lower() in ar):
        return "Okk"
    a = 0.7#round(random.uniform(0.2,0.4),1)
    completion=openai.Completion.create(
        engine=eng,
        prompt=ques,
        max_tokens=1000,
        temperature=a,
        n=1
    )
    response=completion.choices[0].text
    return response

def getmsg():
    pt.moveTo(x,y,duration=.1)
    pt.tripleClick()
    pt.hotkey('ctrl','c')
    s=pyperclip.paste()
    return s
def send():
    global x,y
    sleep(0.5)
    reply=resp(getmsg())
    pyperclip.copy(reply)
    sleep(0.5)
    pt.moveTo(x+100,y+60,duration=.1)
    pt.leftClick()
    sleep(0.5)
    pt.hotkey('ctrl' , 'v')
    pt.press('enter')
#driver code
pt.hotkey('alt', 'tab')
x=1
while(x!=0):
    sleep(0.1)
    pos=pt.locateOnScreen("smiley.png")
    x=pos[0]+75
    y=pos[1]-43
    pix = pt.pixel(int(x),int(y))
    if(pix[0]==32):
        send()
    else:
        pass


