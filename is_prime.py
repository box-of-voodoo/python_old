import os

def cls():
    os.system('cls')    

def is_prime(x):
    for i in range(2,int(x**(1/2))+1):
        if x%i==0:
            return False
    return x

def otazka_cisla(y):
    while True:
        try:
            x=int(input(y))
            break
        except:
            print('Neplatný vstup!Pouze čísla!')
    return x

def question_yn(question,wrong_answer):
    while True:
        x=input(question)
        if x in ['y','Y']:
            return True
        elif x in ['n','N']:
            return False
        print(wrong_answer)

def xx():
    x=otazka_cisla('Prvočísla do: ')
    a=list(range(2,x))
    print(', '.join([str(i) for i in list(filter(is_prime,a))]))
    z=question_yn('Znovu?y/n\n','Neplatný vstup!')
    if z:
        cls()
        xx()
    else:
        raise SystemExit
xx()
