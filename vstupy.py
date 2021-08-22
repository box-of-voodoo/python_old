def otazka_cisla(y):
    while True:
        x=input(y)
        try:
            if x=='exit':
                raise 'exit'
            else:
                x=int(x)#chyba!!!
        except:
            print('Neplatný vstup! Pouze čísla!')
        except 'exit':
            raise SystemExit
    return x
def opakovat(funkce):
    x=otazka('Znova?y/n\n')
    if x=='y':
        funkce()
    else:
        raise SystemExit
def question_yn(question,wrong_answer):
    while True:
        x=input(question)
        if x in ['y','n','Y','N']:
            break
        print(wrong_answer)
    return x
def otazka(y):
    while True:
        x=input(y)
        if x=='y' or x=='n':
            break
        print('Neplatný vstup!')
    return x
