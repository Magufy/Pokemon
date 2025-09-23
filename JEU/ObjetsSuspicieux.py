import random

class Objet:
    def __init__(self, nom, equipe, equipe_adv, poke, poke_adv, nombre, side):
        self.nom = nom
        self.equipe = equipe
        self.equipe_adv = equipe_adv
        self.poke = poke
        self.poke_adv = poke_adv
        self.nombre = nombre
        if side == "Bot":
            self.side="le pokemon du bot"
            self.op="votre pokemon"
        else:
            self.op="le pokemon du bot"
            self.side="votre pokemon"

    def use(self):
        if self.nom not in ("Injection5G", "Glock", "Roulette Russe", "Gambling Time", "Produits Dopants", "Eau", "Calmants Pour Ours", "Repos Long"):
            return
        if self.nombre < 1:
            print(f"{self.side} n'a plus cet objet")
            return
        else:
            if self.nom == "Injection5G":
                self.poke.statut = []
                print(f'{self.side} perd tous ses effets')
            elif self.nom == "Glock":
                self.poke_adv.pv = 0
                print(f"Rapide et Efficace ({self.op} n'a pas survecu a cette balle)")
            elif self.nom == "Roulette Russe":
                a = random.randint(1, 2)
                if a == 1:
                    self.poke.pv = 0
                    print(f"тебе не повезло {self.side} a perdu")
                else:
                    self.poke_adv.pv = 0
                    print(f"тебе повезло {self.op} a perdu")

            elif self.nom == "Gambling Time":
                i = random.randint(-20,20)
                self.poke.pv+=i  
                if i>=0:             
                    print(f"{self.side} gagne {i}pv")
                else :
                    print(f"{self.side} perd {-i} pv")
            elif self.nom == "Produits Dopants":
                self.poke.pv += 20
                self.poke.attaque += 10
                self.poke.attspe += 20
                print(f"+20pv, +10att, +10att spé, c'est légal ça?     {self.side} a maintenant {self.poke.pv}pv")
            elif self.nom == "Eau":
                print(f"{self.side} est hydraté, c'est super mais a quoi ca sert ?")
                # rien
            elif self.nom == "Calmants Pour Ours":
                if "Comptine" not in self.poke_adv.statut:
                    self.poke_adv.statut.append("Comptine")
                print(f"{self.side} est boooriiiing, le {self.op} fait dodo")
            elif self.nom == "Repos Long":
                self.poke.pv += 20
                if "Comptine" not in self.poke.statut:
                    self.poke.statut.append("Comptine")
                print(f"Mimimimimimimimimi ({self.side} dort et recuperez 10PP et 20pv et vous avez {self.poke.pv}pv)")



