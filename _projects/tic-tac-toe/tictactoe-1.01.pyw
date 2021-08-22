from tkinter import *
from ai import *
font2="Helvetica 16"
font1="Helvetica 25 bold"
font="Helvetica 30 bold"
loses,draws,win=0,0,0
board=[]
for i in range(3):
    x=[]
    for ii in range(3):
        x.append(' ')
    board.append(x)
turn=0
result=''

class tictactoe(Tk):

    def __init__(self,*args,**kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self,'tictactoe.ico')
        self.container = Frame(self)
        self.container.pack(side='top', fill='both', expand= True)
        self.title('Tic-Tac-Toe')
        self.minsize(300, 300)
        self.maxsize(600, 600)
        for i in range(3):
            self.container.grid_rowconfigure(i, weight=1)
            self.container.grid_columnconfigure(i, weight=1)

        self.frames={}
        self.frames_button={}
        self.frames_labelx={}
        self.frames_labelo={}
        
        for f in (start_page,help_ttt):
            frame = f(self.container,self)
            self.frames[f] = frame
            frame.grid(row=0,column=0,rowspan=3,columnspan=3,sticky='nsew')

        for i in range(3):
            for ii in range(3):
                frame = buttonxo(self.container,self,(i,ii))
                self.frames_button[(i,ii)] = frame
                frame.grid(row=i,column=ii,sticky='nsew')
                frame_l = labelx(self.container,self,(i,ii))
                self.frames_labelx[(i,ii)] = frame_l
                frame_l.grid(row=i,column=ii,sticky='nsew')
                frame_o = labelo(self.container,self,(i,ii))
                self.frames_labelo[(i,ii)] = frame_o
                frame_o.grid(row=i,column=ii,sticky='nsew')

        menu= Menu(self)
        self.config(menu=menu)

        gamem= Menu()
        gamem.add_command(label='New game', command=self.play_again)
        gamem.add_command(label='Exit', command=exit)
        menu.add_cascade(label='Game', menu=gamem)

        helpm= Menu()
        helpm.add_command(label='Stats',command=self.show_stats)
        helpm.add_command(label='Help', command=lambda: self.show_frame(help_ttt))
        menu.add_cascade(label='Info', menu=helpm)
        
        self.show_frame(start_page)
        
    def show_frame(self,contain,x=False):
        if x:
            frame=self.frames_button[contain]
        else:
            frame = self.frames[contain]
        frame.tkraise()

    def show_frame_label(self,container,x=False):
        if x:
            frame=self.frames_labelo[container]
        else:
            frame=self.frames_labelx[container]
        frame.tkraise()


    def show_u_frame(self,x):
        if x==end_page:
            self.save_result()
        frame = x(self.container,self)
        frame.grid(row=0,column=0,rowspan=3,columnspan=3,sticky='nsew')
        frame.tkraise()

    def save_result(self):
        if result=='WIN':
            x='2'
        elif result=='DRAW':
            x='1'
        else:
            x='0'
        file=open('stats.txt','a')
        file.write(x)
        file.close()

    def show_stats(self):
        global loses,draws,win
        loses,draws,win=0,0,0
        file=open('stats.txt','r')
        x=file.read()
        for i in x:
            if i=='0':
                loses+=1
            elif i=='1':
                draws+=1
            else:
                win+=1
        file.close()
        self.show_u_frame(stats)


                
    def play_again(self):
        global turn,board,result
        board=[]
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append(' ')
            board.append(x)
        turn,result=0,''
        for i in range(3):
            for ii in range(3):
                self.show_frame((i,ii),1)

    
class start_page(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self,parent)
        self.controller=controller
        label = Label(self, text='Tic-Tac-Toe', font=font1,bg='#000000',fg='#22ff99')
        label.pack(pady=0,padx=0, fill='both',expand=True)

        button1=Button(self, text="Play",font=font2,bg='#000000',fg='#22ff99',
                          command=self.start_game)
        button1.pack(fill='both',expand=True)

        button2=Button(self, text="Exit",font=font2,bg='#000000',fg='#22ff99',
                          command=quit)
        button2.pack(fill='both',expand=True)
    
    def start_game(self):
        for i in range(3):
            for ii in range(3):
                self.controller.show_frame((i,ii),1)


class end_page(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self,parent)
        
        label = Label(self, text=result, font=font1,bg='#000000',fg='#22ff99')
        label.pack(pady=0,padx=0,fill='both',expand=True)

        button1=Button(self, text="Play Again",font=font2,bg='#000000',fg='#22ff99',
                       command=controller.play_again)
        button1.pack(fill='both',expand=True)

        button2=Button(self, text="Exit",font=font2,bg='#000000',fg='#22ff99',
                       command=quit)
        button2.pack(fill='both',expand=True)

                
class buttonxo(Frame):
    def __init__(self, parent, controller,parameters):
        Frame.__init__(self,parent)
        self.controller=controller
        self.parameters=parameters
        self.x,self.y=self.parameters
        button1 = Button(self, text='', font=font,bg='#000000',command=self.move)############ func in controller
        button1.pack(fill='both',expand=True)
            
    def move(self):
        self.controller.show_frame_label(self.parameters)
        global turn,board,result
        board[self.x][self.y]='X'
        turn+=1
        result=wins(board,turn)
        if not result:
            x,y=ai(board,turn)
            board[x][y]='O'
            para=x,y
            self.controller.show_frame_label(para,True)
            result=wins(board,turn)
        if result:
             self.controller.show_u_frame(end_page)


class labelx(Frame):
    def __init__(self, parent, controller,parameters):
        Frame.__init__(self,parent)
        self.controller=controller
        self.x,self.y=parameters
        label1= Label(self, text='X',font=font, bg='#000000',fg='#22ff99')
        label1.pack(pady=1,padx=1,fill='both',expand=True)
        

class labelo(Frame):
    def __init__(self, parent, controller,parameters):
        Frame.__init__(self,parent)
        self.controller=controller
        self.x,self.y=parameters
        label1= Label(self, text='O',font=font, bg='#000000',fg='#22ff99')
        label1.pack(pady=1,padx=1,fill='both',expand=True)

class help_ttt(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text='''not supported''',bg='#000000',fg='#22ff99')
        label.pack(pady=0,padx=0, fill='both',expand=True)
        button1=Button(self, text="Back",font=font2,bg='#000000',fg='#22ff99',
                       command=lambda: controller.show_frame(start_page))
        button1.pack(side='bottom', fill='both')
    
class stats(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller=controller
        
        label = Label(self, text='Wins: '+str(win)+'\nDraws: '+str(draws)+'\nLoses: '+str(loses)
                      ,font=font2,bg='#000000',fg='#22ff99')
        label.pack(pady=0,padx=0, fill='both',expand=True)
        button1=Button(self, text="Reset stats",font=font2,bg='#000000',
                       fg='#22ff99',command=self.reset_stats)####################
        button2=Button(self, text="Back",font=font2,bg='#000000',fg='#22ff99',
                       command=lambda: controller.show_frame(start_page))
        button2.pack(side='bottom', fill='both')
        button1.pack(side='bottom', fill='both')

    def reset_stats(self):
        global win,draws,loses
        win,draws,loses=0,0,0
        file=open('stats.txt','r+')
        file.seek(0)
        file.truncate()
        file.close()
        self.controller.show_u_frame(stats) 



app = tictactoe()
app.mainloop()
