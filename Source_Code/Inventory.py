import random
# from Objets import Objet, ObjetConsommable, ObjetPermanent, Nourritur

class Inventaire:
    """
    Stocke objets consommables, permanents, nourritures.
    """
    def __init__(self):
        self.objets_consommables = {
            "Pas": ObjetConsommable("Pas", 70),
            "Pièces": ObjetConsommable("Pièces", 0),
            "Gemmes": ObjetConsommable("Gemmes", 2),
            "Clés": ObjetConsommable("Clés", 0),
            "Dés": ObjetConsommable("Dés", 0)
        }

        self.objets_permanents = {
            "Shovel": ObjetPermanent("Shovel", obtenu=False),
            "Hammer": ObjetPermanent("Hammer", obtenu=False),
            "Lockpick Kit": ObjetPermanent("Lockpick Kit", obtenu=False),
            "Metal Detector": ObjetPermanent("Metal Detector", obtenu=False),
            "Lucky Rabbit Foot": ObjetPermanent("Lucky Rabbit Foot", obtenu=False)
        }

        self.nourritures = {
            "Pomme": Nourriture("Pomme", 2),
            "Banane": Nourriture("Banane", 3),
            "Gâteau": Nourriture("Gâteau", 10),
            "Sandwich": Nourriture("Sandwich", 15),
            "Repas": Nourriture("Repas", 25)
        }

    def ajouter_objet_consommable(self, nom, quantite):
        if nom in self.objets_consommables:
            self.objets_consommables[nom].changer_solde(quantite)
        else:
            self.objets_consommables[nom] = ObjetConsommable(nom, quantite)

    def debloquer_permanent(self, nom):
        if nom in self.objets_permanents:
            self.objets_permanents[nom].debloquer()
        else:
            self.objets_permanents[nom] = ObjetPermanent(nom, obtenu=True)



    def solde_pieces(self):
        """Retourne le nombre actuel de pièces d'or."""
        return self.objets_consommables["Pièces"].quantite

    def ajouter_pieces(self, n: int):
        """Ajoute n pièces (ou en enlève si n < 0)."""
        if n == 0:
            return
        self.objets_consommables["Pièces"].changer_solde(n)

    def depenser_pieces(self, n: int) -> bool:
        """
        Tente de dépenser n pièces.
        Renvoie True si le paiement a réussi, False sinon.
        """
        if n < 0:
            return False
        if self.solde_pieces() >= n:
            self.objets_consommables["Pièces"].changer_solde(-n)
            return True
        return False
    
class Objet:
    """Classe de base pour tout objet du jeu."""
    def __init__(self, nom=None):
        self.nom = nom

class ObjetConsommable(Objet):
    """Objets consommables (Pas, Pièces, Gemmes, Clés, Dés)."""
    def __init__(self, nom, quantite=0):
        super().__init__(nom)
        self.quantite = quantite

    def changer_solde(self, changement):
        """Augmente ou diminue la quantité."""
        self.quantite = self.quantite + changement
        
class ObjetPermanent(Objet):
    """Objet permanent (Shovel, Hammer, etc.)."""
    def __init__(self, nom, obtenu=False):
        super().__init__(nom)
        self.obtenu = obtenu

    def debloquer(self):
        self.obtenu = True

class Nourriture(Objet):
    """Nourriture - donne des pas."""
    def __init__(self, nom, gain):
        super().__init__(nom)
        self.gain = gain

    def consommer(self, inventaire : Inventaire ):
        inventaire.objets_consommables["Pas"].changer_solde(self.gain)

