#Author: Jashanpreet Singh
#Id: js4683
#Date: 05/17/19
#Purpose: CS172 Homework 3

import abc #needed to make an abstract class
import pygame #module used to make the game

class Drawable():
    __metaclass__ = abc.ABCMeta
    def __init__(self, x = 0, y = 0): #initialize the attributes
        self.__x = x
        self.__y = y
    
    def getLocation(self): #get the location of the object
        return (self.__x, self.__y)
    
    def setLocation(self, option): #set the location of the object
        self.__x = option[0]
        self.__y = option[1]
    
    @abc.abstractmethod #abstarct method for drawing the object
    def draw(self, surface):
        pass
    @abc.abstractmethod
    def getRect(self): ##abstarct method for getting a rectangle around the object for collision purpose
        pass


