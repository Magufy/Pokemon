from attaques import *
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


Scovillain = Pokemon(
"Scovillain 🔥🌱  ",
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
"Sorbouboul ❄️  ",
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
"Kravarech 🐲💧  ",
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
"Farigiraf 🧠🔘  ",
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
"Pelage-Sablé 🟫⚡  ",
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
"Galvagon 🐲⚡  ",
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
"Virevorreur 🌱👻  ",
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
"Pomdorochi 🐲🌱  ",
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
[CriDraconique,TempeteVerte,Megafouet,DracoMeteore]
)

Sylveroy  = Pokemon(
"Sylveroy 🧠🌱  ",
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
"Amovénus 🦋🪶  ",
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
"Pondralugon 🔩🐲  ",
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
"Saquedeneu 🌱  ",
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
"Chartor 🔥  ",
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
"Pierroteknik 🔥👻  ",
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
"Mite-de-Fer 🔥🫐  ",
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
    "Balbalèze ❄️  ",
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
    "Ire-Foudre ⚡  ",
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
    "Békaglaçon ❄️  ",
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
    "Péchaminus 🫐👻  ",
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
    "Tomberro 👻  ",
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
    "FerDeTer 🔩  ",
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
    "Hydragla 💧  ",
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
    "Tutétékri 🟫👻  ",
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
