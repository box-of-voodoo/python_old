import os
import tkinter as tk
from tkinter import filedialog

zeros_gl = 0

class app(object):
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()
        self.zeros = tk.IntVar()
        
        l1 = tk.Label(frame, text=' Počet čísel')
        l1.pack( side = tk.LEFT)

        e1 = tk.Entry(frame, textvariable=self.zeros)
        e1.pack(side = tk.LEFT)

        self.hi = tk.Button(frame,text='OK', command=self.makeit)
        self.hi.pack(side = tk.LEFT)
        

        self.button = tk.Button(frame,text='EXIT',command=exit)
        self.button.pack(side = tk.LEFT)



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
        exit()


if __name__=="__main__":
    root = tk.Tk()
    root.geometry('250x40')
    app = app(root)
    root.mainloop()
