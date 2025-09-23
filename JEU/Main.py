from random import choice
from pokemon import *
from Tour import Battle

running=True
while running==True :
    choix=input("voulez vous : 1) Jouer  2) Quitter")

    if choix=='1' :
        pokemons_dispo = [
        Scovillain, Sorbouboul, Kravarech, Farigiraf, PelageSablé,
        Galvagon, Virevorreur, Pomdorochi, Sylveroy,
        Amovenus, Pondralugon, Saquedeneu, Chartor, Pierroteknik, MiteDeFer,
        Hydragla,Ferdeter,Tomberro ,Pechaminus ,Bekaglacon ,IreFoudre ,Balbaleze ,Tutétékri
        ]   
        main=Battle(pokemons_dispo)
        main.cree_equipe(pokemons_dispo)
        main.choix_pokemon()
        main.main()
    elif choix=='2' :
        une_derniere=input("Une dernière partie ?   1) Oui   2) Non")
        if une_derniere!='1':
            running=False
    else:
        print("Bien essayé")
        