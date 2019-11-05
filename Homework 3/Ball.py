#Author: Jashanpreet Singh
#Id: js4683
#Date: 05/17/19
#Purpose: CS172 Homework 3

from Drawable import Drawable #import the parent class
import pygame

class Ball(Drawable): #initialize the attributes
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
    
    def draw(self, surface): #method to draw the ball
        blue = (255,0,0)
        location = super().getLocation() #gets the location
        pygame.draw.circle(surface, blue,(location[0], location[1]), 10) #draws the ball
    
    def getRect(self): #method for a rectangle around the ball for collison testing
        location = super().getLocation() #gets the location of the ball
        return pygame.Rect(location[0], location[1], 10, 10) #makes an invisible rectangle
