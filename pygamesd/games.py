import pygame
import time
import random

pygame.init()

display_width,display_height = 800,600
fontcalibri='calibri.ttf'
car_width, car_height = 71, 55

black,white,red, green,blue = (0,0,0),(240,240,240),(200,0,0),(0,200,0),(0,0,200)
bred, bgreen = (255,0,0),(0,255,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Title')
clock = pygame.time.Clock()
paused = True

carimg = pygame.image.load('star.png')
carico = pygame.image.load('starico.png')
pygame.display.set_icon(carico)


def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('Score: '+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color,[thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def crash():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont(fontcalibri,50)
        TextSurf, TextRect = text_ojects("GAME OVER", largeText)
        TextRect.center = ((display_width/2),(250))
        gameDisplay.blit(TextSurf, TextRect)

        button("AGAIN!",200,300,100,50,green,bgreen,game_loop)
        button("EXIT",500,300,100,50,red,bred,exit_game)              

        pygame.display.update()
        clock.tick(15)

##def message_display(text):
##    largeText = pygame.font.SysFont(fontcalibri,40)
##    TextSurf, TextRect = text_ojects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##    pygame.display.update()
##    time.sleep(2)
##    
##    game_loop()

def button(msg,x,y,w,h,icolor,acolor,event):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolor,(x,y,w,h))
        if click[0] == 1:
            event()
    else:
        pygame.draw.rect(gameDisplay, icolor,(x,y,w,h))
            
    smallText = pygame.font.SysFont(fontcalibri,30)
    textSurf, textRect = text_ojects(msg, smallText)
    textRect.center = ((x+(w/2)),(y +(h/2)))
    gameDisplay.blit(textSurf,textRect)

def text_ojects(text, font):
    textSurface= font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def random_color():
    return (random.randint(0,200),random.randint(0,200),random.randint(0,200))
def random_red(green,blue):
    return (random.randint(100,255),green,blue)
def random_blue(red,green):
    return (red,green,random.randint(0,200))
def random_green(red,blue):
    return (red,random.randint(0,200),blue)
def exit_game():
    pygame.quit()
    raise SystemExit

def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont(fontcalibri,50)
        TextSurf, TextRect = text_ojects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(250))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",200,300,100,50,green,bgreen,game_loop)
        button("EXIT",500,300,100,50,red,bred,exit_game)              

        pygame.display.update()
        clock.tick(15)

def continue_p():
    global paused
    paused = False


def pause():
    global paused
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont(fontcalibri,50)
        TextSurf, TextRect = text_ojects("Paused", largeText)
        TextRect.center = ((display_width/2),(250))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue!",200,300,100,50,green,bgreen,continue_p)
        button("EXIT",500,300,100,50,red,bred,exit_game)              

        pygame.display.update()
        clock.tick(15)
    
def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change, y_change = 0,0

    thing_width = 80
    thing_height = thing_width
    thing_startx = []
    thing_startx.append(random.randrange(0,display_width-thing_width))
    thing_starty = -600
    thing_speed = 5
    thing_count = 1
    dodged = 0
    tick = 60
    background_color = white
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
            
            
        gameDisplay.fill(background_color)
        if dodged >10:
            things_color = random_color()
        else:
            things_color = blue
        for i in range(thing_count):
            things(thing_startx[i], thing_starty, thing_width, thing_height,things_color)
        thing_starty += thing_speed

        car(x,y)
        things_dodged(dodged)
        
        if x>display_width-car_width or x<0 or y<0 or y>display_height-car_height:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height

            for i in range(0,thing_count):
                thing_startx[0] = random.randrange(0,display_width-thing_width)

                
            dodged += 1
            if thing_speed<11 and (dodged<4 or (dodged>19 and dodged%2)):
                thing_speed += 1
            if thing_width<110 and dodged>3:
                thing_width += int(dodged*1.1)
            if dodged%3==0 and thing_count<3:
                thing_count +=1
                thing_startx.append(random.randrange(0,display_width-thing_width))
            if dodged>10 and tick<140:
                tick= int(tick*1.1)
        if dodged > 20:
            background_color = random_red(10,10)


        for i in range(thing_count):
            if y < thing_starty + thing_height < y + car_height or y < thing_starty < y + car_height:
                if thing_startx[i] < x < thing_startx[i] + thing_width or thing_startx[i] < x + car_width < thing_startx[i] + thing_width:
                    crash()
        
        pygame.display.update()
        clock.tick(tick)
game_intro()
game_loop()   
pygame.quit()
