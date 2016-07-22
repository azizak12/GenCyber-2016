# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:37:58 2016

@author: student
"""
from random import randint 

class Pokemon: #make a cookie-cutter
    #Pokemon traits
    def __init__(self, oriName, oriType, orihp, oriMoves): #constructure/beginning of a pokemon
        self.name = oriName
        self.type = oriType
        self.hp = orihp
        self.cp = randint(1,85)
        self.moves = oriMoves
    
    def battle(self, myMove, opponent, opponentMove): #Fight
        #Make my move and announce it 
        print(self.name + " USED " + myMove)
        opponent.hp -= (self.moves[myMove] * self.cp)
        print(opponent.name + " HAS " + str(opponent.hp) + " HP LEFT!")
        #Check if they are alive
        if opponent.hp <= 0:
            print(opponent.name + " DIED!")
            print("YOU WIN!")
            return
        #Make their move
        print(opponent.name + " USED " + opponentMove)
        self.hp -= (opponent.moves[opponentMove] * opponent.cp)
        print(self.name + " HAS " + str(self.hp) + " HP LEFT!" )
        #Check if I am alive
        if self.hp <= 0:
            print(self.name + " DIED!")
            print("YOU LOSE!")
            return
        print("DRAW!")
        
        
eevee_moves = {"Swift": 10, "Dig": 20}
eevee = Pokemon("Eevee","Normal", 5, eevee_moves)


squats_moves = {"Squirt": 40, "Water Gun": 100}
squats = Pokemon("Squirtle", "Water", 90, squats_moves)


print("Vee CP: " + str(eevee.cp))
print("Squats CP: " + str(squats.cp))

eevee.battle("Dig", squats, "Squirt")

"""
turtle = Pokemon("Turdelz", "Water", 69, turtle_moves)
turtle_moves = 

dumbfish = Pokemon("DumbFish", "Water", 1, dumbfish_moves)
dumbfish_moves = 

bee = Pokemon("QueenBey", "Flying", 72, bee_moves)
bee_moves = 

snake = Pokemon("Hebi", "Grass", 90, snake_moves)
snake_moves = 

zombie = Pokemon("StankyZombie","Ghost",36, zombie_moves)
zombie_moves = 

esper = Pokemon("Esper", "Psychic", 85, esper_moves)
esper_moves = 

half-zombie = Pokemon ("Kabaneri", "Normal", 95, half-zombie_moves)
half-zombie_moves = 
"""
