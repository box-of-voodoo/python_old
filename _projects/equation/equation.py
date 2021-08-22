import math as m
operators=['(',')','+','-','*','/','^','log','ln']#log,ln není
##          0   1   2   3   4   5   6    7    8
##plus, minus, asterisk, slash, bracket_l, bracket_r 
###_+_____- ________*______/______(___________)_

#1->2->1->3->


def play(expression):                                 #1 
##    expression = input('Zadej příklad: ')  #+debiluvzdornost
    expression = in_list(expression)
    result = calculation(expression)
    print(result)


def in_list(expression):#                        #2
    expression = [i for i in expression]
    result, num ,pi = [], '', False
     
    for i in expression:
        if i.isdigit():
            num+=i

        elif num and i == '.':
            num+=i
            
        else:        
            if num:
                result.append(float(num))
                num=''
            if i == 'e':
                result.append(m.e)
                
            if i == 'i' and result[-1] == 'p':
                result[-1] = m.pi

            if (i == 'g'
                and result[-1] == 'o'
                and result[-2] == 'l'):

                result.pop(-1)
                result[-1] = 'log'

            if i == 'n' and result[-1] == 'l':
                result[-1] =' ln'
                
            else:
                result.append(i)
                
            #add: sin, etc.       
    if i.isdigit():
        result.append(float(num))
            
    return result


##def equat_or_calcul_or_func(expression):                 #3
##    equat = False
##    funct = False, False
##    only_numbers = True
##    variable = []
##
##    for i in expression:
##        if not (isinstance(i,float) or i in operators+['='] or i in variable):
##            variable.append(i)
##        if i == '=': equat = True
##        if i == 'x': funct = True, funct[1]
##        elif i == 'y': funct = funct[0], True; break
##
##    funct = funct[0] and funct[1]
##    if not equat:
##        if not variable:
##            return calculation(expression)#->4a
####        else:
####            pass
####    elif len(variable) == 1:
####        return equation(expression,variable)#->4b

        
def pos_of_bracket(expression, all_brackets=False):               #5
    opening, closing, brackets = [],[],[]
    for i,v in enumerate(expression):
        if v == '(':
            opening.append(i)
        if v == ')':
            closing.append(i)

    if opening == [] or closing == []:
        return False
    x = len(expression)
    if all_brackets:
        for i in closing:
            c_bk = i
            diff = help_pos_of_bracket(opening,c_bk,x)
            brackets.append([diff[1],c_bk])
        return brackets
    else:
        c_bk = closing.pop(0)
        diff = help_pos_of_bracket(opening,c_bk,x)
        return [diff[1],c_bk]

def help_pos_of_bracket(opening,c_bk,x):           #5.1
    diff = [x,0]
    for i in opening:
        if i < c_bk and diff[0] > (c_bk - i):
            diff = [(c_bk - i),i]
    return diff

                        
##################################################
#4a->(5->4a->6a->4a)->7a->4a->3->1
                
def calculation(expression):                #4a
    while True:
        bracket = pos_of_bracket(expression)
        if not bracket:
            break
        expression = remove_bracket_calcul(expression,bracket)
    return(only_numb(expression))





def remove_bracket_calcul(expression,brackets):           #6a
    bracket = expression[(brackets[0]+1):brackets[1]]
    result = only_numb(bracket)
    
    for i in range(brackets[1],brackets[0]-1,-1):
        expression.pop(i)
    expression.insert(brackets[0],result)
            
    return expression


def only_numb(side):                #7a
    multiply, power = 0,0
    for z in side:
        if z in ['*','/']:
            multiply +=1
        if z == '^':
            power +=1
    for i in range(power):
        for p,z in enumerate(side):
            if z == '^':
                break
        result = side[p-1]**side[p+1]
        side.pop(p+1);side.pop(p);side.pop(p-1)
        side.insert(p-1,result)
    for i in range(multiply):
        for p,z in enumerate(side):
            if z == '*':
                m = True
                break
            if z == '/':
                m = False
                break
        if m:
            result = side[p-1]*side[p+1]
            side.pop(p+1);side.pop(p);side.pop(p-1)
            side.insert(p-1,result)
        else:
            result = side[p-1]/side[p+1]
            side.pop(p+1);side.pop(p);side.pop(p-1)
            side.insert(p-1,result)

    result = side[0]
    for p,z in enumerate(side):
        if z == '+':
            result += side[p+1]
        elif z =='-':
            result -= side[p+1]
    return result
          

####################################################           

##def equation(equation):                     #4b
##    while True:
##        brackets = pos_of_bracket(equation, True)
##        if not brackets:
##            exponent = False
##            for i in equation:
##                if i in operators[6:]:
##                    exponent = True
##            if not exponent:
##                divisors = []
##                can_divine = []
##                for i,v in enumerate(equation):
##                    if v == '/':
##                        if isinstance(equation[i+1],float):
##                            can_divine.append(i)
##                        else:
##                            divisors.append(i)
##                for i in can_divine:
##                    equation[i] = '*'
##                    equation[i+1] = 1/equation[i+1]
##                for i in divisors:
##                    var = equation[i+1]
##                    for i,v in enumerate(equation):
##                        if v in operators[:5] + operators[6:]:
##                            continue
##                        elif #






                        
##########################
        
    #operat = side[bracket[
                    
                    
                
##    if brackets[0] != 0 and ((side[brackets[1]+1] in ['+','-'] or brackets[1] != len(side)-1)):
##            
##        if side[brackets[0]-1] == '+':
##
##            side.pop(brackets[0]);side.pop(brackets[1])
##            return side
##                
##        elif side[brackets[0]-1] == '+':
##
##            x = side[(brackets[0]+1):brackets[1]]
##            for ind,v in enumerate(x):
##                if v == '+':
##                    side[brackets[0]+1+ind] = '-'
##                if v == '-':
##                    side[brackets[0]+1+ind] = '+'
##            side.pop(brackets[0]);side.pop(brackets[1])
##            return side
##            
##        elif side[brackets[0]-1] == '*':
##            for pos,item in enumerate(side[(brackets[0]-2)::-1]):
##                if item == '+':
##                    break
##            wihtout_bracket = []#
##            for u in bracket:
##                if True:
##                    pass
                    
                
def lcm(list_of_numb):
    y = list_of_numb.pop(0)
    while list_of_numb:
        z = list_of_numb.pop(0)
        y = (y*z)/m.gcd(int(y),int(z))
    return y
    
    

    


