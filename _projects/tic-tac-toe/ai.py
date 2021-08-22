import os
from random import randint

def item_of_listx_in_listy(listx,listy):
    for i in listx:
        if i in listy:
            return True
    return False

def where(list1,list2):
    for i,v in enumerate(list1):
        if v in list2:
            return i

def where2(list1,eleme):
    for i,v in enumerate(list1):
        if v==eleme:
            return i

def ai(board,turn,plchar='X',pcchar='O',nonechar=' '):
    condi=[[i[0] for i in board],
           [i[1] for i in board],
           [i[2] for i in board],
           [board[i][i] for i in range(3)],
           [board[2-i][i]for i in range(3)]]
    twocondi=[]
    for i in [plchar,pcchar]:
        twocondi.append([nonechar,i,i])
        twocondi.append([i,nonechar,i])
        twocondi.append([i,i,nonechar])
    zerocondi=[plchar,pcchar,plchar]
    onecondi=[[nonechar,pcchar,plchar],[plchar,pcchar,nonechar]]
    situd=condi[3:]
    situp=[board[1],condi[1]]
    
    if board[1][1]==nonechar:
        return 1,1

    elif turn==1:
        x=randint(0,1)
        xx=[0,2]
        y=randint(0,1)
        yy=[0,2]
        return xx[x],yy[y]
    
    elif (item_of_listx_in_listy(twocondi,board)
          or item_of_listx_in_listy(twocondi,condi)):
        
        if item_of_listx_in_listy(twocondi[3:],board):#O-row
            x=where(board,twocondi[3:])
            y=where2(twocondi[3:],board[x])
            return x,y
        
        elif item_of_listx_in_listy(twocondi[3:],condi):#O-col+diag
            x=where(condi,twocondi[3:])
            y=where2(twocondi[3:],condi[x])
            if x<3:#O-col
                return y,x
            elif x==3:#diag
                return y,y
            elif x==4:
                return (2-y),y
                
        elif item_of_listx_in_listy(twocondi[:3],board):#X-row
            x=where(board,twocondi[:3])
            y=where2(twocondi[:3],board[x])
            return x,y
        
        elif item_of_listx_in_listy(twocondi[:3],condi):#X-col+diag
            x=where(condi,twocondi[:3])
            y=where2(twocondi[:3],condi[x])
            if x<3:#X-col
                return y,x
            elif x==3:#diag
                return y,y
            elif x==4:
                return (2-y),y

    elif turn!=1:
        if zerocondi in situd:
            return 0,1
        elif zerocondi in situp:
            return 0,0
        elif (item_of_listx_in_listy(onecondi,situd)
              and item_of_listx_in_listy(onecondi,situp)):
            x=where(onecondi,situd)
            xx=where2(situd,onecondi[x])
            y=where(onecondi,situp)
            yy=where2(situp,onecondi[y])
            r=[x,xx,y,yy]
            if r in [[0,1,0,1],[1,1,0,0]]:
                return 2,2
            elif r in [[0,0,1,0],[1,0,0,1]]:
                return 2,0
            elif r in [[0,0,1,1],[1,0,0,0]]:
                return 0,2
            elif r in [[0,1,1,0],[1,1,1,1]]:
                return 0,0
        elif [plchar,plchar] in ([board[0][1],board[1][2]],
                                 [board[1][2],board[2][1]],
                                 [board[2][1],board[1][0]],
                                 [board[1][0],board[0][1]]):
            print(0)
            if [plchar,plchar]==[board[0][1],board[1][2]]:
                if board[0][2]==nonechar:
                    return 0,2
            elif [plchar,plchar]==[board[2][1],board[1][2]]:
                if board[2][2]==nonechar:
                    return 2,2
            elif [plchar,plchar]==[board[2][1],board[1][0]]:
                if board[2][0]==nonechar:
                    return 2,0
            elif[plchar,plchar]==[board[0][1],board[1][0]]:
                if board[0][0]==nonechar:
                    return 0,0
    x=[]
    for ii,zz in enumerate(board):
        for i,z in enumerate(zz):
            if z==nonechar:
                x.append([ii,i])
    while True:
        y=randint(0,len(x)-1)
        if board[x[y][0]][x[y][1]]==nonechar:
            return x[y][0],x[y][1]


