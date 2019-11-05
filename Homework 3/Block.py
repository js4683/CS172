#Author: Jashanpreet Singh
#Id: js4683
#Date: 05/17/19
#Purpose: CS172 Homework 3

from Drawable import Drawable #import the parent class
import pygame

class Block(Drawable): #creates a block object
    def __init__(self, x= 0, y=0): #initiliazes the attributes
        super().__init__(x, y)

    def draw(self,surface): #method to draw the block
        blue = (0,0,255) 
        location = super().getLocation() #gets the location to draw it in
        pygame.draw.rect(surface, blue, (location[0], location[1], 20, 20)) #draws the actual block
        pygame.draw.rect(surface, (0,0,0), (location[0], location[1], 20, 20), 1) #makes the black outline
    
    def getRect(self): #method for getting a rectangle around the block
        location = super().getLocation() #gets the location
        return pygame.Rect(location[0], location[1], 20, 20) #draws an invisible rectangle for collision testing