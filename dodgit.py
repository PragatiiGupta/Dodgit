import pygame
import time
import random
pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")

display_height = 600
display_width = 800
black = (0,0,0)
white = (255,255,255)
red = (220,0,0)
b_red = (255,0,0)
green = (0,200,0)
b_green = (0,255,0)
blue = (0,0,200)

bob_width = 70
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dodge it ")
clock = pygame.time.Clock()
img = pygame.image.load("bobb.png")
pause = False

def things_dodged(count) :
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score :"+str(count), True, green)
    gameDisplay.blit(text,(0,0))



def things(thingx, thingy, thingw, thingh, color) :
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    img1 = pygame.image.load("villian.png")
    #img2 = pygame.image.load("villi.png")
    gameDisplay.blit(img1,(thingx, thingy))
    #gameDisplay.blit(img2,(thingx, thingy))


def bob(x,y) :
    gameDisplay.blit(img,(x,y))
    
def text_objects(text,font) :
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

    
def message_display(text) :
    largetext = pygame.font.Font("freesansbold.ttf",100)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash() :

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largetext = pygame.font.Font("freesansbold.ttf",100)
    TextSurf, TextRect = text_objects("crashed !", largetext)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    
    
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
                


        button("RESTART",150,450,100,50,green,b_green,game_loop)
        button("QUIT",550,450,100,50,red,b_red,quitgame)
                     

        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,ic,ac,action = None) :
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + w > mouse[0] > x and y+h > mouse[1] > y :
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None :
            action()
    else :
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,smalltext)

    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def quitgame() :
    pygame.quit()
    quit()

def game_intro() :

    intro = True
    
    while intro :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largetext = pygame.font.Font("freesansbold.ttf",100)
        TextSurf, TextRect = text_objects("Dodged it !", largetext)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("GO",150,450,100,50,green,b_green,game_loop)
        button("QUIT",550,450,100,50,red,b_red,quitgame)
                     

        pygame.display.update()
        clock.tick(15)
def unpause() :
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
    
                         

def paused() :

    pygame.mixer.music.pause()
    largetext = pygame.font.Font("freesansbold.ttf",100)
    TextSurf, TextRect = text_objects("Paused !", largetext)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    
    
    while pause :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
                


        button("Continue",150,450,100,50,green,b_green,unpause)
        button("QUIT",550,450,100,50,red,b_red,quitgame)
                     

        pygame.display.update()
        clock.tick(15)

def game_loop() :
    global pause
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8) 
    x_change = 0
    thing_startx = random.randrange(0, display_width) 
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    thingCount = 1
    dodged = 0

    gameExit = False

    while not gameExit :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    x_change = -7
                if event.key == pygame.K_RIGHT :
                    x_change = 7
                if event.key == pygame.K_p :
                    pause = True
                    paused()
                    
            
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    x_change = 0

        x += x_change
                                   
            #print(event)
        gameDisplay.fill(white)
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        #things1(thing_startx, thing_starty, thing_width, thing_height, black)
        #things2(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        bob(x,y)
        things_dodged(dodged)
        if x > display_width - bob_width or x < 0 :
           crash()

        if thing_starty > display_height :
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged +=1
            thing_speed +=1
            #thing_width += (dodged * 1.2)
        if y < thing_starty+thing_height :
            #print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + bob_width > thing_startx and x + bob_width < thing_startx + thing_width :  
                #print('x crossover')
                crash()

        
        pygame.display.update()
        clock.tick(80)
        
game_intro()
game_loop()
pygame.quit()
quit()
