from tkinter import *


class app(object):
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame,text='EXIT',fg='pink',command=master.destroy)
        self.button.pack(side=RIGHT)

        self.hi=Button(frame,text='something', command=self.horim)
        self.hi.pack(side=LEFT)

    def horim(self):
        print('something')

if __name__=="__main__":
    root=Tk()
    app=app(root)
    root.mainloop()
