class pokus:
    def __init__(self,predmet,znamky):
        self.znamky=znamky
        self.predmet=predmet
        self.znamky_str=[[str(ii) for ii in i] for i in self.znamky]
        self.prumer=(sum(znamky[0])+2*sum(znamky[1])+3*sum(znamky[2])+4*sum(znamky[3])+5*sum(znamky[4]))/(len(znamky[0])+2*len(znamky[1])+3*len(znamky[2])+4*len(znamky[3])+5*len(znamky[4]))
    def __repr__(self):
        return self.predmet

    def zaokrouhleni(self):
        if self.prumer-int(self.prumer)<0.5:
            return int(self.prumer)
        else:
            return 1+int(self.prumer)

    def print_znamky(self):
        for i in range(5):
            print('Váha',str(i+1)+': ',end='')
            print(', '.join(self.znamky_str[i]))

#vstup + predmet ...
def otazka_znamky(y,x=None):
    while True:
        x=input(y)
        if x=='':
            return x
        elif x in ['1','2','3','4','5']:
            return int(x)
        else:
            print('Neplatný vstup! Pouze čísla od 1 do 5!')

def input_znamky(z):
    aa=[]
    while True:
        a=otazka_znamky(z)
        if a=='':
            break
        else:
            aa.append(a)
    return aa

def input_vahy(a=[]):
    for i in range(5):
        e=input_znamky('Váha '+str(i+1)+': ')
        a.append(e)
    return a

def novy_predmet(a=[]):
    while True:
        xp=input('Předmět:')
        if xp=='':
            break
        x=input_vahy()
        a.append(pokus(xp,x))
    return a

#ulozeni ...
def zapsat(a):
    soubor=open('znamky.txt','w')
    for i in a:
        soubor.write(i.predmet+'\n')
        for ii in i.znamky_str:
            soubor.write(','.join(ii)+'\n')
    soubor.close()    

def nacist_file():
    soubor=open('znamky.txt','r')
    a,b,c,d=[],[],[],[]
    while True:
        predmet=soubor.readline()[:-1]
        if predmet=='':
            break
        for i in range(5):
            znamky=soubor.readline()[:-1].split(',')
            d.append(znamky)
        b.append(predmet)
    soubor.close()
    d=str_to_int_in_list_in_list(d)
    return [b,d]

def str_to_int_in_list_in_list(l,z=[]):
    for i in l:
            x=[]
            for ii in i:
                if ii=='':
                    x=[]
                else:
                    ii=int(ii)
                    x.append(ii)
            z.append(x)
    return z

def nacist():
    predmety,znamky,a=nacist_file()[0],nacist_file()[1],[]
    for i in predmety:
        a.append(pokus(i,znamky[:5]))
        del(znamky[:5])
    return a

def smazat():
    soubor=open('znamky.txt','r+')
    soubor.seek(0)
    soubor.truncate()
    soubor.close()

#interface
def kecy(z=None,a=[]):
    if z==None:
        print('Vítejte!')
    while True:
        x=vstup('''1 - zadání nového předmětu
2 - načtení uložených dat
3 - výpis známek daného předmětu
4 - průměr daného předmětu
5 - uložení dat
6 - vymazání dat
7 - vymazání mezipaměti
0 - konec\n''')
        if x not in [str(i) for i in range(8)]:
            print ('!Neplatný výběr!')
        else:
            break
    if x=='1': #1
        a=novy_predmet(a)
        input()
        kecy(1,a)
    elif x=='2':
        a=nacist()
        print('Data byla načtena')
        kecy(1,a)
    elif x=='3':
        vyber_predmetu(a,vypis_znamek)
    elif x=='4':
        vyber_predmetu(a,prumer)
    elif x=='5':
        zapsat(a)
        print('Data byla uložena')
        kecy(1,a)
    elif x=='6':
        smazat()
        print('Všechna data byla odstraněna')
        kecy(1)
    elif x=='7':
        print('Mezipaměť smazána')
        vstup()
        kecy(1)

def vyber_predmetu(a,funkce):
    while True:
        for i in range(len(a)):
            print(i+1,'-',a[i])
        x=vstup()
        if x in[str(i) for i in range(len(a)+1)]:
            break
        print ('!Neplatný výběr!')
    print(int(x)-1)
    funkce(a,int(x)-1)
                       
def vypis_znamek(a,x):
    a[x].print_znamky()
    vstup()
    kecy(1,a)
    
def prumer(a,x):
    print('Průměr',a[x],'je',a[x].prumer)
    print('Zaokrouhleno na',a[x].zaokrouhleni())
    vstup()
    kecy(1,a)

def vstup(y=''):
    x=input(y)
    if x in ['0','end','konec']:
        z=input('Opravdu chcete tento program ukončit? y/n\n')
        if z=='n':
            kecy(z)
        raise SystemExit
    else:
        return x

kecy()

