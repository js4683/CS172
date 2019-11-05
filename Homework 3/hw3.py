#Author: Jashanpreet Singh
#Id: js4683
#Date: 05/17/19
#Purpose: CS172 Homework 3

#NOTE: The program requires two fingers for the drag to work on Macbooks and maybe Windows.

import pygame
#importing all the classes
from Ball import Ball
from Text import Text
from Block import Block
#intiailizing the environment in the game window
#Create a surface to draw on and set the name and color
pygame.init()
surface = pygame.display.set_mode((500, 500))#make the pygame window
pygame.display.set_caption("Homework 3")
#list for thing to be drawn
drawables = []
Blocks = [Block(400, 380), Block(380, 380), Block(360, 380), Block(400, 360), Block(380, 360), Block(360, 360),Block(400, 340), Block(380, 340), Block(360, 340)] #block objects
text = Text(0, 10)#text object
ball = Ball(7,390)#the ball
for block in Blocks:
    drawables.append(block)#adding the blocks to the drawables list
drawables.append(text) #adding the text to be drawn
#initializing the physic's variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0
xv = 0
yv = 0
finalx = 0
finaly = 0
#given variables
dt = 0.1
gravity = 10
rebound = 0.7
friction = 0.5
#score and the trigger for the ball
score = 0
launch = False

while True:#keeps the loop runnig
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q): #quits the game if the user presses q
            pygame.quit()
            exit()
        elif (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_r): #resets the position of the ball if the user presses r
            ball.setLocation((7,390))
            launch = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #Records the position on a mouse press
            mouseLoc = pygame.mouse.get_pos()
            x1= mouseLoc[0]
            y1 = mouseLoc[1]
            launch = False
        elif event.type == pygame.MOUSEBUTTONUP:#Records a position on mouse release and calculates velocity
                                                #Also triggers the ball to move
            mouseLoc = pygame.mouse.get_pos()
            x2 = mouseLoc[0]
            y2 = mouseLoc[1]
            xv = x2 - x1
            yv = (y2-y1) * -1
            launch = True
    if launch == True: #if trigger is True
        x,y = ball.getLocation() #get the location of the ball
        if y > 390:#if the ball is below the "ground", reverse the velcoity and bounce the ball
            yv = -rebound * yv
            xv = xv * friction
        else: #else the ball is affected by gravity
            yv = yv - gravity * dt
        finalx = x + (xv * dt)
        finaly = y - (yv * dt)
        if abs(yv) > 0.0001: #set the location of the ball
            ball.setLocation((int(finalx), int(finaly)))
    surface.fill((255,255,255))#Sets the screen to all white thus "erasing" all previous drawings
    pygame.draw.line(surface, (0,0,0), (0,400),(500,400)) #draws the "ground" line
    ball.draw(surface) #draws the ball
    for drawable in drawables: #to draw the items in the drawbles list
        if isinstance(drawable, Block): #check if the item is a block
            if ball.getRect().colliderect(drawable.getRect()) == True: #to check if there is collison
                drawables.remove(drawable) #remove the block from the list
                score += 1 #add one to the score for each block
            else:
                drawable.draw(surface) #draw the block
        else:
            drawable.draw(surface) #draw the item in the list
    text.setScore(score) #set the score
    pygame.display.update()#Updates the screen
    fpsclock = pygame.time.Clock()
    fpsclock.tick(30)#slows the game down so the animation is not too fast