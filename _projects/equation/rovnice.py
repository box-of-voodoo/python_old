def quadratic(a,b,c,function=False,x=None,y=None,i=False):
    if function:
        if i:
            pass
        else:
            if y:
                return quadratic(a,b,c-y)
            if x:
                return (a*x**2+b*x+c)
    else:
        if i:
            pass
        else:
            d=b**2-4*a*c
            if d<0:
                return None
            elif d==0:
                return (-b/(2*a))
            else:
                return ((-b+d**(1/2))/(2*a),(-(b+d**(1/2))/(2*a)))


def linear(a,b,function=False,x=None,y=None,i=False):
    if function:
        if i:
            pass
        else:
            if y:
                return (y-b)/a
            if x:
                return (a*x+b)
    else:
        if i:
            pass
        else:
            return b/a

def fact(n):
    z=1
    for i in range(1,n+1):
        z*=i
    return z

def combinator_P(n,k):
    return fact(n)/fact(n-k)

def combinator_C(n,k):
    x=1
    for i in range(k+1,n+1):
        x*=i
    return x/fact(n-k)

def euklid_algoritmus(list_of_numb):
    x = list_of_numb.pop(0)
    while list_of_numb:
        x = euklid_algoritmus_for_2(x,list_of_numb.pop(0))
    return x

def euklid_algoritmus_for_2(x,y):
    if x<y: x,y = y,x
    while y != 0:
        x,y = y, x%y
    return x

def least_common_multiple(list_of_numb):
    y = list_of_numb.pop(0)
    while list_of_numb:
        z = list_of_numb.pop(0)
        y = (y*z)/euklid_algoritmus_for_2(y,z)
    return y
    


    
