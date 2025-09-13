import random
from random import choice

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
        if "Poison" in self.statut :
            pass
        if "Burn" in self.statut :
            pass
        if "Comptine" in self.statut :
            if self.cant_attack == True :
                random.randint(0,100)
                if random.randint > 80 :
                    self.statut.remove("Comptine")
            else :
                self.cant_attack = True
        if "Gel" in self.statut :
            if self.cant_attack == True :
                random.randint(0,100)
                if random.randint > 80 :
                    self.statut.remove("Gel")
            else :
                self.cant_attack = True
        if "MG" in self.statut :
            self.defense = self.defense*1.25
            self.defspe = self.defspe*1.25
            self.statut.remove("MG")
        if "Habanerage" in self.statut :
            self.attaque = self.attaque*2
            self.defense = self.defense/2
            self.statut.remove("Habanerage")
        if "Acidarmure" in self.statut :
            self.defense = self.defense*1.5
            self.statut.remove("Acidarmure")
        if "Machination" in self.statut :
            self.attspe = self.attspe*2
            self.statut.remove("Machination")

        

class Attaque():
    def __init__(self,nom,type,statut,special,haut_crit,puissance,proba,precision,prio,PP):
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

class Degats:
    def __init__(self,poke_att,poke_def,attaque):
        self.poke_att=poke_att
        self.poke_def=poke_def
        self.attaque=attaque

    def degats(self):#rajouter les priorités
        vitesse=self.poke_att.vitesse
        if self.poke_att.statut=="Paralysie":
            vitesse=vitesse/4
            if random.randint(0,100)<=25:
                return("Raté  (paralysie)")
        if self.attaque.puissance == 0:
            return 0
        if self.attaque.type in self.poke_def.immu:
            return 0
        
        Att = self.poke_att.attaque if self.attaque.special == False else self.poke_att.attspe
        Def = self.poke_def.defense if self.attaque.special == False else self.poke_def.defspe
        Pui=self.attaque.puissance

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
        Compensateur_Niveaux = 8
        Degats=((((Att*Pui)/Def)/50)+2)*CM*Compensateur_Niveaux
        #Sleep,Paralysie
        #Terrain : pluie,gravité,champelek ptet
        #Vol de Vie,Protection
        #Attaques qui buff
        #remove uminity(gravité)
        #Les pokemon perdent de la vie en attaquant ( malediction , destruction,une autre)
        #PP
        
        if self.attaque.statut != False:
            if self.attaque.statut in ("Poison","Burn","Gel","Confusion","Paralysie","Comptine","MG","Habanerage","Acidarmure","Machination") :
                if random.randint(1,100) <= self.attaque.proba:
                    self.poke_def.statut.append(self.attaque.statut)


            

        return int(Degats)

class Bot:
    def __init__(self,pokemons_dispo):
        self.equipe_bot=[]
        for i in range (6) :
            self.equipe_bot.append(choice(pokemons_dispo))
        self.poke_front_bot=choice(self.equipe_bot)
        self.equipe_bot.remove(self.poke_front_bot)

    def choix_pokemon_bot(self):
        self.poke_front_bot=choice(self.equipe_bot)
        self.equipe_bot.remove(self.poke_front_bot)

