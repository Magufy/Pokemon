import random

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
    def __str__(self):
        return (f"Pokémon: {self.nom}\n"
                f"Type(s): {self.type}, {self.faib} (Faiblesses), {self.res} (Résistances)\n"
                f"PV: {self.pv}\n"
                f"Vitesse: {self.vitesse}\n"
                f"Attaque: {self.attaque} | Défense: {self.defense}\n"
                f"Attaque Spéciale: {self.attspe} | Défense Spéciale: {self.defspe}\n"
                f"Compétences: {', '.join([c.nom for c in self.comp])}")

class Attaque():
    def __init__(self,type,statut,special,haut_crit,puissance):
        self.type=type
        self.statut=statut
        self.special=special
        self.haut_crit=haut_crit
        self.puissance=puissance


class Degats:
    def __init__(self,poke_att,poke_def,attaque):
        self.poke_att=poke_att
        self.poke_def=poke_def
        self.attaque=attaque

    def degats(self):#rajouter les priorités

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
        
        T=int(self.poke_att.vitesse/2)
        if self.attaque.haut_crit==True:
            T=T*8
        if T>255:
            T=255

        if random.randint(0,255)<T :
            Crit= 1.4 
        else:
            Crit= 1
        
        Obj=1  #pass

        CM= STAB * Type * Crit * Obj * random.uniform(0.85,1)
        Compensateur_Niveaux = 8
        Degats=((((Att*Pui)/Def)/50)+2)*CM*Compensateur_Niveaux
        return int(Degats)


Habarenage = Attaque("Plante", None, False, False, 90)
LanceFlamme = Attaque("Feu", None, True, False, 90)
Surchauffe = Attaque("Feu", None, True, False, 130)
CanonGraine = Attaque("Plante", None, False, False, 80)

Blizzard = Attaque("Glace", None, True, False, 110)
Stalactite = Attaque("Glace", None, False, False, 25)
DansePluie = Attaque("Eau", "Statut", True, False, 0)
Destruction = Attaque("Normal", None, False, False, 250)

BueeNoire = Attaque("Glace", "Statut", True, False, 0)
Acidarmure = Attaque("Poison", "Statut", True, False, 0)
Ouragan = Attaque("Vol", None, True, False, 40)
DracoMeteore = Attaque("Dragon", None, True, False, 130)

Psyko = Attaque("Psy", None, True, False, 90)
Machination = Attaque("Ténèbres", "Statut", True, False, 0)
DissonancePsy = Attaque("Psy", None, True, False, 80)
Gravite = Attaque("Psy", "Statut", True, False, 0)

Elecanon = Attaque("Electrique", None, True, False, 120)
Telluriforce = Attaque("Sol", None, True, False, 90)
MagnetControle = Attaque("Electrique", "Statut", True, False, 0)

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
[Habarenage,LanceFlamme,Surchauffe,CanonGraine]
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
[BueeNoire,Acidarmure,Ouragan,DracoMeteore]
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

Test = Degats(Scorvilain, Sorbouboul, Habarenage)
print(Test.degats())




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

