def ceasarova_sifra():
    x=["0","1","2","3","4","5","6","7","8","9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    p=list(input("písmena: "))
    c=(int(input("cislo: ")))%len(x)
    l=len(p)-1
    ll=0
    while ll<=l:
        y=x.index(p[ll])+c
        if y>=(len(x)):
            y=y-len(x)
        print(x[y],end='')
        ll+=1
    print()
def vyber():
    bb=input('again y/n')
    if bb=='y':
        ceasarova_sifra()
        vyber()
    else:
        raise SystemExit
vyber()
