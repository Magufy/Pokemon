class Attaque():
    def __init__(self,nom,type,statut,special,haut_crit,puissance,proba,precision,prio,buff=None):
        self.nom=nom
        self.type=type
        self.statut=statut
        self.special=special
        self.haut_crit=haut_crit
        self.puissance=puissance
        self.proba=proba
        self.precision=precision
        self.prio=prio
        self.buff=buff



#dans lordre :nom,type,statut,special,haut_crit,puissance,proba,precision,prio,buff=None
Habanerage = Attaque("Habanerage🌱","Plante",None, False, False, 90, 100, 100, False)
LanceFlamme = Attaque("LanceFlamme🔥","Feu", None, True, False, 90, 100, 100, False)
Surchauffe = Attaque("Surchauffe🔥","Feu", None, True, False, 130, 100, 90, False)
CanonGraine = Attaque("CanonGraine🌱","Plante", None, False, False, 80, 100, 100, False)

Blizzard = Attaque("Blizzard❄️","Glace", None, True, False, 110, 100, 70, False)
Stalactite = Attaque("Stalactite❄️","Glace", None, False, False, 25, 100, 100, False)
DansePluie = Attaque("DansePluie💧","Eau", None, True, False, 45, 100, 100, False)
Destruction = Attaque("Destruction🔘","Normal", None, False, False, 200, 100, 100, False)

Toxik=Attaque("Toxik🫐","Poison","Poison", False, False, 0, 100, 100, False)
Acidarmure = Attaque("Acidarmure🫐","Poison", None, True, False, 0, 100, 100, False,buff="defense")
Ouragan = Attaque("Ouragan🪶","Vol", None, True, False, 40, 100, 100, False)
DracoMeteore = Attaque("DracoMeteore🐲","Dragon", None, True, False, 130, 100, 90, False)

Psyko = Attaque("Psyko🧠","Psy", None, True, False, 90, 100, 100, False)
Machination = Attaque("Machination👤","Ténèbres",None, True, False, 0, 100, 100, False, buff="attspe")
DissonancePsy = Attaque("DissonancePsy🧠","Psy", None, True, False, 75, 100, 100, False)
Gravite = Attaque("Gravite🧠","Psy", "Statut", True, False, 0, 100, 100, False)

Elecanon = Attaque("Elecanon⚡","Electrique", None, True, False, 120, 100, 50, False)
Telluriforce = Attaque("Telluriforce🟫","Sol", None, True, False, 90, 100, 100, False)
MagnetControle = Attaque("MagnetControle⚡","Electrique", None, True, False, 0, 100, 100, False,buff="defense+defspe")

CavalerieLourde = Attaque("Cavalerie Lourde🐲","Dragon", None, False, False, 90, 100, 100, False)
EclairFou = Attaque("Éclair Fou⚡","Electrique", None, True, False, 80, 100, 100, False)
Colere = Attaque("Colère🐲","Dragon", None, False, False, 120, 100, 100, False)
CageEclair = Attaque("Cage Éclair⚡","Electrique", None, False, False, 0, 100, 100, False,buff="defense")

VoleForce = Attaque("Vole-Force🌱","Plante", None, False, False, 90, 100, 100, False)
OmbrePortee = Attaque("Ombre Portée👻","Spectre", None, True, False, 80, 100, 100, False)
Megafouet = Attaque("Mégafouet🌱","Plante", None, False, False, 120, 100, 85, False)
Malediction = Attaque("Malédiction👻","Spectre", None, False, False, 50, 100, 100, False)

Rapace = Attaque("Rapace🫐","Poison", None, False, False, 80, 100, 100, False)
GigaImpact = Attaque("Giga Impact🔘","Normal", None, False, False, 150, 100, 90, False)
VoixEnvoutante = Attaque("Voix Envoûtante🦋","Fée", "Comptine", True, False, 0, 100, 100, False)
GazToxik = Attaque("Gaz Toxik🫐","Poison", "Poison", False, False, 0, 100, 100, False)

