import tkinter


class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.create_widgets()

    def create_widgets(self):
        self.label_1=tkinter.Label(text="Hello world!",bg='black',fg='white')
        self.label_2=tkinter.Label(text="Hello second time",bg='pink')
        self.label_3=tkinter.Label(text="place",bg="red")
        self.label_1.pack(side=tkinter.TOP,fill=tkinter.X,expand=True)
        self.label_2.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
        self.label_3.place(x=1,y=1, anchor=tkinter.NW)#place
        #print(help(self.label_1.pack))

root = tkinter.Tk()
root.geometry("250x150+300+300")
app = MainWindow(root)
app.mainloop()
