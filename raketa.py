
def telo(znakA,znakB,width,w=None):
    print(znakA,end='')
    print(znakB*(width-2),end='')
    if w is None:
        print(znakA)
    elif w!=1:
        print(znakA,end='')
        
def znak(pocet,znak=None):
    if znak is None:
        print('-'*pocet,end='')
    else:
        print(znak*pocet,end='')

def okno(sirka,delka,znakA,znakB,znakC,x,zz,o):
    znak(zz)
    telo(znakA,znakB,o+2,1)
    print('╔'+'═'*(sirka-((o+1)*2))+'╗',end='')
    print(znakB*o,end='')
    print(znakA)
    while delka>0:
        if delka>8:
            delka=8
        else:
            znak(zz)
            telo(znakA,znakB,o+2,1)
            print('║'+znakC*(sirka-((o+1)*2))+'║',end='')
            print(znakB*o,end='')
            print(znakA)
            delka-=1
            x+=1
    znak(zz)
    telo(znakA,znakB,o+2,1)
    print('╚'+'═'*(sirka-((o+1)*2))+'╝',end='')
    print(znakB*o,end='')
    print(znakA)
    return x

def stavba(i,l,z,y,x,zz,o,v,s,r,xx,rr):
        while s>0:#špička
            zz-=1
            znak(zz)
            print('/',end='')
            znak(o,l)
            print("\\")
            o+=2
            s-=2
            v+=1
        x=x-(v*2)
        while x>0:#tělo
            if x<5 or rr=='n':
                x-=1
                znak(zz)
                telo(i,l,y)
            else:
                x-=2+okno(y-2,int(((xx-(2*v))/10)*3),i,l,r,2,zz,y//5)
                znak(zz)
                telo(i,l,y)
                znak(zz)
                telo(i,l,y)
        b=zz
        p=0
        while v>0:#křidelka
            v-=1
            b-=1
            znak(b)
            print('/',end='')
            znak(p,l)
            telo(i,l,y,0)
            print(l*p,end='')
            print('\\')
            p+=1
        return (p)

def raketa():
    uu=otazka('v letu y/n\n')
    rr=otazka('okno y/n\n')
    volba_znaky=otazka('Zvolit znaky? y/n\n')
    if volba_znaky=='y':
        i=znaky('kraje: ')
        l=znaky('střed: ')
        if uu=='y':
            u=znaky('ohon: ')
        if rr=='y':
            r=znaky('výplň okna: ')
    else:
        i,l,r,u='I','-',' ','¤'        
    z=otazka_cisla('počet znaků:')
    y=otazka_cisla('šířka:')
    while y>(z/2):
        print('Neplatý vstup!Šířka musí být nanejvýš',int(z/2),'!')
        y=otazka_cisla('šířka:')
    x=otazka_cisla('výška:')
    while (y+2)>x:
        print('Neplatý vstup!Výška musí být alespoň',y+2,'!')
        x=otazka_cisla('výška:')
    if y%2==0:
        t=stavba(i,l,z,y,x,z//2,0,0,y,r,x,rr)
        if uu=='y':
            ohen((t*2)+y,z,u)
    else:
        print('-'*(z//2),end='¤\n')
        t=stavba(i,l,z,y,x,z//2,1,0,y-1,r,x,rr)
        if uu=='y':
            ohen(y+(t*2),z,u)
    opakovat()

def ohen(sirkao,sirka,znak1):
    z=(sirka-sirkao)//2+(sirka-sirkao)%2
    while sirkao>0:
        znak(z)
        znak(sirkao,znak1)
        print()
        sirkao-=4
        z+=2
        znak(z)
        znak(sirkao,znak1)
        print()
        sirkao-=2
        z+=1

def opakovat():
    x=otazka('Znova?y/n\n')
    if x=='y':
        os.system('cls')
        raketa()
    else:
        exit()

def otazka(y):
    while True:
        x=input(y)
        if x=='y' or x=='n':
            break
        print('Neplatný vstup!')
    return x

def otazka_cisla(y):
    while True:
        try:
            x=int(input(y))
            break
        except:
            print('Neplatný vstup! Pouze čísla!')
    return x

def znaky(y):
    while True:
        x=input(y)
        if len(x)==1:
            break
        print('Neplatný vstup!Pouze jeden znak!')
    return x

raketa()
