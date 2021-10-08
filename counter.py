from tkinter import *

count = 0

def increment():
     global count
     count+=1
     l1.configure(text=f'CLICKS => {count} times!!')
def reset():
     l1.configure(text=0)
root=Tk()
root.title("CLICK COUNTER")

l=Label(root, text="click the following button to count ")
l.grid(column=4 , row = 0)

l1=Label(root, text=0)
l1.grid(column=4,row=10)
counter = Button (root, bd= 3, padx= 5,  pady=5, text='CLICK ME',command=increment)
counter.grid(column=4 ,row=6)

counter = Button (root, bd= 3, padx= 5,  pady=5, text='RESET',command=reset)
counter.grid(column=5 ,row=6)

root.mainloop()
