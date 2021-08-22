import pygame
from random import randint
import sys







pygame.init()
pygame.display.set_caption('Bouncing')

width,height = 800,600
size = width,height

white, black, red, green, blue = (255,255,255),(0,0,0),(255,0,0),(0,255,0),(0,0,255)
yellow, cyan, purple = (255,255,0),(0,255,255),(255,0,255)
orange,spring_green,violet = (255,128,0),(0,255,128),(128,0,255)
colors=[red,green,blue]
colours=[red,green,blue,yellow, cyan, purple,orange,spring_green,violet]

game_display = pygame.display.set_mode(size)
game_display.fill(black)

clock = pygame.time.Clock()
circles = []

class circle:
    def __init__(self,pos,radius,velocity,color,done=[False,0],index=0):
        self.radius = radius
        self.velocity = velocity
        self.pos = pos
        self.color = color
        self.done = done
        self.index = index

    def size_velo(self):
        return ((self.velocity[0]**2 + self.velocity[1]**2)**.5)
                
    def bouncing(self):
        for i in range(2):
            next_pos = self.pos[i] + self.velocity[i]

            if next_pos <= 0 + self.radius:
                self.pos[i] = 2*self.radius - next_pos
                self.velocity[i] = -self.velocity[i]

            elif next_pos >= size[i] - self.radius:
                self.pos[i] = 2*(size[i] - self.radius)- next_pos
                self.velocity[i] = - self.velocity[i]
                
    def move(self,objects):
##        if self.done:     #jen pro 2
##            self.done=False
##            return 0
        z=False
        for i in range(2):
            next_pos = self.pos[i] + self.velocity[i]
            if not(0 + self.radius < next_pos < size[i] - self.radius):
                z=True
        if z:
            self.collision(objects)
            self.bouncing()
        elif self.collision(objects):
            for i in range(2):
                self.pos[i]=self.pos[i]+self.velocity[i]

    def draw(self):
        pygame.draw.circle(game_display, self.color, (self.pos[0],self.pos[1]), self.radius)

    

    def collision(self,objects):#list
        
        for ob in objects:
            if self == ob: continue
            if self.done[0] and self.done[1] == objects.index(ob):
                self.pcolor(red,'---->>')
                self.done[0]=False
                continue

            dist=distance(self.pos[0]+self.velocity[0],
                          self.pos[1]+self.velocity[1],
                          ob.pos[0]+ob.velocity[0],
                          ob.pos[1]+ob.velocity[1])
            r=self.radius + ob.radius
            if dist <= r:
                self.pcolor(red,'--------><><>')#
                ve_xs,ve_xo = calcul_collision(self.velocity[0],ob.velocity[0])#+m+k
                ve_ys,ve_yo = calcul_collision(self.velocity[1],ob.velocity[1])

                self.velocity = [round(ve_xs),round(ve_ys)]
                ob.velocity = [round(ve_xo),round(ve_yo)]

                s_v = self.size_velo()
                counting=0
                #while dist < r:
                print(counting,dist,r)
                counting+=1
                for i in range(2):
                    self.pos[i] = self.pos[i] + self.velocity[i]

                s_v = ob.size_velo()
                for i in range(2):
                    ob.pos[i] = ob.pos[i] + ob.velocity[i]
                dist=distance(self.pos[0],self.pos[1],ob.pos[0],ob.pos[1])

                ob.done = [True,objects.index(self)]

                return False
            return True
    def pcolor(self,color,text):
        if color==self.color:
            print(text)
                
def calcul_collision(v1,v2,m1=1,m2=1,k=1):            
##    v=(m1*v1+m2*v2)/(m1+m2)
##    x=k*(v1-v2)/(m1+m2)
##    u1=v-(m2*x)
##    u2=v+(m1*x)

    u1 = (m1-k*m2)/(m1+m2)*v1 + (1+k)*m2/(m1+m2)*v2
    u2 = (1+k)*m1/(m1+m2)*v1 + (m2-k*m1)/(m1+m2)*v2

    return u1,u2

def distance(x1,x2,y1,y2):
    return ((x1-y1)**2 + (x2-y2)**2)**0.5

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

circles=[]

##for ii in range(3):
##    for i in range(3):
##        circles.append(circle([size[0]//2+i*20,size[1]//2+i*20],20,[i-1,ii-1],colors[i%3]))

for i in range(3):
    circles.append(circle([size[0]//2,size[1]//(i+1)],20,[3,(i*3)-4],colors[i%3],index=i))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
    click = pygame.mouse.get_pressed()
    while click[0] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()

    game_display.fill(black)
    for i in circles:
        i.move(circles)
        i.draw()

    pygame.display.update()

    clock.tick(60)
    

