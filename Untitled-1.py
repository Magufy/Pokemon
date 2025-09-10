class Pokemon():
    def __init__(self,nom,type,pv,vitesse,res,res2,faib,faib2,attaque,defense,attspé,defspé,comp,immu):
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
        self.attspé = attspé
        self.defspé = defspé
        self.comp = list(comp)
    def __str__(self):
        return (f"Pokémon: {self.nom}\n"
                f"Type(s): {self.type}, {self.faib} (Faiblesses), {self.res} (Résistances)\n"
                f"PV: {self.pv}\n"
                f"Vitesse: {self.vitesse}\n"
                f"Attaque: {self.attaque} | Défense: {self.defense}\n"
                f"Attaque Spéciale: {self.attspé} | Défense Spéciale: {self.defspé}\n"
                f"Compétences: {', '.join([c.nom for c in self.comp])}")
    class Degats():
        def __init__(self,nom,degats,type,precision,caté):
           self.nom = nom
           self.degats = degats
           self.type = type
           self.degats = precision
           self.caté = caté

        def __str__(self):
            return f"{self.nom} ({self.type}) - Puissance: {self.puissance}, Précision: {self.precision}%, Catégorie: {self.categorie}"
        
Scorvilain = Pokemon(
"Scovilain",
("Feu","Plante"),
65,
75,
("Acier","Electrique","Fée"),
("Plante"),
(),
("Poison","Roche","Vol"),
(),
108,
65,
108,
65,
["Habarenage","Lance-flamme","Surchauffe","Canon-Graine"]
)

Sorbouboul = Pokemon(
"Sorbouboul",
("Glace"),
71,
79,
("Glace"),
(),
(),
("Feu","Combat","Vol","Acier"),
(),
95,
85,
110,
95,
["Blizzard","Stalactite","Danse Pluie","Destruction"]
)

Kravarech = Pokemon(
"Kravarech",
("Dragon","Eau"),
65,
44,
("Feu","Eau","Electrique","Combat","Poison","Insecte"),
("Plante"),
(),
("Sol","Glace","Psy","Dragon"),
(),
75,
90,
97,
123,
["Buée Noire","Acidarmure","Ouragan","Draco-Météore"]
)

Farigiraf  = Pokemon(
"Farigiraf ",
("Psy","Normal"),
120,
60,
("Psy"),
(),
("Spectre"),
("Ténèbres","Psy"),
(),
90,
70,
110,
70,
["Psyko","Machination","Dissonance Psy","Gravité"]
)

PelageSablé  = Pokemon(
"Pelage-Sablé ",
("Sol","Electrique"),
85,
101,
("Poison","Vol","Roche","Acier"),
(),
("Electrique"),
("Plante","Eau","Glace","Sol"),
(),
81,
97,
121,
85,
["Élecanon","Telluriforce","Gravité","Magné-Contrôle"]
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
("Plante","Eau",'Elecrtique'),
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






