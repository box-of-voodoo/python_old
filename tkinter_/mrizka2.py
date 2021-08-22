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

        self.buttonsfunc=[[self.but1,self.but2,self.but3],[self.but4,self.but5,self.but6],[self.but7,self.but8,self.but9]]
        self.labels=[]
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append('')
            self.labels.append(x)

        self.create_widgets()

    def create_widgets(self):
        self.buttons=[]
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append(Button(text=" ", bg="white",command= self.buttonsfunc[i][ii]))
            self.buttons.append(x)
        for i in range(3):
            for ii in range(3):
                self.buttons[i][ii].grid(row = i, column = ii, sticky=NSEW)


    def but1(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 0, column = 0, sticky=NSEW)
    def but2(self):
        
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 0, column = 1, sticky=NSEW)
    def but3(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 0, column = 2, sticky=NSEW)
    def but4(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 1, column = 0, sticky=NSEW)
    def but5(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 1, column = 1, sticky=NSEW)
    def but6(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 1, column = 2, sticky=NSEW)
    def but7(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 2, column = 0, sticky=NSEW)
    def but8(self):
        self.label_1=Label(text=" ", bg="white")
        self.label_1.grid(row = 2, column = 1, sticky=NSEW)
    def but9(self):
        self.label_1=Label(text="X", bg="red")
        self.label_1.grid(row = 2, column = 2, sticky=NSEW)
    
 


        
root=Tk()
root.geometry('300x300')
app=dalsiokno(root)
app.mainloop()
