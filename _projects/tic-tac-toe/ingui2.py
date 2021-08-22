from tkinter import *
from ai import *
from tkinter import messagebox
font2="Helvetica 16"
font1="Helvetica 25 bold"
font="Helvetica 30 bold"
best_score=[]
board=[]
for i in range(3):
    x=[]
    for ii in range(3):
        x.append(' ')
    board.append(x)
turn=0
result=''
p_name=''
bg='#000000'#ffffff
fg='#22ff99'#090909
bge='#111111'#eeeeee
app=''
#def popup(x):
#    popup = Tk()
#    popup.configure(bg=bg)
#    popup.wm_title('Warning!')
#    labelpopup = Label(popup,text=x,bg=bg,fg=fg,font=font)
#    buttonpopup = Button(popup,text='OK',command=popup.destroy,bg=bg,fg=fg)
#    labelpopup.pack(fill='both',expand=True)
#    buttonpopup.pack(expand=True)
#    popup.mainloop()
    

    
def playername():
    firstwindow = Tk()
    firstwindow.configure(bg=bg)
    Tk.iconbitmap(firstwindow,'tictactoe.ico')
    firstwindow.geometry('250x80')
    player_name = StringVar()
    for i in range(3):
        firstwindow.grid_rowconfigure(i,weight=1)
    firstwindow.grid_columnconfigure(0,weight=1)
    firstwindow.grid_columnconfigure(1,weight=10)
    firstwindow.grid_columnconfigure(2,weight=1)

    def check_name(x):
        z=([chr(i) for i in range(48,58)]+
           [chr(i) for i in range(97,123)]+
           [chr(i) for i in range(65,91)]+
           [chr(i) for i in range(192,383)])
        for i in x:
            if not i in z:
                return False
        return True
    
    def save_name(*args):
        global p_name,app
        p_name=player_name.get()
        if not p_name.isdigit() and check_name(p_name) and p_name!='':
            firstwindow.destroy()
            app = tictactoe()
            app.mainloop()
        else:
            #popup('Enter your player name')
            messagebox.showerror ('Enter your name!','Only letters and numbers!')


    firstwindow.wm_title('Tic-Tac-Toe')
    labelfw = Label(firstwindow, text='Enter your name',bg=bg,fg=fg)
    entryfw = Entry(firstwindow, textvariable = player_name,bg=bge, fg=fg)
    buttonfw = Button(firstwindow, text='OK', command=save_name,bg=bg,fg=fg)
    entryfw.bind('<Return>',save_name)
    labelfw.grid(row=0,column=1,sticky='NSEW')
    entryfw.grid(row=1,column=1,sticky='NSEW')
    buttonfw.grid(row=2,column=1)
    entryfw.focus()
    firstwindow.mainloop()
    
    


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
        
        for f in (start_page,help_ttt,credits_):
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
        gamem.add_command(label='New player', command=self.new_player)
        gamem.add_command(label='Exit', command=exit)
        menu.add_cascade(label='Game', menu=gamem)

        helpm= Menu()
        helpm.add_command(label='Stats',command=self.show_stats)
        helpm.add_command(label='Help', command=lambda: self.show_frame(help_ttt))
        helpm.add_command(label='Credits', command=lambda: self.show_frame(credits_))
        menu.add_cascade(label='Info', menu=helpm)

        optm= Menu()
        optm.add_command(label='Change color',command=self.change_color)
        menu.add_cascade(label='Options',menu=optm)
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
        file.write(';'+p_name+';'+x)
        file.close()

    def show_stats(self):#############
        global best_score

        file=open('stats.txt','r')
        x=file.read()
        score_list=x.split(';')
        score={}
        for i,v in enumerate(score_list):
            if v=='':
                pass
            elif not v.isdigit():
                score_name=v
                if not score_name in score:
                    score[score_name]=[0,0,0]
            else:
                
                if v=='0':
                    score[score_name][0]+=1
                elif v=='1':
                    score[score_name][1]+=1
                else:
                    score[score_name][2]+=1
                
        file.close()
        a,b,c,d,e,best_score=0,0,0,0,0,[]
        for k,v in score.items():
            p=(v[1]+v[2]*2)/sum(v)
            if p>e:
                if p>a:
                    a,b,c,d,e=p,a,b,c,d
                    if len(best_score)==5:
                        best_score[0]=[k,v[0],v[1],v[2]]
                    else:
                        best_score.insert(0,[k,v[0],v[1],v[2]])
                elif p>b:
                    b,c,d,e=p,b,c,d
                    if len(best_score)==5:
                        best_score[1]=[k,v[0],v[1],v[2]]
                    else:
                        best_score.insert(1,[k,v[0],v[1],v[2]])
                elif p>c:
                    c,d,e=p,c,d
                    if len(best_score)==5:
                        best_score[2]=[k,v[0],v[1],v[2]]
                    else:
                        best_score.insert(2,[k,v[0],v[1],v[2]])
                elif p>d:
                    d,e=p,d
                    if len(best_score)==5:
                        best_score[3]=[k,v[0],v[1],v[2]]
                    else:
                        best_score.insert(3,[k,v[0],v[1],v[2]])
                else:
                    e=p
                    if len(best_score)==5:
                        best_score[4]=[k,v[0],v[1],v[2]]
                    else:
                        best_score.insert(4,[k,v[0],v[1],v[2]])
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

    def new_player(self):
        global turn,board,result,best_score
        tictactoe.destroy(self)
        best_score=[]
        board=[]
        for i in range(3):
            x=[]
            for ii in range(3):
                x.append(' ')
            board.append(x)
        turn=0
        result=''
        playername()


    def change_color(self):
        global bg,fg,bge,app
        if bg=='#ffffff':
            bg='#000000'
            fg='#22ff99'
            bge='#111111'
            x='dark'
        else:
            bg='#ffffff'
            fg='#090909'
            bge='#eeeeee'
            x='white'
        app.destroy()
        app = tictactoe()
        app.mainloop()
        
