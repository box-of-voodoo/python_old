from turtle import*

Screen()
t=Turtle()
bgcolor('gray')
x=0
t.up()
t.bk(0)
t.down()
t.pen(speed=0,shown=False)
t.color('red')
colo=['red','orange','yellow']
col=['green','blue','cyan']
t.color('green')
t.right(90)
t.pen(pensize=5)
t.fd(360)
t.bk(360)
t.pen(pensize=1)
for i in range(60):
    x+=3
    for z in range(3):
        t.color(col[z])
        t.circle(x,60)
        t.up()
        t.circle(x,240)
        t.down()
        t.circle(x,60)
        t.right(120)
    t.right(60)
t.right(30)
for i in range(60):
    x-=3
    for z in range(3):
        t.color(colo[z])
        t.circle(x,60)
        t.up()
        t.circle(x,240)
        t.down()
        t.circle(x,60)
        t.right(120)
    t.right(60)
t.st()
t.right(240)

