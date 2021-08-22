from tkinter import *

class druheokno(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        
        self.create_widgets()

    def create_widgets(self):
        
        self.parent.title("Další GUI app")

        self.pack(fill=BOTH, expand=1)

        menu= Menu(self.parent)
        self.parent.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='EXIT', command=self.something)
        file.add_command(label='QUIT', command=self.something)
        file.add_command(label='EXIT', command=self.something)
        menu.add_cascade(label='File', menu=file)

        edit= Menu(menu)
        edit.add_command(label='Show text', command=self.showtext)
        menu.add_cascade(label='Edit', menu=edit)
        

    def something(self):
        quit()

    def showtext(self):
        text= Label(self, text='XXX')
        text.pack()

    
        
root=Tk()
root.geometry('300x300')
app=druheokno(root)
app.mainloop()
