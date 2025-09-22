import random
from random import choice
import copy
import tkinter as tk
from tkinter import Label
from tkinter import PhotoImage
import os

class Pokemon():
    def __init__(self,nom,type,pv,vitesse,res,res2,faib,faib2,immu,attaque,defense,attspe,defspe,comp):
        self.nom = nom
        self.type = type
        self.pv = pv
        self.vitesse = vitesse
        self.res = res
        self.res2 = res2
        self.immu = immu
        self.faib = faib
        self.faib2 = faib2     
        self.attaque = attaque
        self.defense = defense
        self.attspe = attspe
        self.defspe = defspe
        self.comp = comp
        self.statut = []
        self.buffs = []
        self.cant_attack = False


    def __str__(self):
        return (f"Pokémon: {self.nom}\n"
                f"Type(s): {self.type}, {self.faib} (Faiblesses), {self.res} (Résistances)\n"
                f"PV: {self.pv}\n"
                f"Vitesse: {self.vitesse}\n"
                f"Attaque: {self.attaque} | Défense: {self.defense}\n"
                f"Attaque Spéciale: {self.attspe} | Défense Spéciale: {self.defspe}\n"
                f"Compétences: {', '.join([c.nom for c in self.comp])}")

    def apply_statut(self):
        import random
        if "Poison" in self.statut:
            self.pv -= max(1, self.pv // 8)
            print(f"{self.nom} subit des dégâts de Poison ! PV restant : {self.pv}")
            if random.randint(1, 100) <= 10: 
                self.statut.remove("Poison")
                print(f"{self.nom} n'est plus empoisonné !")

        if "Burn" in self.statut:
            self.pv -= max(1, self.pv // 16)
            print(f"{self.nom} subit des dégâts de Brûlure ! PV restant : {self.pv}")
            if random.randint(1, 100) <= 10:
                self.statut.remove("Burn")
                print(f"{self.nom} n'est plus brûlé !")

        if "Gel" in self.statut:
            if random.randint(1, 100) <= 25:
                self.statut.remove("Gel")
                print(f"{self.nom} n'est plus Gelé !")
                self.cant_attack=False
            else:
                print(f"{self.nom} est gelé et ne peut pas attaquer !")
                self.cant_attack=True

        if "Comptine" in self.statut:
            if random.randint(1, 100) <= 25:
                self.statut.remove("Comptine")
                print(f"{self.nom} n'est plus endormi !")
                self.cant_attack=False
            else:
                print(f"{self.nom} est endormi et ne peut pas attaquer !")
                self.cant_attack=True

        if "Paralysie" in self.statut:
            if random.randint(1, 100) <= 20:
                self.statut.remove("Paralysie")
                print(f"{self.nom} n'est plus paralysé !")
                self.cant_attack=False
            else:
                print(f"{self.nom} est paralysé, sa vitesse est réduite et il risque de ne pas attaquer !")
                self.cant_attack=True
        #buff
        if "defense" in self.buffs:
            self.defense *= 1.5

        if "attspe" in self.buffs:
            self.attspe *= 2

        if "defense+defspe" in self.buffs:
            self.defense *= 1.25
            self.defspe *= 1.25

        if "rage" in self.buffs:
            self.attaque *= 2
            self.defense /= 2


class Attaque():
    def __init__(self,nom,type,statut,special,haut_crit,puissance,proba,precision,prio,PP,buff=None):
        self.nom=nom
        self.type=type
        self.statut=statut
        self.special=special
        self.haut_crit=haut_crit
        self.puissance=puissance
        self.proba=proba
        self.precision=precision
        self.prio=prio
        self.PP=PP
        self.buff=buff

class Degats:
    def __init__(self,poke_att,poke_def,attaque):
        self.poke_att=poke_att
        self.poke_def=poke_def
        self.attaque=attaque

    def degats(self):#rajouter les priorités
        vitesse=self.poke_att.vitesse
        if "Paralysie" in self.poke_att.statut:  
            vitesse = vitesse / 4 
            if random.randint(1, 100) <= 75:
                print(f"{self.poke_att.nom} est paralysé il ne peut pas attaquer !")
                return 0
        if "Comptine" in self.poke_att.statut:   
            if random.randint(1,100) <= 100:
                print(f"{self.poke_att.nom} est endormi il ne pourra pas attaquer !")
                return 0
        if "Gel" in self.poke_att.statut:   
            if random.randint(1,100) <= 100:
                print(f"{self.poke_att.nom} est gelé il ne pourra pas attaquer !")
                return 0
        if self.attaque.puissance == 0:
            return 0
        if self.attaque.type in self.poke_def.immu:
            return 0
        
        Att = self.poke_att.attaque if self.attaque.special == False else self.poke_att.attspe
        Def = self.poke_def.defense if self.attaque.special == False else self.poke_def.defspe
        Pui = self.attaque.puissance
        STAB=1.5 if self.attaque.type in self.poke_att.type else 1
        
        if self.attaque.type in self.poke_def.faib2:
            Type=4
        elif self.attaque.type in self.poke_def.faib:
            Type=2 
        elif self.attaque.type in self.poke_def.res:
            Type=0.5 
        elif self.attaque.type in self.poke_def.res2:
            Type=0.25 
        else :
            Type=1
        
        T=int(vitesse/2)
        if self.attaque.haut_crit==True:
            T=T*8
        if T>255:
            T=255

        if random.randint(0,255)<T :
            Crit= 1.4 
        else:
            Crit= 1
        
        Obj=1  #pass

        CM = STAB * Type * Crit * Obj * random.uniform(0.85,1) # + mod de terrain
        Compensateur_Niveaux = 7
        Degats=((((Att*Pui)/Def)/50)+2)*CM*Compensateur_Niveaux

        #Vol de Vie,Protection
        #Les pokemon perdent de la vie en attaquant ( malediction , destruction,une autre)
        #PP
        
        if self.attaque.statut != False:
            if self.attaque.statut in ("Poison","Burn","Gel","Paralysie","Comptine") :
                if random.randint(1,100) <= self.attaque.proba:
                    self.poke_def.statut.append(self.attaque.statut)
        if self.attaque.buff != None:
             if random.randint(1,100) <= self.attaque.proba:
                self.poke_att.buffs.append(self.attaque.buff)

        return int(Degats)


class Bot:
    def __init__(self,pokemons_dispo):
        self.equipe_bot=[]
        for i in range (1) :
            self.equipe_bot.append(copy.deepcopy(choice(pokemons_dispo)))
        self.poke_front_bot=self.equipe_bot[0]
        self.equipe_bot.remove(self.poke_front_bot)

    def choix_pokemon_bot(self):
        self.poke_front_bot = copy.deepcopy(choice(self.equipe_bot))
        self.equipe_bot.remove(self.poke_front_bot)

class Objet:
    def __init__(self, nom, equipe, equipe_adv, poke, poke_adv, nombre):
        self.nom = nom
        self.equipe = equipe
        self.equipe_adv = equipe_adv
        self.poke = poke
        self.poke_adv = poke_adv
        self.nombre = nombre

    def use(self):
        if self.nom not in ("Injection5G", "Glock", "Roulette Russe", "Gambling Time", "Produits Dopants", "Eau", "Calmants Pour Ours", "Repos Long"):
            return
        if self.nombre > 1:
            self.nombre -= 1
            if self.nom == "Injection5G":
                self.poke.statut = []
                print('ILS NOUS CONTROLENT (votre pokemon perd tout ses effets)')
            elif self.nom == "Glock":
                self.poke_adv.hp = 0
                print(
                    "Rapide et Efficace (le pokemon adverse n'a pas survecu a cette balle)")
            elif self.nom == "Roulette Russe":
                a = random.randint(1, 2)
                if a == 1:
                    self.poke.pv = 0
                    print("тебе не повезло")
                else:
                    self.poke_adv.pv = 0
                    print("тебе повезло")

            elif self.nom == "Gambling Time":
                i = random.randint(-20,20)
                self.poke.pv+=i  
                if i>=0:             
                    print(f"Votre pokemon gagne {i}pv")
                else :
                    print(f"Votre pokemon perd {-i} pv")
            elif self.nom == "Produits Dopants":
                self.poke.pv += 20
                self.poke.attaque += 10
                self.poke.attspe += 20
                print(f"+20pv, +10att, +10att spé, c'est légal ça?     vous avez maintenant {self.poke.pv}pv")
            elif self.nom == "Eau":
                print("Votre pokemon est hydraté, c'est super mais a quoi ca sert ?")
                # rien
            elif self.nom == "Calmants Pour Ours":
                if "Comptine" not in self.poke_adv.statut:
                    self.poke_adv.statut.append("Comptine")
                print("Votre pokepmon est boooriiiing, le pokemon adverse fait dodo")
            elif self.nom == "Repos Long":
                for i in self.poke.comp:
                    i.PP += 10
                self.poke.pv += 20
                if "Comptine" not in self.poke.statut:
                    self.poke.statut.append("Comptine")
                print(f"Mimimimimimimimimi (vous dermez et recuperez 10PP et 20pv et vous avez {self.poke.pv}pv)")


class Battle:
    def __init__(self, pokemons_dispo):
        self.equipe = []
        self.poke_front = None
        self.robot = Bot(pokemons_dispo)
        self.root = tk.Tk()
        self.root.title("Combat Pokémon")

        # dictionnaire de correspondance nom → fichier
        noms_fichiers = {
            "Scovillain🔥🌱": "scovillain.png",
            "Sorbouboul❄️": "sorbouboul.png",
            "Kravarech🐲💧": "kravarech.png",
            "Farigiraf🧠🔘": "farigiraf.png",
            "Pelage-Sablé🟫⚡": "pelagesable.png",
            "Galvagon🐲⚡": "galvagon.png",
            "Virevorreur🌱👻": "virevorreur.png",
            "Pomdorochi🐲🌱": "pomdorochi.png",
            "Sylveroy🧠🌱": "sylveroy.png",
            "Amovénus🦋🪶": "amovenus.png",
            "Pondralugon🔩🐲": "pondralugon.png",
            "Saquedeneu🌱": "saquedeneu.png",
            "Chartor🔥": "chartor.png",
            "Pierroteknik🔥👻": "pierroteknik.png",
            "Mite-de-Fer🔥🫐": "mitedefer.png",
            "Balbalèze❄️": "balbaleze.png",
            "Ire-Foudre⚡": "irefoudre.png",
            "Békaglaçon❄️": "bekaglacon.png",
            "Péchaminus🫐👻": "pechaminus.png",
            "Tomberro👻": "tomberro.png",
            "FerDeTer🔩": "ferdeter.png",
            "Hydragla💧": "hydragla.png",
            "Tutétékri🟫👻": "tutetekri.png",
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
        

    def update_gui(self):
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
    def cree_equipe(self,pokemons_dispo):
        while len(self.equipe)<1:
            poke_num=int(input(f"choisissez vos pokemons :" 
                        f"{[(i+1, pokemons_dispo[i].nom) for i in range (0,len(pokemons_dispo))]}"))
            if poke_num in range (1,len(pokemons_dispo)+1):
                self.equipe.append(copy.deepcopy(pokemons_dispo[poke_num-1]))
                print('pokemon ajouté')
            else:
                print('pokemon non disponible')
            
    def choix_pokemon(self):
        while self.poke_front==None:
            poke=int(input(
                f"choisissez un pokemon a envoyer au combat{[i.nom for i in self.equipe]}"))
            if poke in range (1,len(self.equipe)+1):
                self.poke_front=self.equipe[poke-1]
                self.equipe.remove(self.equipe[poke-1])

    def mort_poke_front(self):
        if self.poke_front.pv<=0 : 
            self.poke_front=None
            self.choix_pokemon()
    def executer_attaque(self, attaquant, defenseur, attaque):
        if attaque.puissance == 0:
            # buff
            if attaque.buff:
                attaquant.buffs.append(attaque.buff)
                if attaque.buff == "defense":
                    print( 
                        f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense augmente fortement !")

                elif attaque.buff == "attspe":
                    print( 
                        f"{attaquant.nom} utilise {attaque.nom} ! Son Attaque Spéciale augmente fortement !")
                elif attaque.buff == "defense+defspe":
                    print(
                        f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense et Défense Spéciale augmentent !")
                elif attaque.buff == "rage":
                    print(
                        f"{attaquant.nom} est pris de rage ! Son Attaque augmente énormément mais sa Défense baisse !")
            # statut
            elif attaque.statut:
                defenseur.statut.append(attaque.statut)
                print(
                    f"{attaquant.nom} utilise {attaque.nom} ! {defenseur.nom} est affecté par {attaque.statut} !")
        else:
            # attaquedebase
            deg = Degats(attaquant, defenseur, attaque).degats()
            
            if deg != 0:   
                defenseur.pv -= deg
                print(f"{attaquant.nom} utilise {attaque.nom} ! Dégâts infligés : {deg}")
            self.update_gui()
                


    def tour(self):
        self.mort_poke_front()

        if self.poke_front:
            self.poke_front.apply_statut()
        if self.robot.poke_front_bot:
            self.robot.poke_front_bot.apply_statut()

        if not hasattr(self, 'bot_sent'):
            print(f"\nLe bot envoie {self.robot.poke_front_bot.nom} !")
            self.bot_sent = True  
        action = None
        while action is None:
            action = int(input(
                "choisissez une action : 1) Attaquer , 2) Objet , 3) Changer , 4) Capituler : "))

            if action == 1:
                choix=None
                while choix==None:
                    choix = input(f"Choisissez une attaque : "
                                    f"1) {self.poke_front.comp[0].nom} | "
                                    f"2) {self.poke_front.comp[1].nom} | "
                                    f"3) {self.poke_front.comp[2].nom} | "
                                    f"4) {self.poke_front.comp[3].nom} : ")
                    
                    if choix not in (str(a)for a in range(1,len(self.poke_front.comp))):
                        choix=None
                        print("Entrez un chiffre entre 1 et 4")

                    else:
                        if self.poke_front.cant_attack==False:
                            attaque_joueur = self.poke_front.comp[int(choix)-1]
                        else:
                            print("vous ne pouvez pas")


                        if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False :
                            attaque_bot = choice(self.robot.poke_front_bot.comp)


                        if self.poke_front.vitesse >= (self.robot.poke_front_bot.vitesse if self.robot.poke_front_bot else 0):
                            self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

                            if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False:
                                print(f"Bot : {self.robot.poke_front_bot.nom}, utilise {attaque_bot.nom} !")
                                self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

                        else:
                            if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0 and self.robot.poke_front_bot.cant_attack==False:
                                print(f"Bot : {self.robot.poke_front_bot.nom}, utilise {attaque_bot.nom} !")
                                self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

                            if self.poke_front.pv > 0:
                                self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

            elif action == 2: 
                objet_util=None
                while objet_util==None:
                    objet_util=input(f"Choisissez un objet : "
                                  f"1) {self.objets[0].nom} | "
                                  f"2) {self.objets[1].nom} | "
                                  f"3) {self.objets[2].nom} | "
                                  f"4) {self.objets[3].nom} | "
                                  f"5) {self.objets[4].nom} | "
                                  f"6) {self.objets[5].nom} | "
                                  f"7) {self.objets[6].nom} | "
                                  f"8) {self.objets[7].nom} : ")
                    
                    if objet_util not in (str(a)for a in range(1,len(self.objets)+1)):
                        objet_util=None
                        print("Entrez un chiffre entre 1 et 8")

                    elif self.objets[int(objet_util)-1].nombre<1:
                        objet_util=None
                        print("Vous n'avez plus cet objet")

                    else:
                        self.objets[int(objet_util)-1].use()


            elif action == 3: 
                poke_change=None
                while poke_change==None:
                    poke_change = input(f"Choisissez un Pokémon : {[i.nom for i in self.equipe]} : ")

                    if objet_util not in (str(a)for a in range(1,len(self.equipe))):
                        print(f"Entrez un chiffre entre 1 et {len(self.equipe)}")
                        poke_change=None
                    else:
                        self.equipe.append(self.poke_front)
                        self.poke_front = self.equipe[poke_change-1]
                        self.equipe.remove(self.poke_front)
                        print(f"Vous envoyez {self.poke_front.nom} !")

            elif action == 4: 
                print("Vous abandonnez...")
                global running
                running = False
                return

    def main(self):

        Injection5G = Objet("Injection5G", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3)
        Glock = Objet("Glock", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,1)
        RouletteRusse = Objet("Roulette Russe", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,5)
        GamblingTime = Objet("Gambling Time", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,1)
        ProduitsDopants = Objet("Produits Dopants", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3)
        Eau = Objet("Eau", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,3)
        CalmantsPourOurs = Objet("Calmants Pour Ours", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,2)
        ReposLong = Objet("Repos Long", self.equipe,self.robot.equipe_bot,self.poke_front,self.robot.poke_front_bot,4)
        self.objets = [Injection5G,Glock,RouletteRusse,GamblingTime,ProduitsDopants,Eau,CalmantsPourOurs,ReposLong]


        self.root.after(100, self.boucle_de_jeu)
        self.root.mainloop()
    def boucle_de_jeu(self):
        # Vérif défaite
        if (self.equipe == [] and self.poke_front is None) or (self.poke_front and self.poke_front.pv <= 0):
            print("Vous avez perdu (la honte)")
            self.root.quit()
            return

        # Vérif victoire
        if (self.robot.equipe_bot == [] and self.robot.poke_front_bot is None) or (self.robot.poke_front_bot and self.robot.poke_front_bot.pv <= 0):
            print("Bravo, vous avez gagné (heureusement, c'est un bot)")
            self.root.quit()
            return

        # sinon : jouer un tour
        self.tour()

        # replanifier la suite
        self.root.after(100, self.boucle_de_jeu)


# ajouter : proba,precision,prio,PP

#dans lordre :nom,type,statut,special,haut_crit,puissance,proba,precision,prio,PP,buff=None
Habanerage = Attaque("Habanerage🌱","Plante","Gel", False, False, 0, 100, 100, False, 24)
LanceFlamme = Attaque("LanceFlamme🔥","Feu", None, True, False, 90, 100, 100, False, 24)
Surchauffe = Attaque("Surchauffe🔥","Feu", None, True, False, 130, 100, 90, False, 5)
CanonGraine = Attaque("CanonGraine🌱","Plante", None, False, False, 80, 100, 100, False, 24)

Blizzard = Attaque("Blizzard❄️","Glace", None, True, False, 110, 100, 70, False, 5)
Stalactite = Attaque("Stalactite❄️","Glace", None, False, False, 25, 100, 100, False, 30)
DansePluie = Attaque("DansePluie💧","Eau", "Pluie", True, False, 0, 100, 100, False, 5)
Destruction = Attaque("Destruction🔘","Normal", None, False, False, 200, 100, 100, False, 5)

Toxik=Attaque("Toxik🫐","Poison","Poison", False, False, 0, 100, 100, False, 16)
Acidarmure = Attaque("Acidarmure🫐","Poison", "Acidarmure", True, False, 0, 100, 100, False, 20,buff="defense")
Ouragan = Attaque("Ouragan🪶","Vol", None, True, False, 40, 100, 100, False, 20)
DracoMeteore = Attaque("DracoMeteore🐲","Dragon", None, True, False, 130, 100, 90, False, 5)

Psyko = Attaque("Psyko🧠","Psy", None, True, False, 90, 100, 100, False, 10)
Machination = Attaque("Machination👤","Ténèbres", "Machination", True, False, 0, 100, 100, False, 20, buff="attspe")
DissonancePsy = Attaque("DissonancePsy🧠","Psy", None, True, False, 75, 100, 100, False, 10)
Gravite = Attaque("Gravite🧠","Psy", "Statut", True, False, 0, 100, 100, False, 5)

Elecanon = Attaque("Elecanon⚡","Electrique", None, True, False, 120, 100, 50, False, 20)
Telluriforce = Attaque("Telluriforce🟫","Sol", None, True, False, 90, 100, 100, False, 20)
MagnetControle = Attaque("MagnetControle⚡","Electrique", "MG", True, False, 0, 100, 100, False, 20 ,buff="defense+defspe")
CavalerieLourde = Attaque("Cavalerie Lourde🐲","Dragon", None, False, False, 90, 100, 100, False, 10)
EclairFou = Attaque("Éclair Fou⚡","Electrique", None, True, False, 80, 100, 100, False, 15)
Colere = Attaque("Colère🐲","Dragon", None, False, False, 120, 100, 100, False, 10)
CageEclair = Attaque("Cage Éclair⚡","Electrique", None, False, False, 0, 100, 100, False, 20,buff="defense")

VoleForce = Attaque("Vole-Force🌱","Plante", None, False, False, 90, 100, 100, False, 15)
OmbrePortee = Attaque("Ombre Portée👻","Spectre", None, True, False, 80, 100, 100, False, 10)
Megafouet = Attaque("Mégafouet🌱","Plante", None, False, False, 120, 100, 85, False, 10)
Malediction = Attaque("Malédiction👻","Spectre", "Malédiction", False, False, 0, 100, 100, False, 5)

Rapace = Attaque("Rapace🫐","Poison", None, False, False, 80, 100, 100, False, 15)
GigaImpact = Attaque("Giga Impact🔘","Normal", None, False, False, 150, 100, 90, False, 5)
VoixEnvoutante = Attaque("Voix Envoûtante🦋","Fée", None, True, False, 90, 100, 100, False, 10)
GazToxik = Attaque("Gaz Toxik🫐","Poison", "Poison", False, False, 0, 100, 100, False, 10)

CriDraconique = Attaque("Cri Draconique🐲","Dragon", None, True, False, 80, 100, 100, False, 10)
TempeteVerte = Attaque("Tempête Verte🌱","Plante", None, True, False, 90, 100, 100, False, 10)
Soin = Attaque("Soin🔘","Normal", None, False, False, 0, 100, 100, False, 5)
PsykoudBoul = Attaque("Psykoud'Boul🧠","Psy", None, False, False, 80, 100, 100, False, 10)
Interversion = Attaque("Interversion🧠","Psy", None, False, False, 0, 100, 100, False, 10)
ForceAjoutee = Attaque("Force Ajoutée🌱","Plante", None, False, False, 80, 100, 100, False, 10)

Calinerie = Attaque("Câlinerie🦋","Fée", None, True, False, 70, 100, 100, False, 15)
ExploBrume = Attaque("Explo-Brume🦋","Fée", None, True, False, 90, 100, 100, False, 10)
VoixEnjoleuse = Attaque("Voix Enjôleuse🦋","Fée", None, True, False, 80, 100, 100, False, 10)

Ultralaser = Attaque("Ultralaser🔩","Acier", None, True, False, 120, 100, 90, False, 5)
Luminocanon = Attaque("Luminocanon🔩","Acier", None, True, False, 90, 100, 100, False, 10)
MurDeFer = Attaque("Mur de Fer🔩","Acier", None, False, False, 0, 100, 100, False, 10,buff="defense")
Puissance = Attaque("Puissance🔩","Acier", None, False, False, 100, 100, 100, False, 10)

NoeudHerbe = Attaque("Nœud Herbe🌱","Plante", None, False, False, 90, 100, 100, False, 10)
BlablaDodo = Attaque("Blabla Dodo🔘","Normal", "Comptine", False, False, 0, 100, 100, False, 15)
BombeBeurk = Attaque("Bombe Beurk🫐","Poison", None, False, False, 90, 100, 100, False, 10)

Abime = Attaque("Abîme🔥","Feu", None, True, False, 90, 100, 1000, False, 10)
Surpuissance = Attaque("Surpuissance🥊","Combat", None, False, False, 120, 100, 100, False, 10)
CoudKrane = Attaque("Coud'Krâne🥊","Combat", None, False, False, 80, 100, 100, False, 15)
TacleFeu = Attaque("Tacle Feu🔥","Feu", None, False, False, 65, 100, 95, False, 20)

DernierRecours = Attaque("Dernier Recours🔘","Normal", None, False, False, 140, 100, 100, False, 5)
VastePouvoir = Attaque("Vaste Pouvoir🔘","Normal", None, True, False, 120, 100, 90, False, 10)
Zenith = Attaque("Zénith🔥","Feu", "Zénith", True, False, 0, 100, 100, False, 5)

StridoSon = Attaque("Strido-Son🔥","Feu", None, True, False, 70, 100, 100, False, 15)
Boutefeu = Attaque("Boutefeu🔥","Feu", None, True, False, 90, 100, 100, False, 10)
MurLumiere = Attaque("Mur Lumière🔘","Normal", None, False, False, 0, 100, 100, False, 10,buff="defense")

Charge = Attaque("Charge🔘", "Normal", None, False, False, 40, 100, 100, False, 25)
PoingGlace = Attaque("Poing-Glace❄️","Glace",None, False, False, 65, 100, 100, False, 15)
TeteDeFer = Attaque("Tête-De-Fer🔩", "Acier", None, False, False, 80, 100, 80, False, 15)
CarapacePsy = Attaque("Carapace Psy🧠","Psy", "MG", True, False, 0, 100, 100, False, 20 ,buff="defense+defspe")

CoupDBoule = Attaque("Coup d'Boule🔘","Normal", None, False, False, 70, 100, 100, False, 15)
Armure = Attaque("Armure🔘","Normal", "MG", True, False, 0, 100, 100, False, 20 ,buff="defense+defspe")
Eboulement = Attaque("Eboulement🟫","Roche","Paralysie", False, False, 75, 100, 90, False, 15)
PistoletAO = Attaque("Pistolet à O💧","Eau", None, False, False, 40, 100, 100, False, 25)

EspritFrappeur=Attaque("Esprit Frappeur👻","Spectre",None,None,None,110,0,100,False,10)


Scovillain = Pokemon(
"Scovillain🔥🌱",
("Feu","Plante"),
65,
75,
("Acier","Electrique","Fée"),
("Plante",),
(),
("Poison","Roche","Vol"),
(),
108,
65,
108,
65,
[Habanerage,LanceFlamme,Surchauffe,CanonGraine]
)



Sorbouboul = Pokemon(
"Sorbouboul❄️",
("Glace",),
71,
79,
("Glace",),
(),
(),
("Feu","Combat","Vol","Acier"),
(),
95,
85,
110,
95,
[Blizzard,Stalactite,DansePluie,Destruction]
)

Kravarech = Pokemon(
"Kravarech 🐲💧",
("Dragon","Eau"),
65,
44,
("Feu","Eau","Electrique","Combat","Poison","Insecte"),
("Plante",),
(),
("Sol","Glace","Psy","Dragon"),
(),
75,
90,
97,
123,
[Toxik,Acidarmure,Ouragan,DracoMeteore]
)

Farigiraf  = Pokemon(
"Farigiraf 🧠🔘",
("Psy","Normal"),
120,
60,
("Psy",),
(),
("Spectre",),
("Ténèbres","Psy"),
(),
90,
70,
110,
70,
[Psyko,Machination,DissonancePsy,Gravite]
)

PelageSablé  = Pokemon(
"Pelage-Sablé🟫⚡",
("Sol","Electrique"),
85,
101,
("Poison","Vol","Roche","Acier"),
(),
("Electrique",),
("Plante","Eau","Glace","Sol"),
(),
81,
97,
121,
85,
[Elecanon,Telluriforce,Gravite,MagnetControle]
)

Galvagon  = Pokemon(
"Galvagon🐲⚡",
("Dragon","Electrique"),
90,
75,
("Plante","Vol","Feu","Acier","Eau"),
(),
(),
("Glace","Dragon","Fée","Sol"),
(),
100,
90,
80,
70,
[CavalerieLourde,EclairFou,Colere,CageEclair]
)

Virevorreur  = Pokemon(
"Virevorreur🌱👻",
("Plante","Spectre"),
55,
90,
("Plante","Electrique","Sol","Eau"),
(),
("Normal","Combat"),
("Glace","Feu","Spectre","Ténèbres","Vol"),
(),
115,
70,
80,
70,
[VoleForce,OmbrePortee,Megafouet,Malediction]
)

Pomdorochi  = Pokemon(
"Pomdorochi🐲🌱",
("Dragon","Plante"),
106,
44,
("Sol",),
("Plante","Eau",'Electrique'),
(),
("Poison","Vol","Insecte","Dragon","Fée"),
("Glace",),
80,
110,
120,
80,
[CriDraconique,TempeteVerte,Soin,DracoMeteore]
)

Sylveroy  = Pokemon(
"Sylveroy🧠🌱",
("Psy","Plante"),
100 ,
80,
("Plante","Eau","Electrique","Combat","Sol","Psy"),
(),
(),
("Ténèbres","Spectre","Feu","Vol","Glace","Poison"),
("Insecte",),
80,
80,
80,
80,
[PsykoudBoul,Interversion,ForceAjoutee,TempeteVerte]
)

Amovenus  = Pokemon(
"Amovénus🦋🪶",
("Fée","Vol"),
74 ,
106,
("Plante","Ténèbres"),
("Insecte","Combat"),
("Combat","Sol"),
("Electrique","Glace","Poison","Roche","Acier"),
(),
115,
70,
135,
80,
[Calinerie,VoixEnvoutante,ExploBrume,VoixEnjoleuse]
)

Pondralugon  = Pokemon(
"Pondralugon🔩🐲",
("Acier","Dragon"),
90 ,
85,
("Normal","Acier","Eau","Electrique","Vol","Psy","Insecte","Roche"),
("Plante",),
("Poison",),
("Combat","Sol"),
(),
105,
130,
125,
65,
[Ultralaser,Luminocanon,MurDeFer,Puissance]
)

Saquedeneu  = Pokemon(
"Saquedeneu🌱",
("Plante",),
65,
60,
("Plante","Eau","Electrique","Sol"),
(),
(),
("Feu","Glace","Poison","Vol","Insecte"),
(),
55,
115,
100,
40,
[Ultralaser,NoeudHerbe,BlablaDodo,BombeBeurk]
)

Chartor  = Pokemon(
"Chartor🔥",
("Feu",),
70,
20,
("Plante","Feu","Glace","Insecte","Acier","Fée"),
(),
(),
("Eau","Sol","Roche"),
(),
85,
140,
85,
70,
[Abime,Surpuissance,CoudKrane,TacleFeu]
)

Pierroteknik  = Pokemon(
"Pierroteknik🔥👻",
("Feu","Spectre"),
53,
107,
("Plante","Feu","Glace","Poison","Acier","Fée"),
(),
("Normal","Combat"),
("Eau","Sol","Roche","Spectre","Ténèbres"),
(),
127,
53,
151,
79,
[Surchauffe,DernierRecours,VastePouvoir,Zenith]
)

MiteDeFer  = Pokemon(
"Mite-de-Fer🔥🫐",
("Feu","Poison"),
80,
110,
("Plante","Feu","Glace","Poison","Acier","Fée"),
(),
("Normal","Combat"),
("Eau","Sol","Roche","Spectre","Ténèbres"),
(),
70,
60,
140,
110,
[StridoSon,Boutefeu,Toxik,MurLumiere]
)

Balbaleze = Pokemon(
    "Balbalèze❄️",
    ("Glace",),
    170,
    73,
    ("Glace",),
    (),
    ("Feu","Roche","Combat","Acier",),
    (),
    (),
    113,
    65,
    45,
    55,
    [Blizzard,Charge,Malediction,Ultralaser]
)

 

IreFoudre = Pokemon(
    "Ire-Foudre⚡",
    ("Electrique",),
    125,
    73,
    ("Acier","Eau","Feu","Plante","Vol",),
    ("Electrique",),
    ("Dragon","Fée","Glace","Sol",),
    (),
    (),
    91,
    137,
    89,
    75,
    [Zenith,DracoMeteore,CriDraconique,Ultralaser]
)

 

Bekaglacon = Pokemon(
    "Békaglaçon❄️",
    ("Glace",),
    75,
    50,
    ("Glace",),
    (),
    ("Acier","Combat","Feu","Roche",),
    (),
    (),
    80,
    110,
    65,
    90,
    [Blizzard,Charge,PoingGlace,TeteDeFer]
)

 

Pechaminus = Pokemon(
    "Péchaminus🫐👻",
    ("Poison","Spectre",),
    88,
    88,
    ("Fée","Plante",),
    ("Poison"),
    ("Psy","Sol","Spectre","Ténèbres",),
    (),
    ("Normal","Combat",),
    88,
    160,
    88,
    88,
    [Machination,Toxik,CarapacePsy,GazToxik]
)
Tomberro = Pokemon(
    "Tomberro👻",
    ("Spectre",),
    72,
    68,
    ("Insecte","Poison",),
    (),
    ("Spectre","Ténèbres"),
    (),
    ("Normal","Combat",),
    101,
    100,
    50,
    97,
    [CoupDBoule,Toxik,CarapacePsy,Calinerie]
)

 

Ferdeter = Pokemon(
    "FerDeTer🔩",
    ("Acier",),
    70,
    65,
    ("Acier","Dragon","Fée","Glace","Insecte","Normal","Plante","Psy","Roche","Vol",),
    (),
    ("Combat","Feu","Sol",),
    (),
    ("Poison",),
    85,
    145,
    60,
    55,
    [Charge,Armure,TeteDeFer,Eboulement]
)

 

Hydragla = Pokemon(
    "Hydragla💧",
    ("Eau",),
    90,
    55,
    ("Eau",),
    ("Glace",),
    ("Roche","Plante","Combat","Electrique",),
    (),
    (),
    90,
    100,
    80,
    90,
    [Blizzard,GigaImpact,CoupDBoule,PistoletAO]
)
 
Tutétékri=Pokemon(
    "Tutétékri🟫👻",
    ("Sol","Spectre"),
    58,
    30,
    ("Insecte","Roche",),
    ("Poison",),
    ("Plante","Spectre","Ténèbre","Eau","Glace",),
    (),
    ("Electrique","Combat","Normal",),
    95,
    145,
    50,
    105,
    [Malediction,Ultralaser,PsykoudBoul,EspritFrappeur]
)


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
        