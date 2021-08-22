import pygame
import time
import random

pygame.init()

displayw,displayh = 800,600
white, black, red, green, blue = (255,255,255),(0,0,0),(255,0,0),(0,255,0),(0,0,255)

gameDisplay = pygame.display.set_mode((displayw,displayh))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)

pixAr[10][20] = green
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
pygame.draw.rect(gameDisplay, red, (400,400,50,25))
pygame.draw.circle(gameDisplay, white, (150,150),75)
pygame.draw.polygon(gameDisplay, green, ((25,75),(76,225),(250,375),(55,550),(600,500)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
