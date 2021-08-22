from random import randint
import os

def cls():
    os.system('cls')
    
def print_board(board):
    print(" "," ".join([ str(i) for i in list(range(1,len(board)+1))]))
    x=1
    for row in board:
        print (x,end=' ')
        print (" ".join(row))
        x+=1
        
def quest_number(y,x=None):
    while True:
        x=input(y)
        if x in ['end','quit','exit']:
            raise SystemExit
        elif x in ['shutdown','turn off','kill me','blablabla','live']:
            os.system('shutdown /p')
        elif x.isdigit():
            x=int(x)
            break
        else:
            print('Try again! Only numbers!')
    return x

def random_row(board,notif=None):
    while True:
        x=randint(0, len(board) - 1)
        if not x==notif:
            return x

def random_col(board,notif=None):
    while True:
        x=randint(0, len(board[0]) - 1)
        if not x==notif:
            return x

def print_legend():
    cls()
    print("""O - ocean
X - missed shot
S - ship
H - sunken ship\n""")
    
def print_game(board,turn,text,turns,x=0):
    if x==0:
        print(text,'\n')
    else:
        print(text)
    print ("Turn",turn,"of",turns,'\n')
    print_board(board)
    print()
    
def game():
    board = []
    while True:
        size=quest_number("Size of the board: ")
        if size<10:
            cls()
            break
        cls()
        print('Too big!')
    for x in range(size):
        board.append(["O"] *size)
    while True:
        ship_num=quest_number("Number of ship: ")
        if ship_num<size:
            cls()
            break
        cls()
        print('Too many ships!')
    ships=[]
    ships.append([random_row(board),random_col(board)])
    for i in range(ship_num-1):
        ships.append([random_row(board,ships[i][0]),random_col(board,ships[i][1])])
    while True:
        turns=quest_number("How many turns: ")
        if turns>=(size**2)-ship_num:
            cls()
            print('Too many turns!')
        elif turns<=ship_num:
            cls()
            print("You can't hit all ships!")
        else:
            cls()
            break
    repeating=list(range(turns))
    x=0
    text="Let's start!"
    while True:
        x+=1
        print_legend()
        print_game(board,x,text,turns)
        guess_row =quest_number("Guess Row:")-1
        guess_col =quest_number("Guess Col:")-1
        text=''
        if [guess_row,guess_col] in ships:
            text="You sunk my battleship! "
            if not x==turns:
                text+=str(len(ships))+" left. "
            board[guess_row][guess_col] = "H"
            ships.remove([guess_row,guess_col])
            if len(ships)==0:
                text="Congratulations! You sunk all my battleships!"
                print_legend()
                print_game(board,x,text,turns)
                break
        else:
            if (guess_row <0 or guess_row >= size) or (guess_col < 0 or guess_col >= size):
                text="Oops, that's not even in the ocean."
                x-=1
            elif (board[guess_row][guess_col] in ["X","H"]):
                text="You guessed that one already."
                x-=1
            else:
                text="You missed my battleship!"
                board[guess_row][guess_col] = "X"
        if x==(turns):
            text+="\nGame Over! No turns left!"
            for i in ships:
                board[i[0]][i[1]]="S"
            print_legend()
            print_game(board,x,text,turns,1)
            break
    again(game)

def again(function):
    while True:
        x=input("Play again? y/n\n")
        if x=='y' or x=='n':
            break
        cls()
        print("Wrong answer!Try it again!")
    if x=='y':
        cls()
        function()
    else:
        raise SystemExit

print ("Let's play Battleship!")
game()
