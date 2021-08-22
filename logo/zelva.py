from turtle import*

def kruhkruhu(polomer,polomer2,pocet):
    usek=360/pocet
    for i in range(pocet):
        t.color('purple')
        t.circle(polomer,usek)
        t.color('pink')
        t.begin_fill()
        t.circle(polomer2)
        t.end_fill()

def po30(y):
    for i in range(12):
        t.pen(shown=True)
        t.right(30)
        t.fd(y)
        t.bk(y)
        t.pen(shown=False)
        


Screen()
t=Turtle()
bgcolor('gray')
x=0
t.pen(speed=0,shown=False)
x=180
t.up()
t.fd(360)
t.down()
t.right(270)
for i in range(10):
    kruhkruhu(x*2,18,60)
    t.right(270)
    t.up()
    t.fd(36)
    t.down()
    t.left(270)
    x-=18
t.right(90)
t.st()
t.color('black')
for i in range(6):
    t.fd(360)
    t.bk(360)
    t.right(60)
t.right(30)
t.color('white')
for i in range(6):
    t.fd(360)
    t.bk(360)
    t.right(60)
t.left(30)
t.ht()
colo=['red','orange','yellow']
col=['green','blue','cyan']
for i in range(60):
    x+=3
    for z in range(3):
        t.color(col[z])
        t.circle(x)
        t.right(120)
    t.right(60)
z=x
y=x*2
t.right(30)
for i in range(60):
    x-=3
    for zz in range(3):
        t.color(colo[zz])
        t.circle(x)
        t.right(120)
    t.down()
    t.right(60)
t.left(30)
input()
raise SystemExit
