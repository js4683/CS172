#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172


#This class defines a generic monster
#It doesn't actually DO anything.
#It just gives you a template for how a monster works.

#We can make any number of monsters and have them fight
#they just all need to INHERIT from this one so that work the same way

#Since this class is not intended to be used
#none of the methods do anything
#This class is cannot be used by itself.
import abc

class monster(metaclass=abc.ABCMeta):
    def __init__(self):
        return
    def __str__(self):
        return "Generic Monster Class"
    #Methods that need to be implemented
    #The description is printed at the start to give
    #additional details
    
    #Name the monster we are fighting
    #The description is printed at the start to give
    #additional details
    @abc.abstractmethod
    def getName(self):
        pass
        
    @abc.abstractmethod
    def getDescription(self):
        pass
        
    #Basic Attack Move
    #This will be the most common attack the monster makes
    #You are passed the monster you are fighting
    @abc.abstractmethod
    def basicAttack(self,enemy):
        pass
        
    #Print the name of the attack used
    @abc.abstractmethod
    def basicName(self):
        pass
        
    #Defense Move
    #This move is used less frequently to
    #let the monster defend itself
    @abc.abstractmethod
    def defenseAttack(self,enemy):
        pass
        
    #Print out the name of the attack used
    @abc.abstractmethod
    def defenseName(self):
        pass
        
    #Special Attack
    #This move is used less frequently
    #but is the most powerful move the monster has
    @abc.abstractmethod
    def specialAttack(self,enemy):
        pass
        
    @abc.abstractmethod
    def specialName(self):
        pass
        
    #Health Management
    #A monster at health <= 0 is unconscious
    #This returns the current health level
    @abc.abstractmethod
    def getHealth(self):
        pass
        
    #This function is used by the other monster to
    #either do damage (positive int) or heal (negative int)
    @abc.abstractmethod
    def doDamage(self,damage):
        pass
        
    #Reset Health for next match
    @abc.abstractmethod
    def resetHealth(self):
        pass

class Jashan(monster):
    def __init__(self):
        self.__name = "Jashan"
        self.__health = 100 
        self.__description = "He is a friendly person, but if you are on his bad side, you are done"
    
    def getName(self):
        return self.__name 
    
    def getDescription(self):
        return self.__description

    def basicAttack(self,enemy):
        return self.__name + "used"  + self.basicName()
        enemy.doDamage(20)

    def basicName(self):
        return "Turban"

    def defenseAttack(self,enemy):
        return self.__name + "used" + self.defenseName()
        enemy.doDamage(10)

    def defenseName(self):
        return "Release the turban"

    def specialAttack(self,enemy):
        self.__name + "used" + self.specialName() 
        enemy.doDamage(50)

    def specialName(self):
        return "Dancing"
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self,damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 100 
    
    def __str__(self):
        return self.__name + "at" + self.__health

    
class Hamza(monster):
    def __init__(self):
        self.__name = "Hamza"
        self.__health = 100
        self.__description = "Specialize in the drunk in fist"
    
    def getName(self):
        return self.__name 
    
    def getDescription(self):
        return self.__description

    def basicAttack(self,enemy):
        return self.__name + "used" + self.basicName()
        enemy.doDamage(35)

    def basicName(self):
        return "Smack"

    def defenseAttack(self,enemy):
        return self.__name + "used" + self.defenseName()
        enemy.doDamage(15)

    def defenseName(self):
        return "Block"

    def specialAttack(self,enemy):
        self.__name + "used" + self.specialName()
        enemy.doDamage(50)

    def specialName(self):
        return "Kick"
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self,damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 100
    
    def __str__(self):
        return self.__name + "at" + self.__health
    


