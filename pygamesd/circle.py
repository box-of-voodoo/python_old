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
pygame.draw.circle(gameDisplay, white, (75,75),75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
