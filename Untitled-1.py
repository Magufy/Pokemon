import random
from random import choice
import copy

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

        for statut in ["Comptine", "Gel", "Paralysie", "Confusion"]:
            if statut in self.statut:
                if self.cant_attack:
                    if random.randint(1, 100) <= 50: 
                        self.statut.remove(statut)
                        self.cant_attack = False
                        print(f"{self.nom} n'est plus affecté par {statut} !")
                else:
                    self.cant_attack = True
                    print(f"{self.nom} est affecté par {statut} et risque de ne pas attaquer !")
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
        Compensateur_Niveaux = 7
        Degats=((((Att*Pui)/Def)/50)+2)*CM*Compensateur_Niveaux
        #Sleep,Paralysie
        #Terrain : pluie,gravité,champelek ptet
        #Vol de Vie,Protection
        #remove uminity(gravité)
        #Les pokemon perdent de la vie en attaquant ( malediction , destruction,une autre)
        #PP
        
        if self.attaque.statut != False:
            if self.attaque.statut in ("Poison","Burn","Gel","Confusion","Paralysie","Comptine") :
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

class Battle:
    def __init__(self,pokemons_dispo):
        self.equipe=[]
        self.poke_front=None
        self.robot= Bot(pokemons_dispo)

    def cree_equipe(self,pokemons_dispo):
        while len(self.equipe)<1:
            poke_num=int(input(f"choisissez le numero de votre pokemon votre pokemon {[i.nom for i in pokemons_dispo]}"))
            if poke_num in range (1,len(pokemons_dispo)+1):
                self.equipe.append(copy.deepcopy(pokemons_dispo[poke_num-1]))
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
    def executer_attaque(self, attaquant, defenseur, attaque):
        if attaque.puissance == 0:
            #buff
            if attaque.buff:
                attaquant.buffs.append(attaque.buff)
                if attaque.buff == "defense":
                    print(f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense augmente fortement !")
                elif attaque.buff == "attspe":
                    print(f"{attaquant.nom} utilise {attaque.nom} ! Son Attaque Spéciale augmente fortement !")
                elif attaque.buff == "defense+defspe":
                    print(f"{attaquant.nom} utilise {attaque.nom} ! Sa Défense et Défense Spéciale augmentent !")
                elif attaque.buff == "rage":
                    print(f"{attaquant.nom} est pris de rage ! Son Attaque augmente énormément mais sa Défense baisse !")
            #statut
            elif attaque.statut:
                defenseur.statut.append(attaque.statut)
                print(f"{attaquant.nom} utilise {attaque.nom} ! {defenseur.nom} est affecté par {attaque.statut} !")
        else:
            #attaquedebase
            deg = Degats(attaquant, defenseur, attaque).degats()
            defenseur.pv -= deg
            print(f"{attaquant.nom} utilise {attaque.nom} ! Dégâts infligés : {deg}")

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
            action = int(input("choisissez une action : 1) Attaquer , 2) Objet , 3) Changer , 4) Capituler : "))

            if action == 1:
                choix = int(input(f"Choisissez une attaque : "
                                f"1) {self.poke_front.comp[0].nom} | "
                                f"2) {self.poke_front.comp[1].nom} | "
                                f"3) {self.poke_front.comp[2].nom} | "
                                f"4) {self.poke_front.comp[3].nom} : "))
                attaque_joueur = self.poke_front.comp[choix-1]

                if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0:
                    attaque_bot = choice(self.robot.poke_front_bot.comp)
                else:
                    attaque_bot = None

                if self.poke_front.vitesse >= (self.robot.poke_front_bot.vitesse if self.robot.poke_front_bot else 0):
                    self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

                    if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0:
                        print(f"Bot : {self.robot.poke_front_bot.nom}, utilise {attaque_bot.nom} !")
                        self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

                else:
                    if self.robot.poke_front_bot and self.robot.poke_front_bot.pv > 0:
                        print(f"Bot : {self.robot.poke_front_bot.nom}, utilise {attaque_bot.nom} !")
                        self.executer_attaque(self.robot.poke_front_bot, self.poke_front, attaque_bot)

                    if self.poke_front.pv > 0:
                        self.executer_attaque(self.poke_front, self.robot.poke_front_bot, attaque_joueur)

            elif action == 2: 
                print("Pas encore implémenté.")
                return

            elif action == 3: 
                poke_change = int(input(f"Choisissez un Pokémon : {[i.nom for i in self.equipe]} : "))
                if 1 <= poke_change <= len(self.equipe):
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
        while True:
            if (self.equipe == [] and self.poke_front is None) or (self.poke_front and self.poke_front.pv <= 0):
                print("Vous avez perdu (la honte)")
                return

            if (self.robot.equipe_bot == [] and self.robot.poke_front_bot is None) or (self.robot.poke_front_bot and self.robot.poke_front_bot.pv <= 0):
                print("Bravo, vous avez gagné (heureusement, c'est un bot)")
                return

            self.tour()





# ajouter : proba,precision,prio,PP

#dans lordre :nom,type,statut,special,haut_crit,puissance,proba,precision,prio,PP,buff=None
Habanerage = Attaque("Habanerage","Plante","Habanerage", False, False, 0, 100, 100, False, 24, buff="rage")
LanceFlamme = Attaque("LanceFlamme","Feu", None, True, False, 90, 100, 100, False, 24)
Surchauffe = Attaque("Surchauffe","Feu", None, True, False, 130, 100, 90, False, 5)
CanonGraine = Attaque("CanonGraine","Plante", None, False, False, 80, 100, 100, False, 24)

Blizzard = Attaque("Blizzard","Glace", None, True, False, 110, 100, 70, False, 5)
Stalactite = Attaque("Stalactite","Glace", None, False, False, 25, 100, 100, False, 30)
DansePluie = Attaque("DansePluie","Eau", "Pluie", True, False, 0, 100, 100, False, 5)
Destruction = Attaque("Destruction","Normal", None, False, False, 200, 100, 100, False, 5)

Toxic=Attaque("Toxic","Poison","Poison", False, False, 0, 100, 100, False, 16)
Acidarmure = Attaque("Acidarmure","Poison", "Acidarmure", True, False, 0, 100, 100, False, 20,buff="defense")
Ouragan = Attaque("Ouragan","Vol", None, True, False, 40, 100, 100, False, 20)
DracoMeteore = Attaque("DracoMeteore","Dragon", None, True, False, 130, 100, 90, False, 5)

Psyko = Attaque("Psyko","Psy", None, True, False, 90, 100, 100, False, 10)
Machination = Attaque("Machination","Ténèbres", "Machination", True, False, 0, 100, 100, False, 20, buff="attspe")
DissonancePsy = Attaque("DissonancePsy","Psy", None, True, False, 75, 100, 100, False, 10)
Gravite = Attaque("Gravite","Psy", "Statut", True, False, 0, 100, 100, False, 5)

Elecanon = Attaque("Elecanon","Electrique", None, True, False, 120, 100, 50, False, 20)
Telluriforce = Attaque("Telluriforce","Sol", None, True, False, 90, 100, 100, False, 20)
MagnetControle = Attaque("MagnetControle","Electrique", "MG", True, False, 0, 100, 100, False, 20 ,buff="defense+defspe")
CavalerieLourde = Attaque("Cavalerie Lourde","Dragon", None, False, False, 90, 100, 100, False, 10)
EclairFou = Attaque("Éclair Fou","Electrique", None, True, False, 80, 100, 100, False, 15)
Colere = Attaque("Colère","Dragon", None, False, False, 120, 100, 100, False, 10)
CageEclair = Attaque("Cage Éclair","Electrique", None, False, False, 0, 100, 100, False, 20,buff="defense")

VoleForce = Attaque("Vole-Force","Plante", None, False, False, 90, 100, 100, False, 15)
OmbrePortee = Attaque("Ombre Portée","Spectre", None, True, False, 80, 100, 100, False, 10)
Megafouet = Attaque("Mégafouet","Plante", None, False, False, 120, 100, 85, False, 10)
Malediction = Attaque("Malédiction","Spectre", "Malédiction", False, False, 0, 100, 100, False, 5)

Rapace = Attaque("Rapace","Poison", None, False, False, 80, 100, 100, False, 15)
GigaImpact = Attaque("Giga Impact","Normal", None, False, False, 150, 100, 90, False, 5)
VoixEnvoutante = Attaque("Voix Envoûtante","Fée", None, True, False, 90, 100, 100, False, 10)
GazToxik = Attaque("Gaz Toxik","Poison", "Poison", False, False, 0, 100, 100, False, 10)

CriDraconique = Attaque("Cri Draconique","Dragon", None, True, False, 80, 100, 100, False, 10)
TempeteVerte = Attaque("Tempête Verte","Plante", None, True, False, 90, 100, 100, False, 10)
Soin = Attaque("Soin","Normal", None, False, False, 0, 100, 100, False, 5)
PsykoudBoul = Attaque("Psykoud'Boul","Psy", None, False, False, 80, 100, 100, False, 10)
Interversion = Attaque("Interversion","Psy", None, False, False, 0, 100, 100, False, 10)
ForceAjoutee = Attaque("Force Ajoutée","Plante", None, False, False, 80, 100, 100, False, 10)

Calinerie = Attaque("Câlinerie","Fée", None, True, False, 70, 100, 100, False, 15)
ExploBrume = Attaque("Explo-Brume","Fée", None, True, False, 90, 100, 100, False, 10)
VoixEnjoleuse = Attaque("Voix Enjôleuse","Fée", None, True, False, 80, 100, 100, False, 10)

Ultralaser = Attaque("Ultralaser","Acier", None, True, False, 120, 100, 90, False, 5)
Luminocanon = Attaque("Luminocanon","Acier", None, True, False, 90, 100, 100, False, 10)
MurDeFer = Attaque("Mur de Fer","Acier", None, False, False, 0, 100, 100, False, 10,buff="defense")
Puissance = Attaque("Puissance","Acier", None, False, False, 100, 100, 100, False, 10)

NoeudHerbe = Attaque("Nœud Herbe","Plante", None, False, False, 90, 100, 100, False, 10)
BlablaDodo = Attaque("Blabla Dodo","Normal", "Sommeil", False, False, 0, 100, 100, False, 15)
BombeBeurk = Attaque("Bombe Beurk","Poison", None, False, False, 90, 100, 100, False, 10)

Abime = Attaque("Abîme","Feu", None, True, False, 90, 100, 100, False, 10)
Surpuissance = Attaque("Surpuissance","Combat", None, False, False, 120, 100, 100, False, 10)
CoudKrane = Attaque("Coud'Krâne","Combat", None, False, False, 80, 100, 100, False, 15)
TacleFeu = Attaque("Tacle Feu","Feu", None, False, False, 65, 100, 95, False, 20)

DernierRecours = Attaque("Dernier Recours","Normal", None, False, False, 140, 100, 100, False, 5)
VastePouvoir = Attaque("Vaste Pouvoir","Normal", None, True, False, 120, 100, 90, False, 10)
Zenith = Attaque("Zénith","Feu", "Zénith", True, False, 0, 100, 100, False, 5)

StridoSon = Attaque("Strido-Son","Feu", None, True, False, 70, 100, 100, False, 15)
Boutefeu = Attaque("Boutefeu","Feu", None, True, False, 90, 100, 100, False, 10)
Toxik = Attaque("Toxik","Poison","Poison", False, False, 0, 100, 100, False, 15)
MurLumiere = Attaque("Mur Lumière","Normal", None, False, False, 0, 100, 100, False, 10,buff="defense")



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
[CavalerieLourde,EclairFou,Colere,CageEclair]
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
[VoleForce,OmbrePortee,Megafouet,Malediction]
)

Pomdorochi  = Pokemon(
"Pomdorochi",
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
"Sylveroy",
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
[Calinerie,VoixEnvoutante,ExploBrume,VoixEnjoleuse]
)

Pondralugon  = Pokemon(
"Pondralugon",
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
"Saquedeneu",
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
"Chartor",
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
"Pierroteknik",
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
"Mite-de-Fer",
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


running=True
while running==True :
    choix=int(input("voulez vous : 1) Jouer  2) Quitter"))
    if choix==1 :
        pokemons_dispo = [
        Scorvilain, Sorbouboul, Kravarech, Farigiraf, PelageSablé,
        Galvagon, Virevorreur, Pomdorochi, Sylveroy,
        Amovenus, Pondralugon, Saquedeneu, Chartor, Pierroteknik, MiteDeFer
        ]   
        main=Battle(pokemons_dispo)
        main.cree_equipe(pokemons_dispo)
        main.choix_pokemon()
        main.main()
    elif choix==2 :
        running==False
