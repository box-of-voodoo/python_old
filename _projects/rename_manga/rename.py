import os
import tkinter as tk
from tkinter import filedialog

zeros_gl = 0


class app(object):
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()
        self.zeros = tk.IntVar()
        self.zeros.set(3)

        for i in range(3):
            frame.grid_rowconfigure(i,weight=1)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_columnconfigure(1,weight=10)
        frame.grid_columnconfigure(2,weight=1)
        
        l1 = tk.Label(frame, text='Počet čísel')
        l1.grid(row=0,column=1,sticky='NSEW')

        e1 = tk.Entry(frame, textvariable=self.zeros)
        e1.bind('<Return>',self.makeit)
        e1.grid(row=1,column=1,sticky='NSEW')
        e1.focus()
        
        self.hi = tk.Button(frame,text='OK', command=self.makeit)
        self.hi.grid(row=2,column=1)
        




    def makeit(self):
        zeros_gl = self.zeros.get()
        folder = filedialog.askdirectory()
        directory = os.listdir(folder)

        for file in directory:
            if not '.' in file:
                continue
            if len(file[:-4]) < zeros_gl:
                diff = zeros_gl - len(file[:-4])
                new_name = '0'*diff+file
                os.rename(folder+'/'+file, folder+'/'+new_name)
        run()

def run():
    root.mainloop()

if __name__=="__main__":
    root = tk.Tk()
    root.geometry('250x80')
    app = app(root)
    root.mainloop()
