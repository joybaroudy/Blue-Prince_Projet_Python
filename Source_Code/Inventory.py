import random

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

    def consommer(self, inventaire):
        inventaire.objets_consommables["Pas"].changer_solde(self.gain)

class Casier(Objet):
    """
    Casier : peut être ouvert avec une clé (coût 1 par défaut).
    Contenu généré aléatoirement.
    """
    def __init__(self, contenu=None):
        super().__init__("Casier")
        self.cout = 1
        self.ouvert = False
        self.contenu = contenu  # None ou liste d'objets

    def ouvrir_casier(self, inventaire):
        """
        Ouvre le casier s'il y a assez de clés et s'il n'est pas déjà ouvert.
        """
        if not self.ouvert:
            if inventaire.objets_consommables["Clés"].quantite >= self.cout:
                inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
                self.ouvert = True
                return True
            else:
                return False
        return False

    def generer_contenu(self):
        """
        Génère le contenu du casier : nombre d'objets (probabilités).
        Retourne une liste d'éléments (ex: ["Pièces", "Clés", "Pomme"])
        """
        nb_possible = [0,1,2,3,4,5]
        probas = [0.05, 0.23, 0.3, 0.2, 0.1, 0.05]
        nb_obj = random.choices(nb_possible, weights=probas, k=1)[0]

        contenu = []
        # exemple simple : 50% pièces, 20% clés, 20% nourriture, 10% rien (à améliorer)
        for _ in range(nb_obj):
            r = random.random()
            if r < 0.5:
                contenu.append(("Pièces", random.randint(1, 20)))
            elif r < 0.7:
                contenu.append(("Clés", 1))
            else:
                contenu.append(("Pomme", 1))  # ou autre nourriture
        self.contenu = contenu
        return contenu


class Coffre(Objet):
    """
    Coffre : peut être ouvert avec une clé ou un marteau.
    """
    def __init__(self):
        super().__init__("Coffre")
        self.cout = 1
        self.ouvert = False
        self.contenu = None

    def ouvrir_coffre(self, inventaire):
        """
        Ouvre le coffre si joueur a marteau (obtenu=True) ou assez de clés.
        """
        if self.ouvert:
            return False

        hammer = inventaire.objets_permanents["Hammer"]
        if isinstance(hammer, ObjetPermanent) and hammer.obtenu:
            self.ouvert = True
            return True
        elif inventaire.objets_consommables["Clés"].quantite >= self.cout:
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
            return True
        else:
            return False

    def generer_contenu(self):
        """
        Génère le contenu du coffre (ex: pièces, gemmes, objet permanent rare...).
        """
        choix = random.random()
        if choix < 0.5:
            # pièces
            self.contenu = [("Pièces", random.randint(10, 40))]
        elif choix < 0.8:
            self.contenu = [("Gemmes", 1)]
        else:
            # petit chance d'avoir un objet permanent (ex: Metal Detector)
            self.contenu = [("Metal Detector", 1)]
        return self.contenu

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