class start_page(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self,parent)
        self.controller=controller
        label = Label(self, text='Tic-Tac-Toe', font=font1,bg=bg,fg=fg)
        label.pack(pady=0,padx=0, fill='both',expand=True)

        button1=Button(self, text="Play",font=font2,bg=bg,fg=fg,
                          command=self.start_game)
        button1.pack(fill='both',expand=True)

        button2=Button(self, text="Exit",font=font2,bg=bg,fg=fg,
                          command=quit)
        button2.pack(fill='both',expand=True)
    
    def start_game(self):
        for i in range(3):
            for ii in range(3):
                self.controller.show_frame((i,ii),1)


class end_page(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self,parent)
        
        label = Label(self, text=result, font=font1,bg=bg,fg=fg)
        label.pack(pady=0,padx=0,fill='both',expand=True)

        button1=Button(self, text="Play Again",font=font2,bg=bg,fg=fg,
                       command=controller.play_again)
        button1.pack(fill='both',expand=True)

        button2=Button(self, text="Exit",font=font2,bg=bg,fg=fg,
                       command=quit)
        button2.pack(fill='both',expand=True)

                
class buttonxo(Frame):
    def __init__(self, parent, controller,parameters):
        Frame.__init__(self,parent)
        self.controller=controller
        self.parameters=parameters
        self.x,self.y=self.parameters
        button1 = Button(self, text='', font=font,bg=bg,command=self.move)############ func in controller
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
        label1= Label(self, text='X',font=font, bg=bg,fg=fg)
        label1.pack(pady=1,padx=1,fill='both',expand=True)
        

class labelo(Frame):
    def __init__(self, parent, controller,parameters):
        Frame.__init__(self,parent)
        self.controller=controller
        self.x,self.y=parameters
        label1= Label(self, text='O',font=font, bg=bg,fg=fg)
        label1.pack(pady=1,padx=1,fill='both',expand=True)

class help_ttt(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text=(
            '''If you need help for this game
then you aren't mentaly ready to using this app.'''),bg=bg,fg=fg)
        label.pack(pady=0,padx=0, fill='both',expand=True)
        button1=Button(self, text="Back",font=font2,bg=bg,fg=fg,
                       command=lambda: controller.show_frame(start_page))
        button1.pack(side='bottom', fill='both')
    
class credits_(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text=(
            '''\nAll credits go to me!!!!\n\n[shinobu laugh]\n\n'''),bg=bg,fg=fg,font=font2)
        label.pack(pady=0,padx=0, fill='both',expand=True)
        label2 = Label(self, text=('minakuba,bubak10100,wogat'),bg=bg,fg=fg)
        button1=Button(self, text="Back",font=font2,bg=bg,fg=fg,
                       command=lambda: controller.show_frame(start_page))
        button1.pack(side='bottom', fill='both')
        label2.pack(pady=0,padx=0, fill='both', side='bottom',expand=True)

class stats(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.configure(bg=bg)
        
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(6,weight=1)

        p_label=Label(self, text='Player',bg=bg,fg=fg)
        w_label=Label(self, text='Wins',bg=bg,fg=fg)
        d_label=Label(self, text='Draws',bg=bg,fg=fg)
        l_label=Label(self, text='Loses',bg=bg,fg=fg)
        s_label=Label(self, text='Score',bg=bg,fg=fg)

        p_label.grid(row=0,column=1,sticky='NSEW')
        w_label.grid(row=0,column=2,sticky='NSEW')
        d_label.grid(row=0,column=3,sticky='NSEW')
        l_label.grid(row=0,column=4,sticky='NSEW')
        s_label.grid(row=0,column=5,sticky='NSEW')
        
        player_labels,win_labels,draw_labels,lose_labels,score_labels,rank_labels=[],[],[],[],[],[]
        for i,v in enumerate(best_score):
            rank_labels.append(Label(self, text=str(i+1),bg=bg,fg=fg))
            player_labels.append(Label(self, text=v[0],bg=bg,fg=fg))
            win_labels.append(Label(self, text=str(v[3]),bg=bg,fg=fg))
            draw_labels.append(Label(self, text=str(v[2]),bg=bg,fg=fg))
            lose_labels.append(Label(self, text=str(v[1]),bg=bg,fg=fg))
            score_labels.append(Label(self, text=str(round((v[3]*2+v[2])/(v[1]+v[2]+v[3]),3)),
                              bg=bg,fg=fg))
            rank_labels[i].grid(row=i+1,column=0,sticky='NSEW')
            player_labels[i].grid(row=i+1,column=1,sticky='NSEW')
            win_labels[i].grid(row=i+1,column=2,sticky='NSEW')
            draw_labels[i].grid(row=i+1,column=3,sticky='NSEW')
            lose_labels[i].grid(row=i+1,column=4,sticky='NSEW')
            score_labels[i].grid(row=i+1,column=5,sticky='NSEW')

            
        button1=Button(self, text="Reset stats",font=font2,bg=bg,
                       fg=fg,command=self.reset_stats)
        button1.grid(row=6,columnspan=6,sticky='NESW')

    def reset_stats(self):
        global best_score
        best_score=[]
        file=open('stats.txt','r+')
        file.seek(0)
        file.truncate()
        file.close()
        self.controller.show_u_frame(stats)


playername()

