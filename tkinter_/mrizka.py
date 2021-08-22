from tkinter import *
import time

class dalsiokno(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.parent.title("APP")
        self.parent.rowconfigure(0, weight=300)
        self.parent.rowconfigure(1, weight=300)
        self.parent.rowconfigure(2, weight=300)
        self.parent.columnconfigure(0, weight=300)
        self.parent.columnconfigure(1, weight=300)
        self.parent.columnconfigure(2, weight=300)
        #self.parent.minsize(300, 300) # minimální velisost
        #self.parent.maxsize(900, 900) # maximální velikost
        self.parent.resizable(True, True) # je okno měnitelné
        self.create_widgets()


    def create_widgets(self):
        self.label_1 = Label(text="X", bg="red")
        self.label_2 = Label(text="O", bg="yellow")
        self.label_3 = Label(text=" ", bg="white")
        self.label_4 = Label(text=" ", bg="white")
        self.label_5 = Label(text="O", bg="yellow")
        self.label_6 = Label(text=" ", bg="white")
        self.label_7 = Label(text="O", bg="yellow")
        self.label_8 = Label(text="X", bg="red")
        self.label_9 = Label(text="X", bg="red")
        self.label_1.grid(row = 0, column = 0, sticky=NSEW)
        self.label_2.grid(row = 0, column = 1, sticky=NSEW)
        self.label_3.grid(row = 0, column = 2, sticky=NSEW)
        self.label_4.grid(row = 1, column = 0, sticky=NSEW)
        self.label_5.grid(row = 1, column = 1, sticky=NSEW)
        self.label_6.grid(row = 1, column = 2, sticky=NSEW)
        self.label_7.grid(row = 2, column = 0, sticky=NSEW)
        self.label_8.grid(row = 2, column = 1, sticky=NSEW)
        self.label_9.grid(row = 2, column = 2, sticky=NSEW)
        self.label_1.bind("<Button-1>", self.mys1)
        self.label_2.bind("<Button-1>", self.mys1)
        self.label_3.bind("<Button-1>", self.mys1)
        self.label_4.bind("<Button-1>", self.mys1)
        self.label_5.bind("<Button-1>", self.mys1)
        self.label_6.bind("<Button-1>", self.mys1)
        self.label_7.bind("<Button-1>", self.mys1)
        self.label_8.bind("<Button-1>", self.mys1)
        self.label_9.bind("<Button-1>", self.mys1)


    def mys1(self,poloha):
        print(str(self.label_1))
        self.label_1 = Label(text="O", bg="yellow")
        self.label_1.grid(row = 0, column = 0, sticky=NSEW)
        print(poloha.widget)
        str(self.label_1)



        
root=Tk()
root.geometry('300x300')
app=dalsiokno(root)
app.mainloop()
