from random import choice
from pokemon import *
from Tour import Battle

running=True
while running==True :
    choix=input("\033[1;33 voulez vous : 1) Jouer  2) Quitter \033[0m")

    if choix=='1' :
        pokemons_dispo = [
        Scovillain, Sorbouboul, Kravarech, Farigiraf, PelageSablé,
        Galvagon, Virevorreur, Pomdorochi, Sylveroy,
        Amovenus, Pondralugon, Saquedeneu, Chartor, Pierroteknik, MiteDeFer,
        Hydragla,Ferdeter,Tomberro ,Pechaminus ,Bekaglacon ,IreFoudre ,Balbaleze ,Tutétékri,Francois
        ]   
        main=Battle(pokemons_dispo)
        main.cree_equipe(pokemons_dispo)
        main.choix_pokemon()
        main.main()
    elif choix=='2' :
        une_derniere=input("\033[1;36 Une dernière partie ?   1) Oui   2) Non \033[0m")
        if une_derniere!='1':
            running=False
    else:
        print("\033[1;36 Bien essayé \033[0m")
        