class Battle:
    def __init__(self,pokemons_dispo):
        self.equipe=[]
        self.poke_front=None
        self.robot= Bot(pokemons_dispo)

    def cree_equipe(self,pokemons_dispo):
        while len(self.equipe)<6:
            poke_num=int(input(f"choisissez le numero de votre pokemon votre pokemon {[i.nom for i in pokemons_dispo]}"))
            if poke_num in range (1,len(pokemons_dispo)+1):
                self.equipe.append(pokemons_dispo[poke_num-1])
                print('pokemon ajouté')
            else:
                print('pokemon non disponible')
            
    def choix_pokemon(self):
        while self.poke_front==None:
            poke=int(input(f"choisissez un pokemon a envoyer au combat{[i.nom for i in self.equipe]}"))
            if poke in range (1,len(self.equipe)+1):
                self.poke_front=self.equipe[poke-1]
                self.equipe.remove(self.equipe[poke-1])

    def mort_poke_front(self):
        if self.poke_front.pv<=0 : 
            self.poke_front=None
            self.choix_pokemon()

    def tour(self):
        self.mort_poke_front()

        action=None
        while action == None:
            action=int(input("choisissez une action : 1)  Attaquer , 2) Objet , 3) Changer , 4) Capituler"))
                
            if action == 2 :
                pass
                
            if action == 1 :
                attaque=None
                while attaque==None :
                    attaque=input(f"choisissez une attaque : 1) {self.poke_front.comp[0].nom}  2) {self.poke_front.comp[1].nom}  3) {self.poke_front.comp[2].nom}  4) {self.poke_front.comp[3].nom}   :")
                    if 1 <= int(choix) <= 4:
                        attaque = self.poke_front.comp[int(choix)-1]
                        deg = Degats(self.poke_front, self.robot.poke_front_bot, attaque).degats()
                        print(f"{self.poke_front.nom} utilise {attaque.nom} ! Dégâts infligés : {deg}")
                    else:
                        attaque=None

            elif action == 3 :
                poke_change=None
                while poke_change==None :
                    poke_change=input(f"choisissez un pokemon : {self.equipe}")
                    if poke_change in self.equipe:
                        self.equipe.append(self.poke_front)
                        self.poke_front=poke_change
                        self.equipe.remove(poke_change)
                    else:
                        poke_change=None

            elif action == 4 :
                global running
                running==False
            
            else:
                action=None

            #bot joue
            if self.robot.poke_front_bot.pv<=0:
                self.robot.choix_pokemon_bot
            Degats(self.poke_front, self.robot.poke_front_bot, attaque).degats()


    def main(self):
        if self.equipe==[] and self.poke_front==None :
            print("Vous avez perdu (la honte)")
            return
        elif self.robot.equipe_bot==[] and self.robot.poke_front_bot==None :
            print("Bravo, vous avez gagnez (heureusement, c'est un bot)")
            return
        else :
            self.tour()





# ajouter : proba,precision,prio,PP

Habanerage = Attaque("Habanerage","Plante","Habanerage", False, False, 0, 100, 100, False, 24)
LanceFlamme = Attaque("LanceFlamme","Feu", None, True, False, 90, 100, 100, False, 24)
Surchauffe = Attaque("Surchauffe","Feu", None, True, False, 130, 100, 90, False, 5)
CanonGraine = Attaque("CanonGraine","Plante", None, False, False, 80, 100, 100, False, 24)

Blizzard = Attaque("Blizzard","Glace", None, True, False, 110, 100, 70, False, 5)
Stalactite = Attaque("Stalactite","Glace", None, False, False, 25, 100, 100, False, 30)
DansePluie = Attaque("DansePluie","Eau", "Pluie", True, False, 0, 100, 100, False, 5)
Destruction = Attaque("Destruction","Normal", None, False, False, 200, 100, 100, False, 5)

Toxic=Attaque("Toxic","Poison","Poison", False, False, 0, 100, 100, False, 16)
Acidarmure = Attaque("Acidarmure","Poison", "Acidarmure", True, False, 0, 100, 100, False, 20)
Ouragan = Attaque("Ouragan","Vol", None, True, False, 40, 100, 100, False, 20)
DracoMeteore = Attaque("DracoMeteore","Dragon", None, True, False, 130, 100, 90, False, 5)

Psyko = Attaque("Psyko","Psy", None, True, False, 90, 100, 100, False, 10)
Machination = Attaque("Machination","Ténèbres", "Machination", True, False, 0, 100, 100, False, 20)
DissonancePsy = Attaque("DissonancePsy","Psy", None, True, False, 75, 100, 100, False, 10)
Gravite = Attaque("Gravite","Psy", "Statut", True, False, 0, 100, 100, False, 5)

Elecanon = Attaque("Elecanon","Electrique", None, True, False, 120, 100, 50, False, 20)
Telluriforce = Attaque("Telluriforce","Sol", None, True, False, 90, 100, 100, False, 20)
MagnetControle = Attaque("MagnetControle","Electrique", "MG", True, False, 0, 100, 100, False, 20)


