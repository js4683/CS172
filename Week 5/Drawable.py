import pygame
import abc

class Drawable():
    __metaclass__ = abc.ABCMeta
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self,p):
        self.__x = p[0]
        self.__y = p[1]
    
    
    @abc.abstractmethod
    def draw(self,surface):
        pass

class Rectangle(Drawable):
    def __init__(self, x=0, y=0, width = 0, height = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
    
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getColor(self):
        return self.__color
    
    def setWidth(self, option):
        self.__width = option
    def setHeight(self, option):
        self.__height = option
    def setColor(self, option):
        self.__color = option
    
    def draw(self, surface):
        location = super().getLoc()
        pygame.draw.rect(surface, self.getColor(), [location[0], location[1], self.getWidth(), self.getHeight()])

class Snowflake(Drawable):
    def __init__(self, x= 0, y=0):
        super().__init__(x,y)
    
    def draw(self, surface):
        loc = super().getLoc()
        pygame.draw.line(surface, (255,255, 255), ((loc[0])-5, (loc[1])), ((loc[0])+5, (loc[1])))
        pygame.draw.line(surface, (255,255, 255), ((loc[0]), (loc[1])-5), ((loc[0]), (loc[1])+5))
        pygame.draw.line(surface, (255,255, 255), ((loc[0])-5, (loc[1])-5), ((loc[0])+5, (loc[1])+5))
        pygame.draw.line(surface, (255,255, 255), ((loc[0])-5, (loc[1])+5), ((loc[0])+5, (loc[1])-5))