import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((200,200))
gameDisplay.fill((10,10,10))

while True:
    for event in pygame.event.get():
        print(event)
