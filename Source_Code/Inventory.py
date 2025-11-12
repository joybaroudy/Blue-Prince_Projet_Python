import random

class Case : 
    def __init__(self,coordinates) : 
        self.coordinates = coordinates
        if coordinates == [1,1] or coordinates == [1,5] or coordinates == [9,1] or coordinates == [9,5] : 
            self.position = "Corner"
        elif coordinates[0] == 1 or coordinates[0] == 9 or coordinates[1] == 1 or coordinates[1] == 5 : 
            self.position = "Edge"
        else : 
            self.position = "Normal"


class Objet: # To check if we keep it 
    """
    Classe de base pour tout objet du jeu.
    """
    def __init__(self, nom = None):
        self.nom = nom

class ObjetConsommable(Objet):
    """
    Classe pour les objets consommables (pas, pièces, clés, etc.)
    """
    def __init__(self, nom, quantite=0):
        super().__init__(nom)
        self.quantite = quantite

    def changer_solde(self, changement):
        """ 
        Methode qui aumente ou diminue la quantité d'item consommables dans l'inventaire 
        quand ils sont utilisés ou obtenus
        """
        self.quantite = self.quantite + changement

class ObjetPermanent(Objet):
    """Classe pour les objets permanents (Hammer, Shovel, etc.)"""
    def __init__(self, nom, obtenu=False):
        super().__init__(nom)
        self.obtenu = obtenu

    def debloquer(self):
        self.obtenu = True

class Nourriture(Objet):
    """
    Classe pour les objets nourriture (qui augmentent les pas), et leur methodes
    """
    def __init__(self, nom, gain):
        super().__init__(nom)
        self.gain = gain

    def consommer(self, inventaire):
        inventaire.objets_consommables["Pas"].changer_solde(self.gain)

class casier(Objet) : 
    """
    Classe pour les portes et leur methodes
    """
    def __init__(self, contenu = None) :

        self.cout = 1
        self.ouvert = False
        self.contenu = contenu

    def OuvrirCasier(self, inventaire) : 
        if inventaire.objets_consommables["Clés"] < self.cout and self.ouvert == False : 
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
    
    def ContenuCasier(self, inventaire) : 
        nb_possible = [0,1,2,3,4,5]
        probas = [0.05, 0.23, 0.3, 0.2, 0.1, 0.05]
        nb_obj = random.choices(nb_possible, weights=probas, k=1)[0]
        # To add contenu du casier


class Coffre(Objet) : 
    """
    Classe pour les coffre et leur methodes
    """
    def __init__(self) : 
        self.cout = 1
        self.ouvert = False
    
    def OuvrirCoffre(self, inventaire) : 
        if inventaire.objets_permanents["Hammer"] == True : 
            self.ouvert = True
        elif inventaire.objets_consommables["Clés"] > self.cout and self.ouvert == False : 
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True



class Inventaire:
    """
    Class contenant tous les items (permanents et non permanents) dans l'inventaire,  
    ainsi que les classes et methodes associées.

    L'inventaire contient : 
        
        Objets consommables : 
            Pas (Qui diminuent à chaque fois que le jouer change de pièce)
            Pièces (Qui sont utilisées pour être échangées contre d'autres objet)
            Gemmes (Qui sont utilisés pour debloquer certaines salles)
            Clés (Qui permettent d'ouvrir certaines portes et corffres)
            Dés (Qui permettent de tirer à nouveau au sort les pièces proposées apres ouverture de porte)

        Objets permanents : 
            Shovel (Qui permet de creuser pour trouver certains items)
            Hammer (Qui permet d'ouvrir des coffres sans utiliser des clés)
            Lockpick Kit (Qui permet d'ouvrir certaines portes sans utiliser de clés)
            Metal Detector (Qui augmente la chance de trouver des clés et des pièces)
            Lucky Rabbit's Foot (Qui augmente la chance de trouver des items dans le manoir(objets permanents inclus))

        Autres objets : 
            Pomme (Qui redonne 2 pas)
            Banane (Qui redonne 3 pas)
            Gâteau (Qui redonne 10 pas)
            Sandwich (Qui redonne 15 pas)
            Repas (Qui redonne 25 pas)
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
            "Shovel": ObjetPermanent("Shovel"),
            "Hammer": ObjetPermanent("Hammer"),
            "Lockpick Kit": ObjetPermanent("Lockpick Kit"),
            "Metal Detector": ObjetPermanent("Metal Detector"),
            "Lucky Rabbit Foot": ObjetPermanent("Lucky Rabbit's Foot")
        }

        self.nourritures = {
            "Pomme": Nourriture("Pomme", 2),
            "Banane": Nourriture("Banane", 3),
            "Gâteau": Nourriture("Gâteau", 10),
            "Sandwich": Nourriture("Sandwich", 15),
            "Repas": Nourriture("Repas", 25)
        }


        







































