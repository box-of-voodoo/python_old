import pygame


pygame.init()

d_w,d_h = 800,600
white, black, red, green, blue = (255,255,255),(0,0,0),(255,0,0),(0,255,0),(0,0,255)

g_display = pygame.display.set_mode((d_w,d_h))
g_display.fill(black)

pixels = pygame.PixelArray(g_display)
class block():
    def __init__(x,y,z,leng,width,heigh):
        self.x = x
        self.y = y
        self.z = z
        self.leng = leng
        self.width = width
        self.heigh = height
    
def cube(x,y,l,w,h):
    for i in range(l):
        for ii in range(h):
            color = green
            if i in (0,l-1) or ii in (0,h-1):
                color = red
            pixels[i+x][ii+y] = color
    for i in range(w//2):
        for ii in range(h):
            color = green
            if i in (0,w//2-1) or ii in (0,h-1):
                color = red
            pixels[x+l+i][y+ii-i] = color
    for i in range(w//2):
        for ii in range(l):
            color = green
            if i in (0,w//2-1) or ii in (0,l-1):
                color = red
            pixels[x+l+i-ii-1][y-i] = color
            
    pygame.display.update()

cube(100,200,200,100,50)
cube(500,400,100,300,50)
cube(500,200,10,10,50)
cube(100,400,150,150,150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
