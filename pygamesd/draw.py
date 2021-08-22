import pygame
from time import sleep

pygame.init()

displayw,displayh = 1500,800
white, black, red, green, blue = (255,255,255),(0,0,0),(200,0,0),(0,200,0),(0,0,200)
color = [white, red, green, blue]
fat = 15 #odd
colour = 0
if fat%2!=0:
    odd=1
else:
    odd=0
gameDisplay = pygame.display.set_mode((displayw,displayh))

clock = pygame.time.Clock()
pixAr = pygame.PixelArray(gameDisplay)
def clean():
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, color[colour], (0,displayh-(displayh//15),displayw,displayh//15))
clean()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[2] == 1:
        sleep(0.25)
        colour +=1
        if colour == len(color):
            colour = 0
        pygame.draw.rect(gameDisplay, color[colour], (0,displayh-(displayh//15),displayw,displayh//15))
    elif click[0] == 1:
        for i in range(-fat//2,fat//2+odd):
            for ii in range(-fat//2,fat//2+odd):
                if 0 < mouse[0]+i < 1500 and 0 < mouse[1]+i < 746:
                    pixAr[mouse[0]+i][mouse[1]+ii] = color[colour]
    elif click[1] == 1:
        clean()
    pygame.display.update()
    clock.tick()