def wins(board,turn,plchar='X',pcchar='O',nonechar=' '):
    x,o=[plchar,plchar,plchar],[pcchar,pcchar,pcchar]
    condi=[[i[0] for i in board],
           [i[1] for i in board],
           [i[2] for i in board],
           [board[i][i] for i in range(3)],
           [board[2-i][i]for i in range(3)]]
    draw=[[nonechar,plchar,plchar],[plchar,nonechar,plchar],
          [plchar,plchar,nonechar]]
    
    if x in board or x in condi:
        return 'WIN'
    elif o in board or o in condi:
        return 'LOSE'
    elif (turn>4 and not(x in board or x in condi)
          and not(o in board or o in condi)
          and not(item_of_listx_in_listy(draw,board))):
        return 'DRAW'
    else:
        return False

#############################################



def cls():
    os.system('cls')

def q_num(text):
    while True:
        x=input(text)
        if x in ['end','quit','exit','e']:
            raise SystemExit
        elif x.isdigit():
            return int(x)
        else:
            print('Only numbers!')
def q_con(text,low_con,high_con):
    while True:
        x=q_num(text)
        if x>low_con and x<high_con:
            return x
        print('Higher than',low_con,'and lower than',high_con)

def print_board(x):
    print('╔═══╦═══╦═══╗')
    print('║ '+x[0][0]+' ║ '+x[0][1]+' ║ '+x[0][2]+' ║')
    print('╠═══╬═══╬═══╣')
    print('║ '+x[1][0]+' ║ '+x[1][1]+' ║ '+x[1][2]+' ║')
    print('╠═══╬═══╬═══╣')
    print('║ '+x[2][0]+' ║ '+x[2][1]+' ║ '+x[2][2]+' ║')
    print('╚═══╩═══╩═══╝')



def field(p_field):
    if p_field in [1,2,3]:
        p_row=2
    elif p_field in [4,5,6]:
        p_row=1
    elif p_field in [7,8,9]:
        p_row=0
    if p_field in [1,4,7]:
        p_col=0
    elif p_field in [2,5,8]:
        p_col=1
    elif p_field in [3,6,9]:
        p_col=2
    return p_row,p_col

def question_yn(question,wrong_answer):
    while True:
        x=input(question)
        if x in ['y','n','Y','N']:
            if x in ['y','Y']:
                return True
            else:
                return False
        print(wrong_answer)
        
def again(function):
    
    x=question_yn('Again? y/n\n','Try it again.')
    if x:
        function()
    else:
        raise SystemExit


helpagain=0
def help_f():
    global helpagain
    if helpagain in [0,1]:
        qhelp=question_yn('Help? y/n\n','Try it again')
        bhelp=[['7','8','9'],['4','5','6'],['1','2','3']]
        if qhelp:
            print_board(bhelp)
            input('Press Enter to continue...')
        else:
            helpagain+=1


def game():
    board=[]
    for i in range(3):
        x=[]
        for z in range(3):
            x.append(' ')
        board.append(x)
    turn=0
    help_f()
    while True:
        turn+=1
        cls()
        print_board(board)
        while True:
            p_field=q_con('Field: ',0,10)
            p_row,p_col=field(p_field)
            if board[p_row][p_col]==' ':
                break
            print('Only free fields!')
        board[p_row][p_col]='X'
        end=wins(board,turn)
        if end:
            cls()
            print_board(board)
            print(end)
            break
        posx,posy=ai(board,turn)
        board[posx][posy]='O'
        end=wins(board,turn)
        if end:
            cls()
            print_board(board)
            print(end)
            break
    help_f()
    again(game)
if __name__ == "__main__":
    print('''Let's play tic-tac-toe\n\n\n\n\n\n\n''')
    input('Press Enter to continue...')
    cls()
    game()
