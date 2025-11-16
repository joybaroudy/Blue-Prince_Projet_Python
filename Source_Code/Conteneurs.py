import random
from Inventory import Inventaire, ObjetConsommable, ObjetPermanent, Nourriture



class Coffre:
    """
    Coffre / Casier / DigSpot
    Peut contenir plusieurs objets aléatoires (0 à 4)
    """
    def __init__(self, salle_manager, max_items=4):
        """
        salle_manager : instance de SalleManager (pour accéder à get_item_weights)
        max_items : nombre max d'objets par coffre
        """
        self.contenu = []
        self.max_items = max_items
        self.salle_manager = salle_manager
        self.genere = False
        self.cout = 1
        self.ouvert = False

    def ouvrir_coffre(self, inventaire : Inventaire):
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

    def generer_contenu(self, salle_ID):
        """
        Génère de 1 à max_items objets pour ce coffre
        """
        n_items = random.randint(1, self.max_items)
        item_weights = self.salle_manager.get_item_weights(salle_ID)

        if not item_weights:
            return  # pas de loot défini

        objets_possibles = list(item_weights.keys())
        poids = list(item_weights.values())

        for _ in range(n_items):
            choix = random.choices(objets_possibles, weights=poids, k=1)[0]
            # Déterminer la quantité selon le type
            if choix in  ["Pièces", "Gemmes", "Clés", "Dés"]:
                if choix == "Pièces" : 
                    quantite = random.randint(5,20)
                quantite = random.randint(1, 10)
                self.contenu.append((choix, quantite)) # ajoute un tuple avec la clé de l'item (pour l'inventaire) et sa quantité
            elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]: 
                quantite = 1
                self.contenu.append(Nourriture(choix, quantite)) # ajoute la clé seulement car le gain par objet nourriture est fixe
            else:                                                # Lavariable quantite est ajoutée pour eviter les errurs plus tard
                # Objet permanent
                quantite = 1
                self.contenu.append(choix,quantite)


class Casier:
    """
    Casier
    Peut contenir plusieurs objets aléatoires (0 à 4)
    """
    def __init__(self, salle_manager, max_items=4):
        """
        salle_manager : instance de SalleManager (pour accéder à get_item_weights)
        max_items : nombre max d'objets par coffre
        """
        self.contenu = []
        self.max_items = max_items
        self.salle_manager = salle_manager
        self.genere = False
        self.cout = 1
        self.ouvert = False

    def ouvrir_casier(self, inventaire : Inventaire):
        """
        Ouvre le coffre si joueur a marteau (obtenu=True) ou assez de clés.
        """
        if self.ouvert:
            return False

        if inventaire.objets_consommables["Clés"].quantite >= self.cout:
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
            return True
        else:
            return False

    def generer_contenu(self, salle_ID):
        """
        Génère de 0 à max_items objets pour ce coffre
        """
        n_items = random.randint(0, self.max_items)
        item_weights = self.salle_manager.get_item_weights(salle_ID)

        objets_possibles = list(item_weights.keys())
        poids = list(item_weights.values())

        for _ in range(n_items):

            self.genere = True
            choix = random.choices(objets_possibles, weights=poids, k=1)[0]
            # Déterminer la quantité selon le type
            if choix in  ["Pièces", "Gemmes", "Clés", "Dés"]:
                if choix == "Pièces" : 
                    quantite = random.randint(5,20)
                quantite = random.randint(1, 10)
                self.contenu.append((choix, quantite)) # ajoute un tuple avec la clé de l'item (pour l'inventaire) et sa quantité
            elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]: 
                quantite = 1
                self.contenu.append(Nourriture(choix, quantite)) # ajoute la clé seulement car le gain par objet nourriture est fixe
            else:                                                # Lavariable quantite est ajoutée pour eviter les errurs plus tard
                # Objet permanent
                continue # Si l'objet tiré est un objet permanent on ne l'ajoute pas car le casier n'a que des consommables

class Digspot:
    """
    DigSpot
    Peut contenir plusieurs objets aléatoires (0 à 4)
    """
    def __init__(self, salle_manager, max_items=3):
        """
        salle_manager : instance de SalleManager (pour accéder à get_item_weights)
        max_items : nombre max d'objets par coffre
        """
        self.contenu = []
        self.max_items = max_items
        self.salle_manager = salle_manager
        self.genere = False

    def generer_contenu(self, salle_ID, inventaire : Inventaire):
        """
        Génère de 0 à max_items objets pour ce digspot
        """

        shovel = inventaire.objets_permanents["Shovel"]
        if shovel.obtenu:

            self.genere = True 
            
            n_items = random.randint(0, self.max_items)
            item_weights = self.salle_manager.get_item_weights(salle_ID)

            objets_possibles = list(item_weights.keys())
            poids = list(item_weights.values())

            for _ in range(n_items):
                choix = random.choices(objets_possibles, weights=poids, k=1)[0]
                # Déterminer la quantité selon le type
                if choix in  ["Pièces", "Gemmes", "Clés", "Dés"]:
                    if choix == "Pièces" : 
                        quantite = random.randint(5,20)
                    quantite = random.randint(1, 10)
                    self.contenu.append((choix, quantite)) # ajoute un tuple avec la clé de l'item (pour l'inventaire) et sa quantité
                elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]: 
                    quantite = 1
                    self.contenu.append(Nourriture(choix, quantite)) # ajoute la clé seulement car le gain par objet nourriture est fixe
                else:                                                # Lavariable quantite est ajoutée pour eviter les errurs plus tard
                    # Objet permanent
                    continue # Si l'objet tiré est un objet permanent on ne l'ajoute pas car le casier n'a que des consommables









