#Author: Jashanpreet Singh
#Id: js4683
#Date: 05/17/19
#Purpose: CS172 Homework 3

from Drawable import Drawable #importing the parent class
import pygame

class Text(Drawable): #class to create a text object
    def __init__(self, x=0, y=0, score=0): #intializes the attributes
        super().__init__(x, y)
        self.__score = score
        self.__font = pygame.font.Font("freesansbold.ttf", 15)
        self.__font2 = pygame.font.Font("freesansbold.ttf", 20)

    def setScore(self, option): #setter for the score
        self.__score = option

    def draw(self, surface): #method to make the actual text
        location = super().getLocation()
        color = (255, 255, 255)
        textSurface = self.__font.render('Score: ' + str(self.__score), True, (0,0,0)) #draws the text box at the top right hand corner for the score
        instrucSurface = self.__font2.render("Drag your mouse to launch the ball.", True, (0,0,0)) #draws the instructions
        instrucSurface2 = self.__font2.render("Press 'r' to reset the location of the ball.", True, (0,0,0)) #draws the instructions line 2
        instrucSurface3 = self.__font2.render("Press 'q' to quit the game.", True, (0,0,0)) #draws the instructuons line 3
        surface.blit(instrucSurface, (0, 440)) #for getting the text on the surface
        surface.blit(instrucSurface2, (0, 460)) #for getting the text on the surface
        surface.blit(instrucSurface3, (0, 480))#for getting the text on the surface
        surface.blit(textSurface, (location[0], location[1])) #for getting the score box on the surface
 
    def getRect(self): #method for getting a rectangle around the text for collision detetcion
        location = super().getLocation()
        return pygame.Rect(location[0], location[1], 5, 5)
