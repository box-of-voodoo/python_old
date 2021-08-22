import pygame

pygame.init()

displayw, displayh = 600, 600
size = 600/8
black, white = (0,0,0),(255,255,255)

board = pygame.display.set_mode((displayw,displayh))
board.fill(black)
clock = pygame.time.Clock()

h,w = 0,0
for ii in range(8):
    for i in range(8):
        if (i%2==0 and ii%2==0) or (i%2==1 and ii%2==1):
            color = white
        else:
            color = black
        pygame.draw.rect(board, color, (h,w,size,size))
        h+=size
        pygame.display.update()
        clock.tick(60)
    w+=size
    h=0

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
