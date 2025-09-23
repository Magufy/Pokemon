import random


class Degats:
    def __init__(self,poke_att,poke_def,attaque):
        self.poke_att=poke_att
        self.poke_def=poke_def
        self.attaque=attaque
        self.terrain=None

    def degats(self)-> int:#rajouter les priorités
        """
        calcul des degats infligés
        """
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

        Mod_terrain=0
        if self.attaque.statut=="Pluie":
            if self.attaque.type=="Eau":
                Mod_terrain+=0.5   # Aucune de nos attaque affectée par danse pluie donc delire de l'artiste

        CM = STAB * Type * Crit * random.uniform(0.85,1) + Mod_terrain
        Compensateur_Niveaux = 4
        Degats=((((Att*Pui)/Def)/50)+2)*CM*Compensateur_Niveaux

        #Les pokemon perdent de la vie en attaquant ( malediction , destruction,une autre)
        
        if self.attaque.statut != False:
            if self.attaque.statut in ("Poison","Burn","Gel","Paralysie","Comptine") :
                if random.randint(1,100) <= self.attaque.proba:
                    self.poke_def.statut.append(self.attaque.statut)
        if self.attaque.buff != None:
             if random.randint(1,100) <= self.attaque.proba:
                self.poke_att.buffs.append(self.attaque.buff)

        return int(Degats)






