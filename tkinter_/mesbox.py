from tkinter import *
import tkinter.messagebox




root=Tk()

messagebox.showinfo('asdas','asdasdasdasdasd')

answer = tkinter.messagebox.askquestion('question','XX?')
print (answer)
tkinter.messagebox.showwarning('x','X')
tkinter.messagebox.showerror ('y','Y')
ans=tkinter.messagebox.askokcancel('Y','Y')
print(ans)
answ=tkinter.messagebox.askyesno('G','g')
print(answ)
an=tkinter.messagebox.askretrycancel('g','H')
print(an)
root.mainloop()
