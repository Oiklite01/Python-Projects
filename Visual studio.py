from tkinter import * 
from tkinter import font as tkfont
root=Tk()
font_1=tkfont.Font(family='Helvetica',size=5,weight='bold')
font_2=tkfont.Font(family='Helvetica',size=2,weight='bold')
root.iconphoto(False,PhotoImage(file="Images/calculator-icon-png-28.png"))
def lable():
     label=Label(root,text="Hellow",height=10,width=10,font=font_1).pack(padx=5,pady=5)
but=Button(root,text="click me",height=5,width=5,font=font_2,command=lable).pack()
root.mainloop()
