
from tkinter import *


def funct():
    text=input_text.get()
    print(text)


top = Tk()
input_text= StringVar()

l1 = Label(top, text="User Name")
l1.pack( side = LEFT)
e1 = Entry(top, bd =5, textvariable=input_text)
e1.pack(side = RIGHT)
b1 = Button(top, text='OK', command=funct)
b1.pack(side = BOTTOM)


top.mainloop()