Scorvilain = Pokemon(
"Scovilain",
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
"Sorbouboul",
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
"Kravarech",
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
[Toxic,Acidarmure,Ouragan,DracoMeteore]
)

Farigiraf  = Pokemon(
"Farigiraf ",
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
"Pelage-Sablé ",
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


"""
Galvagon  = Pokemon(
"Galvagon",
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
["Cavalerie Lourde","Éclair Fou","Colère","Cage Éclair"]
)

Virevorreur  = Pokemon(
"Virevorreur",
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
["Vole-Force","Ombre Portée","Mégafouet","Malédiction"]
)

Virevorreur  = Pokemon(
"Virevorreur",
("Poison","Fée"),
88,
99,
("Plante","Ténèbres","Fée"),
("Combat","Insecte"),
("Dragon"),
("Psy","Acier","Sol"),
(),
91,
82,
70,
125,
["Rapace","Giga Impact","Voix Envoûtante","Gaz Toxik"]
)

Pomdorochi  = Pokemon(
"Pomdorochi",
("Dragon","Plante"),
106,
44,
("Sol"),
("Plante","Eau",'Electrique'),
(),
("Poison","Vol","Insecte","Dragon","Fée"),
("Glace"),
80,
110,
120,
80,
["Cri Draconique","	Tempête Verte","Soin","Draco-Météore"]
)

Sylveroy  = Pokemon(
"Sylveroy",
("Psy","Plante"),
100 ,
80,
("Plante","Eau","Electrique","Combat","Sol","Psy"),
(),
(),
("Ténèbres","Spectre","Feu","Vol","Glace","Poison"),
("Insecte"),
80,
80,
80,
80,
["Psykoud'Boul","Interversion","Force Ajoutée","Tempête Verte"]
)

Amovénus  = Pokemon(
"Amovénus",
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
["Câlinerie","Voix Envoûtante","Explo-Brume","Voix Enjôleuse"]
)

Pondralugon  = Pokemon(
"Pondralugon",
("Acier","Dragon"),
90 ,
85,
("Normal","Acier","Eau","Electrique","Vol","Psy","Insecte","Roche"),
("Plante"),
("Poison"),
("Combat","Sol"),
(""),
105,
130,
125,
65,
["Ultralaser","Luminocanon","Mur de Fer","Puissance"]
)

Saquedeneu  = Pokemon(
"Saquedeneu",
("Plante"),
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
["Ultralaser","	Nœud Herbe","Blabla Dodo","Bombe Beurk"]
)

Chartor  = Pokemon(
"Chartor",
("Feu"),
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
["Abîme","Surpuissance","Coud'Krâne","Tacle Feu"]
)

Pierroteknik  = Pokemon(
"Pierroteknik",
("Feu","Spectre"),
53,
107,
("Plante","Feu","Glace","Poison","Acier","Fée"),
(),
("Normal","Combat"),
("Eau","Sol","Roche","Spectre","Ténebres"),
(),
127,
53,
151,
79,
["Surchauffe","Dernier Recours","Vaste Pouvoir","Zénith"]
)

MiteDeFer  = Pokemon(
"Mite-de-Fer",
("Feu","Poison"),
80,
110,
("Plante","Feu","Glace","Poison","Acier","Fée"),
(),
("Normal","Combat"),
("Eau","Sol","Roche","Spectre","Ténebres"),
(),
70,
60,
140,
110,
["Strido-Son","Boutefeu","Toxik","Mur Lumière"]
)

"""

running=True
while running==True :
    choix=int(input("voulez vous : 1) Jouer  2) Quitter"))
    if choix==1 :
        pokemons_dispo=[PelageSablé,Farigiraf,Kravarech,Sorbouboul,Scorvilain]
        main=Battle(pokemons_dispo)
        main.cree_equipe(pokemons_dispo)
        main.choix_pokemon()
        main.main()
    elif choix==2 :
        running==False
