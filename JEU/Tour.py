import random
from BotBienBoosté import Bot
import tkinter as tk
from tkinter import Label
from tkinter import PhotoImage
import os
import copy
from ObjetsSuspicieux import Objet
from random import choice
from degats import Degats
import pygame

class Battle:
    def __init__(self,pokemons_dispo:list)-> None:
        self.equipe=[]
        self.poke_front=None
        self.robot= Bot(pokemons_dispo)
        self.run=True
        self.root = tk.Tk()
        self.root.title("Combat Pokémon")
        pygame.mixer.init()

        musique_path = "C:\\JEU\\battle_theme.mp3"
        pygame.mixer.music.load(musique_path)
        pygame.mixer.music.set_volume(0.15)  
        pygame.mixer.music.play(-1)  

        # dictionnaire de correspondance nom → fichier
        noms_fichiers = {
            "Scovillain 🔥🌱  ": "scovillain.png",
            "Sorbouboul ❄️  ": "sorbouboul.png",
            "Kravarech 🐲💧  ": "kravarech.png",
            "Farigiraf 🧠🔘  ": "farigiraf.png",
            "Pelage-Sablé 🟫⚡  ": "pelagesable.png",
            "Galvagon 🐲⚡  ": "galvagon.png",
            "Virevorreur 🌱👻  ": "virevorreur.png",
            "Pomdorochi 🐲🌱  ": "pomdorochi.png",
            "Sylveroy 🧠🌱  ": "sylveroy.png",
            "Amovénus 🦋🪶  ": "amovenus.png",
            "Pondralugon 🔩🐲  ": "pondralugon.png",
            "Saquedeneu 🌱  ": "saquedeneu.png",
            "Chartor 🔥  ": "chartor.png",
            "Pierroteknik 🔥👻  ": "pierroteknik.png",
            "Mite-de-Fer 🔥🫐  ": "mitedefer.png",
            "Balbalèze ❄️  ": "balbaleze.png",
            "Ire-Foudre ⚡  ": "irefoudre.png",
            "Békaglaçon ❄️  ": "bekaglacon.png",
            "Péchaminus 🫐👻  ": "pechaminus.png",
            "Tomberro 👻  ": "tomberro.png",
            "FerDeTer 🔩  ": "ferdeter.png",
            "Hydragla 💧  ": "hydragla.png",
            "Tutétékri 🟫👻  ": "tutetekri.png",
        }

        self.canvas = tk.Frame(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.images = {}
        dossier_images = "C:\\JEU\\images_pokemon"

        # Chargement dynamique des images
        for poke in pokemons_dispo:
            fichier = noms_fichiers.get(poke.nom)
            if fichier:
                try:
                    chemin = os.path.join(dossier_images, fichier)
                    self.images[poke.nom] = PhotoImage(file=chemin)
                    print(f"Image {poke.nom} chargée :", chemin)
                except Exception as e:
                    print(f"Erreur chargement image {poke.nom} :", e)
                    self.images[poke.nom] = None
            else:
                self.images[poke.nom] = None

        # Labels pour afficher les Pokémon
        self.label_poke_joueur = Label(self.canvas, text="", font=("Arial", 14), fg="green", bg="black")
        self.label_vs = Label(self.canvas, text=" VS ", font=("Arial", 20, "bold"), fg="red", bg="black")
        self.label_poke_bot = Label(self.canvas, text="", font=("Arial", 14), fg="blue", bg="black")

        self.label_poke_joueur.grid(row=0, column=0, padx=30, pady=20)
        self.label_vs.grid(row=0, column=1, padx=30, pady=20)
        self.label_poke_bot.grid(row=0, column=2, padx=30, pady=20)

        self.label_img_joueur = Label(self.canvas, bg="black")
        self.label_img_joueur.grid(row=1, column=0, padx=30, pady=10)

        self.label_img_bot = Label(self.canvas, bg="black")
        self.label_img_bot.grid(row=1, column=2, padx=30, pady=10)
        

    def update_gui(self) -> None:
        if self.poke_front:
            self.label_poke_joueur.config(text=f"{self.poke_front.nom}\nPV: {self.poke_front.pv}")
            if self.images.get(self.poke_front.nom):
                self.label_img_joueur.config(image=self.images[self.poke_front.nom])
                self.label_img_joueur.image = self.images[self.poke_front.nom]  # obligatoire pour Tkinter
        if self.robot.poke_front_bot:
            self.label_poke_bot.config(text=f"{self.robot.poke_front_bot.nom}\nPV: {self.robot.poke_front_bot.pv}")
            if self.images.get(self.robot.poke_front_bot.nom):
                self.label_img_bot.config(image=self.images[self.robot.poke_front_bot.nom])
                self.label_img_bot.image = self.images[self.robot.poke_front_bot.nom]
        self.root.update_idletasks()

    def cree_equipe(self,pokemons_dispo:list)-> None:
        while len(self.equipe)<6:
            for i, poke in enumerate(pokemons_dispo, start=1):
                print(f"{i}) {poke.nom}")
            poke_num=input(f"choisissez vos pokemons :")

            if poke_num in (str(i) for i in range(1,len(pokemons_dispo)+1)):
                self.equipe.append(copy.deepcopy(pokemons_dispo[int(poke_num)-1]))
                print(f'{pokemons_dispo[int(poke_num)-1].nom} ajouté')
            else:
                print('pokemon non disponible')
            
    def choix_pokemon(self)-> None:
        while self.poke_front==None:
            poke=int(input(
                f"choisissez un pokemon a envoyer au combat{[i.nom for i in self.equipe]}"))
            if poke in range (1,len(self.equipe)+1):
                self.poke_front=self.equipe[poke-1]
                self.equipe.remove(self.equipe[poke-1])

    def mort_poke_front(self)-> None:
        if self.poke_front.pv<=0 : 
            if self.equipe==[]:
                print("\033[1;31m Vous avez perdu (la honte)\033[0m")
                self.run=False
                return
            self.poke_front=None
            self.choix_pokemon()
    def executer_attaque(self, attaquant, defenseur, attaque)-> None:
        self.update_gui()
        self.root.update()
        couleur=None
        if attaquant==self.robot.poke_front_bot:
            couleur="\033[1;31m "
        else :
            couleur="\033[1;34m "
        if attaque==None:
            return
               # buff
        if attaque.buff:
            attaquant.buffs.append(attaque.buff)
            if attaque.buff == "defense":
                print( 
                    couleur + f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense augmente fortement !\033[0m")

            elif attaque.buff == "attspe":
                print( 
                    couleur + f"{attaquant.nom} utilise {attaque.nom} ! Son Attaque Spéciale augmente fortement !\033[0m")
            elif attaque.buff == "defense+defspe":
                print(
                    couleur + f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense et Défense Spéciale augmentent !\033[0m")
            elif attaque.buff == "rage":
                print(
                    couleur + f"{attaquant.nom} est pris de rage ! Son Attaque augmente énormément mais sa Défense baisse !\033[0m")
        # statut
        elif attaque.statut:
            defenseur.statut.append(attaque.statut)
            print(
                couleur + f"{attaquant.nom} utilise {attaque.nom} ! {defenseur.nom} est affecté par {attaque.statut} !\033[0m")

        else:
            # attaquedebase
            deg = Degats(attaquant, defenseur, attaque).degats()
            
            if deg != 0:   
                defenseur.pv -= deg
                print(couleur + f"{attaquant.nom} utilise {attaque.nom} ! Dégâts infligés : {deg}\033[0m")
            
        self.update_gui()
        self.root.update()
            
    def tour(self)-> None:
        """
        1 tour du joueur et du bot
        """
        self.mort_poke_front()
        attaque_joueur=None
        attaque_bot=None

        if self.poke_front:
            self.poke_front.apply_statut()
        if self.robot.poke_front_bot:
            self.robot.poke_front_bot.apply_statut()

        if not hasattr(self, 'bot_sent'):
            print(f"\nLe bot envoie {self.robot.poke_front_bot.nom} !")
            self.bot_sent = True  
        action = None
        while action is None:
            action = input("\033[1;32m Choisissez une action : 1) Attaquer , 2) Objet , 3) Changer , 4) Capituler : \033[0m")
            
            if action == '1':
                choix=None
                while choix==None:
                    choix = input(f"Choisissez une attaque : "
                                    f" 1) {self.poke_front.comp[0].nom} | "
                                    f" 2) {self.poke_front.comp[1].nom} | "
                                    f" 3) {self.poke_front.comp[2].nom} | "
                                    f" 4) {self.poke_front.comp[3].nom} : ")
                    if choix not in (str(a)for a in range(1,len(self.poke_front.comp)+1)):
                        choix=None
                        print("Entrez un chiffre entre 1 et 4")
                attaque_joueur=self.poke_front.comp[int(choix)-1]    


            elif action == '2': 
                objet_util=None
                while objet_util==None:
                    objet_util=input(f"""Choisissez un objet : 
                                  1) {self.objets[0].nom} : {self.objets[0].nombre}
                                  2) {self.objets[1].nom} : {self.objets[1].nombre}
                                  3) {self.objets[2].nom} : {self.objets[2].nombre}
                                  4) {self.objets[3].nom} : {self.objets[3].nombre}
                                  5) {self.objets[4].nom} : {self.objets[4].nombre}
                                  6) {self.objets[5].nom} : {self.objets[5].nombre}
                                  7) {self.objets[6].nom} : {self.objets[6].nombre}
                                  8) {self.objets[7].nom} : {self.objets[7].nombre}""")
                    
                    if objet_util not in (str(a)for a in range(1,len(self.objets)+1)):
                        objet_util=None
                        print("Entrez un chiffre entre 1 et 8")

                    else:
                        self.objets[int(objet_util)-1].use()
                        print(f"\033[1;32 Vous utilisez l'objet {self.objets[int(objet_util)-1].nom}\033[0m")
  
                

            elif action == '3': 
                if self.equipe==[]:
                    action=None
                else:
                    poke_change=None
                    while poke_change==None:
                        poke_change = input(f"\033[1;32 Choisissez un Pokémon : {[i.nom for i in self.equipe]} : \033[0m")

                        if poke_change not in (str(i) for i in range(1,len(self.equipe)+1) ) :
                            print(f"Entrez un chiffre entre 1 et {len(self.equipe)}")
                            poke_change=None
                        else:
                            self.equipe.append(self.poke_front)
                            self.poke_front = self.equipe[int(poke_change)-1]
                            self.equipe.remove(self.poke_front)
                            print(f"\033[1;32 Vous envoyez {self.poke_front.nom} !\033[0m")
   

            elif action == '4': 
                print("\033[1;32 Vous abandonnez...\033[0m")
                self.run=False

        
            else:
                print("Entrez un chiffre entre 1 et 4")
                action=None


        if self.robot.poke_front_bot.pv <= 20:
            tour_bot = random.choice(["Change", "Objet"])
        elif self.robot.poke_front_bot.pv < 50:
            tour_bot = random.choice(["Change"] + ["Attaque"] * 4)
        else:
            tour_bot = random.choice(["Change"] + ["Objet"] * 5 + ["Attaque"] * 10)


    
        if tour_bot=="Change":
            attaque_bot=None
            self.robot.choix_pokemon_bot()

        elif tour_bot=="Objet":
            attaque_bot=None
            objet_util=None
            while objet_util==None:
                objet_util=random.choice(self.objets_bot)
                if objet_util.nombre>0:
                    objet_util.use()
                else:
                    objet_util=None
                          
        elif tour_bot=="Attaque":
            if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False :
                attaque_bot = random.choice(self.robot.poke_front_bot.comp)
            else:
                attaque_bot=None

        #Si l'un n'attaque pas
        if attaque_joueur==None and attaque_bot!=None:
            self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)
        elif attaque_bot==None and attaque_joueur!=None:
            self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

        elif self.poke_front.vitesse >= (self.robot.poke_front_bot.vitesse if self.robot.poke_front_bot else 0):
            self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

            if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False:
                self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

        else:
            if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False:
                self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

            if self.poke_front.pv > 0 :
                self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)
            

    def main(self)-> None:
        Injection5G = Objet("Injection5G", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3,"Joueur")
        Glock = Objet("Glock", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,1,"Joueur")
        RouletteRusse = Objet("Roulette Russe", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,5,"Joueur")
        GamblingTime = Objet("Gambling Time", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,1,"Joueur")
        ProduitsDopants = Objet("Produits Dopants", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3,"Joueur")
        Eau = Objet("Eau", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3,"Joueur")
        CalmantsPourOurs = Objet("Calmants Pour Ours", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,2,"Joueur")
        ReposLong = Objet("Repos Long", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,4,"Joueur")
        self.objets = [Injection5G,Glock,RouletteRusse,GamblingTime,ProduitsDopants,Eau,CalmantsPourOurs,ReposLong]

        Injection5G_bot = Objet("Injection5G", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        Glock_bot = Objet("Glock", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        RouletteRusse_bot = Objet("Roulette Russe", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        GamblingTime_bot = Objet("Gambling Time", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        ProduitsDopants_bot = Objet("Produits Dopants", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        Eau_bot = Objet("Eau", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        CalmantsPourOurs_bot = Objet("Calmants Pour Ours", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        ReposLong_bot = Objet("Repos Long", self.robot.equipe_bot,self.equipe,self.robot.poke_front_bot,self.poke_front,3,"Bot")
        self.objets_bot = [Injection5G_bot,Glock_bot,RouletteRusse_bot,GamblingTime_bot,ProduitsDopants_bot,Eau_bot,CalmantsPourOurs_bot,ReposLong_bot]

        self.root.after(100, self.boucle_de_jeu())
        self.root.mainloop()

    def boucle_de_jeu(self)-> None:
        if self.run == True:
            if self.robot.poke_front_bot is None or self.robot.poke_front_bot.pv <= 0:
                if self.robot.poke_front_bot:  
                    print(f"{self.robot.poke_front_bot.nom} est K.O !")

                if self.robot.equipe_bot: 
                    self.robot.choix_pokemon_bot()
                    self.update_gui()
                    self.root.update()
                else:  
                    print("Bravo, vous avez gagné (heureusement, c'est un bot)")
                    self.root.quit()
                    return
            if self.robot.poke_front_bot is None or self.robot.poke_front_bot.pv <= 0:
                print(f"{self.robot.poke_front_bot.nom} est K.O !")
                self.robot.poke_front_bot = None  

                if self.robot.equipe_bot:  
                    print("Le Pokémon adverse est K.O ! Le bot en envoie un autre.")
                    self.robot.choix_pokemon_bot()
                else:  
                    print("Bravo, vous avez gagné (heureusement, c'est un bot)")
                    self.root.quit()
                    return
            
        self.tour()
        self.update_gui()
        self.root.update()

        self.root.after(100, self.boucle_de_jeu)





