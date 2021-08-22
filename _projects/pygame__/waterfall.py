import pygame as pg
import random as r
pg.init()
width,height = 800,600
white, black, red, green, blue = (255,255,255),(0,0,0),(255,0,0),(0,255,0),(0,0,255)
waterwin = pg.display.set_mode(width,height)
waterwin.fill(black)

pixels = pg.PixelArray(waterwin)

class water_pixel():
    def __init__(x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def move(self):
        x = self.x; y = self.y; vx = self.vx; y = self.vy #opss :(
        
        if pixels[x+vx,y+vy] != black:
            if r.randint(0,1)== 1:
                pixels[x+vx,y+vy+1] == blue
            else:
                pisels[x+vx][y+vy-1] == blue
        else:    
            pixels[x+vx,y+vy] = blue
            self.vx = 
        pixels[x][y] = black
        pg.waterwin.update()
        
