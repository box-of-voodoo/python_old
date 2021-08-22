from tkinter import *
from ai import *

font="Helvetica",20,"bold"

class dalsiokno(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.parent.title("Tic-Tac-Toe")
        for i in range(3):
            self.parent.rowconfigure(i, weight=1)
            self.parent.columnconfigure(i, weight=1)
        self.parent.minsize(300, 300) # minimální velikost
        self.parent.maxsize(900, 900) # maximální velikost
        self.parent.resizable(True, True) # je okno měnitelné
        self.turn=0
        self.buttonsfunc=[[self.but1,self.but2,self.but3],[self.but4,self.but5,self.but6],[self.but7,self.but8,self.but9]]
        self.labels=[]
        self.board=[]
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append(' ')
            self.labels.append(x)
            self.board.append(x)
        

        self.create_widgets()

    def create_widgets(self):
        menu= Menu(self.parent)
        self.parent.config(menu=menu)

        gamem= Menu()
        gamem.add_command(label='New game', command=self.new_game)
        gamem.add_command(label='Exit', command=exit)
        menu.add_cascade(label='Game', menu=gamem)

        helpm= Menu()
        helpm.add_command(label='Info', command=self.not_supp)
        menu.add_cascade(label='Help', menu=helpm)
        
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
        self.turn+=1
        self.labels[0][0]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[0][0].grid(row = 0, column = 0, sticky=NSEW)
        self.board[0][0]='X'
        
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but2(self):
        self.turn+=1
        self.labels[0][1]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[0][1].grid(row = 0, column = 1, sticky=NSEW)
        self.board[0][1]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but3(self):
        self.turn+=1
        self.labels[0][2]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[0][2].grid(row = 0, column = 2, sticky=NSEW)
        self.board[0][2]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but4(self):
        self.turn+=1
        self.labels[1][0]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[1][0].grid(row = 1, column = 0, sticky=NSEW)
        self.board[1][0]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but5(self):
        self.turn+=1
        self.labels[1][1]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[1][1].grid(row = 1, column = 1, sticky=NSEW)
        self.board[1][1]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but6(self):
        self.turn+=1
        self.labels[1][2]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[1][2].grid(row = 1, column = 2, sticky=NSEW)
        self.board[1][2]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but7(self):
        self.turn+=1
        self.labels[2][0]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[2][0].grid(row = 2, column = 0, sticky=NSEW)
        self.board[2][0]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but8(self):
        self.turn+=1
        self.labels[2][1]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[2][1].grid(row = 2, column = 1, sticky=NSEW)
        self.board[2][1]='X'
        
        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()

    def but9(self):
        self.turn+=1
        self.labels[2][2]=Label(text="X",pady=1,padx=1, bg="yellow", font=font)
        self.labels[2][2].grid(row = 2, column = 2, sticky=NSEW)
        self.board[2][2]='X'

        if self.win():
            x,y=ai(self.board,self.turn)
            self.labels[x][y]=Label(text="O",pady=1,padx=1, bg="red", font=font)
            self.labels[x][y].grid(row = x, column = y, sticky=NSEW)
            self.board[x][y]='O'
            self.win()
        
    def win(self):
        z=wins(self.board, self.turn)
        if z:
            self.label=Label(text=z,font=font)
            self.label.grid(row=0,column=0,rowspan=3,columnspan=3,sticky=NSEW)
            return False
        return True
 
    def new_game(self):
        
        try:
            self.label.grin_forget()
        except:
            pass
        self.label=Label(text='New Game', bg='green')
        self.label.grid(row=0,column=0,rowspan=3,columnspan=3,sticky=NSEW)
        try:
            self.label.grin_forget()
        except:
            pass
        for i in self.labels:
            for ii in i:
                try:
                    ii.grin_remove()
                except:
                    pass
        self.turn=0
        self.labels=[]
        self.board=[]
        
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append(' ')
            self.labels.append(x)
            self.board.append(x)
        

        self.create_widgets()

    def not_supp(self):
        pass

        
root=Tk()
root.geometry('300x300')
app=dalsiokno(root)
app.mainloop()
