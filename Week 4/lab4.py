from monster import Satyaa, Ibe
from monster2 import Jashan, Hamza
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    #first reset everyone's health!
    m1.resetHealth()
    m2.resetHealth()

    #next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None
    
    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial definder
    x = random.randint(0, 10)
    if x % 2 == 0:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
    
    
    print(attacker.getName()+" goes first.")
    #Loop until either 1 is unconscious or timeout
    while( m1.getHealth() > 0 and m2.getHealth() > 0):


        #Pick a number between 1 and 100
        move = random.randint(1,100)
        #It will be nice for output to record the damage done
        before_health=defender.getHealth()
        
        #for each of these options, apply the appropriate attack and 
        #print out who did what attack on whom
        if( move >=1 and move <= 60):
            #Attacker uses basic attack on defender
            attacker.basicAttack(defender)
            print(attacker.getName() + ' used ' + attacker.basicName())
            
        elif move>=61 and move <= 80:
            #Defend!
            defender.defenseAttack(attacker)
            print(defender.getName() + ' used ' + defender.defenseName())
        else:
            #Special Attack!
            attacker.specialAttack(defender)
            print(attacker.getName() + ' used ' + attacker.specialName())
        
        #Swap attacker and defender
        if attacker.getName() == m1.getName():
            attacker = m2
            defender = m1
        else:
            attacker = m1
            defender = m2
        
        #Print the names and healths after this round
        print(m1.getName()+ " is at " + str(m1.getHealth()))
        print(m2.getName() + " is at " + str(m2.getHealth()))
        print('--------------------')
    #Return who won
    if m1.getHealth() > m2.getHealth():
        return m1
    else:
        return m2

#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    
    random.seed(0)
    first = Ibe()
    second = Satyaa()
    third = Jashan()
    fourth = Hamza()
    
    winner = monster_battle(first,second)
    print("The winner of this battle is " + winner.getName())
    print('NEXT BATTLE!')
    print('')

    winner2 = monster_battle(third,fourth)
    print("The winner of this battle is " + winner2.getName())
    print('NEXT BATTLE!')
    print('')
    
    totalwinner = monster_battle(winner,winner2)
    print("The winner of the whole tournament is " + totalwinner.getName())
    print('Tournament Over!')