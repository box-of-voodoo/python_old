def ceas():
    s=input(':')
    o=""
    for x in s:
        if ord(x)>=ord('a') and ord(x)<=ord('z'):
            o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
        else:
            o+=x
    print (o)
