import random
from random import choice
import copy

class Bot:
    def __init__(self,pokemons_dispo:list)-> None:
        self.equipe_bot=[]
        for i in range (6) :
            self.equipe_bot.append(copy.deepcopy(random.choice(pokemons_dispo)))
        self.poke_front_bot=self.equipe_bot[0]
        self.equipe_bot.remove(self.poke_front_bot)

    def choix_pokemon_bot(self)-> None:
        if self.equipe_bot==[]:
            print("Bravo")
            return
        poke_front_avant=self.poke_front_bot

        self.poke_front_bot = self.equipe_bot[0]
        self.equipe_bot.remove(self.equipe_bot[0])

        if poke_front_avant.pv > 0:
            self.equipe_bot.append(poke_front_avant)
        
        print(f"Le bot rappelle {poke_front_avant.nom}et fait entrer {self.poke_front_bot.nom}")


