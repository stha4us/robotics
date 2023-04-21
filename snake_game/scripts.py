#Snake ate Apple

import pygame
import random

pygame.init()               #initializes the Game

white=(255,255,255)     #255 values of Red, Green and Blue
black=(0,0,0)
red=(255,0,0)           #we can use 4th parameter alpha i.e. degree of opaque
green=(0,155,0)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MyGame')

icon=pygame.image.load('apple.png')
pygame.display.set_icon(icon)           #standard icon pixel is 32*32
img=pygame.image.load('snakeHead.png')
appleimg=pygame.image.load('apple.png')


#pygame.display.update()      #can use pygame.didsplay.flip(), this updates the whole screen but using update and providing it with specific parameters we can update only specific areas on the screen




clock=pygame.time.Clock()       #Clock object is invoked

AppleThickness=30
block_size=20                   #size of snake
FPS=15
direction="right"

smallfont=pygame.font.SysFont("Courier New",25)       #initializing object, this returns font objext to variable named font
medfont=pygame.font.SysFont("Courier New",40)
largefont=pygame.font.SysFont("Courier New",60)


def pause():
    paused=True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
       
        clock.tick(5)

def score(score):
    text=smallfont.render("Score: "+str(score),True, black)
    gameDisplay.blit(text,[0,0])

    
def randAppleGen():
    randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY



def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Utsab Welcomes you!",green,-100,"large")
        message_to_screen("The Objective of the game is to eat apples",black,-30)
        message_to_screen("Avoid the Walls and running into own body!",black,10)
        message_to_screen("Enjoy!",black,50)
        message_to_screen("Press C to play, P to pause or Q to exit!",black,180)
        

        pygame.display.update()
        clock.tick(15)

def snake(block_size,snakelist):            #function parameter asking what is all these parameters
    if direction=="right":
        head=pygame.transform.rotate(img,270)
    if direction=="left":
        head=pygame.transform.rotate(img,90)
    if direction=="up":
        head=img
    if direction=="down":
        head=pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))       #(x,y pair coorrdinate position dont b confuse)
    for XnY in snakelist[:-1]:                                      #leave last element i.e head
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size]) # width*height
  
def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=largefont.render(text,True,color)
        
    
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="small"):      #displacement from center which is initialize 0 i.e. center so that we dont need to compulsarily pass 3rd para
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

##    screen_text=font.render(msg,True,color)     #font object used
##    gameDisplay.blit(screen_text,[display_width/2,display_height/2])

def gameLoop():
    global direction            #making direction a global variable so that we can modify it
    direction="right"
    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2      #head point or start coordinate at the middle

    lead_x_change=10
    lead_y_change=0

    snakeList=[]
    snakeLength=1
    
    randAppleX,randAppleY=randAppleGen()
    
    while not gameExit:


        if gameOver==True:
            message_to_screen("Game Over!",red, -30,
                              size="large")
            message_to_screen("Press C to Play again or Q to quit!",black,30,"medium")
            pygame.display.update()

        while gameOver==True:
            
            #gameDisplay.fill(green)
            

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                  gameExit=True                 #immataral if prefer gameExit or gameOver in 1st
                  gameOver=False
                
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=+block_size         #each movement is 2 pixel i.e.2 pixel at a time
                    lead_y_change=0
                    direction="right"
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                    direction="up"
                elif event.key==pygame.K_DOWN:
                    lead_y_change=+block_size
                    lead_x_change=0
                    direction="down"

                elif event.key==pygame.K_p:
                    pause()

        if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
            gameOver=True

            #if event.type==pygame.KEYUP:
             #   if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
              #      lead_x_change=0

        lead_x=lead_x+lead_x_change
        lead_y=lead_y+lead_y_change

        gameDisplay.fill(white)
        
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:           #analyze list up to last element i.e-1
            if eachSegment==snakeHead:
                gameOver=True
        snake(block_size,snakeList)

        score(snakeLength-1)
        
        pygame.display.update()



##        if lead_x>=randAppleX and lead_x<=randAppleX+AppleThickness:
##            if lead_y>=randAppleY and lead_y<=randAppleY+AppleThickness:
##                randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
##                randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0
##                snakeLength+=1

        if lead_x>randAppleX and lead_x<randAppleX+AppleThickness or lead_x+block_size>randAppleX and lead_x+block_size<randAppleX+AppleThickness:
            if lead_y>randAppleY and lead_y<randAppleY+AppleThickness or lead_y+block_size>randAppleY and lead_y+block_size<randAppleY+AppleThickness:
                randAppleX,randAppleY=randAppleGen()
                snakeLength+=1

                
        
        clock.tick(FPS)      #used for getting frames per seconds, primal rate, lower is slower
        
        #gameDisplay.fill(red, rect=[200,200,50,50]) #in coordinate position 200,200,draw a 50*50

        
    #message_to_screen("You Lose!",red)      #appears for some milliseconds only
    #pygame.display.update()
    #time.sleep(2)               #Just to hold

    pygame.quit()                #Quits the game
    quit()

game_intro()
gameLoop()
