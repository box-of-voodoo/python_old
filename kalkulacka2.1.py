import os

def scitani():    
    x = float(input('číslo:'))
    y = float(input('číslo:'))
    print(x+y,)
    input('\n')
    vyber()
def odcitani():
    x = float(input('číslo:'))
    y = float(input('číslo:'))
    print(x-y)
    input('\n')
    vyber()
def nasobeni():
    x = float(input('číslo:'))
    y = float(input('číslo:'))
    print(x*y)
    input('\n')
    vyber()
def deleni():
    x=input('beze zbytku-1, se zbytkem-2\n')
    if x=='1':
        deleni1()
    elif x=='2':
        deleni2()
    else:
        print('zkus to znovu')
        deleni()
def deleni1():
    x = float(input('číslo:'))
    y = float(input('číslo:'))
    print(x/y)
    input('\n')
    vyber()
def deleni2():
    x = int(input('číslo:'))
    y = int(input('číslo:'))
    print(x//y,'(',x%y,')')
    input('\n')
    vyber()
def mocniny():
    x = float(input('mocněnec:'))
    y = float(input('mocnitel:'))
    print(x**y)
    input('\n')
    vyber()
def odmocniny():
    x = float(input('odmocněnec:'))
    y = float(input('odmocnitel:'))
    print(x**(1/y))
    input('\n')
    vyber()
def ciselne_soustavy():
    x=input('dec->x-1, x->dec-2\n')
    if x=='1':
        yyy=int(input('číslo:'))
        s=int(input('soustava:'))
        print(dec_to_s(yyy,s))        
    elif x=='2':
        yy=input('číslo:')
        ss=int(input('soustava:'))
        print(s_to_dec(yy,ss))
    else:
        print('zkus to znovu')
        ciselne_soustavy()
    input('\n')
    vyber()
def soust_pismena(x):
    if x == 10:
        x = 'A'
    elif x == 11:
        x = 'B'
    elif x == 12:
        x = 'C'
    elif x == 13:
        x = 'D'
    elif x == 14:
        x = 'E'
    elif x == 15:
        x = 'F'
    elif x == 16:
        x = 'G'
    elif x == 17:
        x = 'H'
    elif x == 18:
        x = 'I'
    elif x == 19:
        x = 'J'
    else:
        x = str(x)
    return x
def soust_pismena2(x):
    if x == 'A' or x == 'a':
        x = 10
    elif x == 'B' or x == 'b':
        x = 11
    elif x == 'C' or x == 'c':
        x = 12
    elif x == 'D' or x == 'd':
        x = 13
    elif x == 'E' or x == 'e':
        x = 14
    elif x == 'F' or x == 'f':
        x = 15
    elif x == 'G' or x == 'g':
        x = 16
    elif x == 'H' or x == 'h':
        x = 17
    elif x == 'I' or x == 'i':
        x = 18
    elif x == 'J' or x == 'j':
        x = 19
    else:
        x = int(x)
    return x
def dec_to_s(x,s):
    y=''
    while x>0:
        z=x%s
        z=soust_pismena(z)
        y=z+y
        x=x//s
    return y
def s_to_dec(x,s):
    y = yy = int(len(str(x)))
    d = 0
    while y>0:
        u = soust_pismena2(str(x)[yy-y])
        y = y-1
        v = u*s**y
        d = d+v
    return d
def vyber():
    os.system('cls')
    o=input('sčítání-1, odčítání-2, dělení-3, násobení-4, mocniny-5, odmocniny-6,\npřevody čiselných soustav-7, konec\n')
    if o=='1':
        scitani()
    elif o=='2':
        odcitani()
    elif o=='3':
        deleni()
    elif o=='4':
        nasobeni()
    elif o=='5':
        mocniny()
    elif o=='6':
        odmocniny()
    elif o=='7':
        ciselne_soustavy()
    elif o=='konec' or o=='end':
        quit()
    else:
        print('zkus to znovu')
        vyber()
print()
print('==============================================================================')
print()
vyber()