CriDraconique = Attaque("Cri Draconique🐲","Dragon", None, True, False, 80, 100, 100, False)
TempeteVerte = Attaque("Tempête Verte🌱","Plante", None, True, False, 90, 100, 100, False)
PsykoudBoul = Attaque("Psykoud'Boul🧠","Psy", None, False, False, 80, 100, 100, False)
Interversion = Attaque("Interversion🧠","Psy", None, False, False, 0, 100, 100, False)

ForceAjoutee = Attaque("Force Ajoutée🌱","Plante", None, False, False, 80, 100, 100, False)
Calinerie = Attaque("Câlinerie🦋","Fée", None, True, False, 70, 100, 100, False)
ExploBrume = Attaque("Explo-Brume🦋","Fée", None, True, False, 90, 100, 100, False)
VoixEnjoleuse = Attaque("Voix Enjôleuse🦋","Fée", None, True, False, 80, 100, 100, False)

Ultralaser = Attaque("Ultralaser🔩","Acier", None, True, False, 120, 100, 90, False)
Luminocanon = Attaque("Luminocanon🔩","Acier", None, True, False, 90, 100, 100, False)
MurDeFer = Attaque("Mur de Fer🔩","Acier", None, False, False, 0, 100, 100, False,buff="defense")
Puissance = Attaque("Puissance🔩","Acier", None, False, False, 100, 100, 100, False)

NoeudHerbe = Attaque("Nœud Herbe🌱","Plante", None, False, False, 90, 100, 100, False)
BlablaDodo = Attaque("Blabla Dodo🔘","Normal", "Comptine", False, False, 0, 100, 100, False)
BombeBeurk = Attaque("Bombe Beurk🫐","Poison", None, False, False, 90, 100, 100, False)

Abime = Attaque("Abîme🔥","Feu", None, True, False, 90000, 100, 10, False)
Surpuissance = Attaque("Surpuissance🥊","Combat", None, False, False, 120, 100, 100, False)
CoudKrane = Attaque("Coud'Krâne🥊","Combat", None, False, False, 80, 100, 100, False)
TacleFeu = Attaque("Tacle Feu🔥","Feu", None, False, False, 65, 100, 95, False)

DernierRecours = Attaque("Dernier Recours🔘","Normal", None, False, False, 140, 100, 100, False)
VastePouvoir = Attaque("Vaste Pouvoir🔘","Normal", None, True, False, 120, 100, 90, False)
Zenith = Attaque("Zénith🔥","Feu", None, True, False, 75, 100, 100, False)

StridoSon = Attaque("Strido-Son🔥","Feu", None, True, False, 70, 100, 100, False)
Boutefeu = Attaque("Boutefeu🔥","Feu", None, True, False, 90, 100, 100, False)
MurLumiere = Attaque("Mur Lumière🔘","Normal", None, False, False, 0, 100, 100, False,buff="defense")

Charge = Attaque("Charge🔘", "Normal", None, False, False, 40, 100, 100, False)
PoingGlace = Attaque("Poing-Glace❄️","Glace",None, False, False, 65, 100, 100, False)
TeteDeFer = Attaque("Tête-De-Fer🔩", "Acier", None, False, False, 80, 100, 80, False)
CarapacePsy = Attaque("Carapace Psy🧠","Psy", None, True, False, 0, 100, 100, False,buff="defense+defspe")

CoupDBoule = Attaque("Coup d'Boule🔘","Normal", None, False, False, 70, 100, 100, False)
Armure = Attaque("Armure🔘","Normal", None, True, False, 0, 100, 100, False ,buff="defense+defspe")
Eboulement = Attaque("Eboulement🟫","Roche","Paralysie", False, False, 75, 100, 90, False)
PistoletAO = Attaque("Pistolet à O💧","Eau", None, False, False, 40, 100, 100, False)

EspritFrappeur=Attaque("Esprit Frappeur👻","Spectre",None,None,None,110,0,100,False)
AppelALaGreve=Attaque("Appel à la Grève🔘","Normal",None,True,None,10,0,10,False)

