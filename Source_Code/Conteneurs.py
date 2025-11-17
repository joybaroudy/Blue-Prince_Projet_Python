import random
from Inventory import Inventaire, ObjetConsommable, ObjetPermanent, Nourriture


class Conteneur:
    """
    Classe parent pour Coffre, Casier et Digspot.
    Définit:
        - contenu
        - cout (si applicable)
        - ouvert / genere
        - salle_manager
    Ne définit PAS generer_contenu, ni ouvrir (abstrait).
    """

    def __init__(self, salle_manager, max_items=4):
        self.contenu = []
        self.max_items = max_items
        self.salle_manager = salle_manager

        self.genere = False
        self.ouvert = False

        # Valeur par défaut pour les conteneurs
        self.cout = 0  # Coffre / Casier changeront à 1

    def generer_contenu(self, salle_ID):
        pass

    def ouvrir(self, inventaire: Inventaire):
        pass



class Coffre(Conteneur):
    """
    Coffre : ouverture avec 1 clé OU Hammer.
    Peut contenir :
        - consommables
        - pièces, gemmes...
        - nourriture
        - objets permanents
    """

    def __init__(self, salle_manager, max_items=4):
        super().__init__(salle_manager, max_items)
        self.cout = 1  # 1 clé pour ouvrir le coffre

    def ouvrir(self, inventaire: Inventaire):
        """
        Ouvre le coffre :
            - si Hammer obtenu : ouverture gratuite
            - sinon consomme 1 clé si disponible
        """
        if self.ouvert:
            return True

        # Marteau -> ouvre gratuitement
        hammer = inventaire.objets_permanents["Hammer"]
        if isinstance(hammer, ObjetPermanent) and hammer.obtenu:
            self.ouvert = True
            return True

        # Sinon, payer 1 clé
        if inventaire.objets_consommables["Clés"].quantite >= self.cout:
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
            return True

        return False

    def generer_contenu(self, salle_ID):
        if self.genere:
            return

        self.genere = True
        n_items = random.randint(1, self.max_items)

        item_weights = self.salle_manager.get_item_weights(salle_ID)
        if not item_weights:
            return

        objets = list(item_weights.keys())
        poids = list(item_weights.values())

        for _ in range(n_items):
            choix = random.choices(objets, weights=poids, k=1)[0]

            # Consommables classiques
            if choix in ["Pièces", "Gemmes", "Clés", "Dés"]:
                if choix == "Pièces":
                    quantite = random.randint(5, 20)
                else:
                    quantite = random.randint(1, 10)
                self.contenu.append((choix, quantite))

            # Nourriture
            elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]:
                self.contenu.append(Nourriture(choix, 1))

            # Objets permanents
            else:
                # On stock l’objet permanent sous forme de string
                self.contenu.append((choix, 1))



class Casier(Conteneur):
    """
    Casier :
        - coûte 1 clé pour ouvrir
        - NE PEUT PAS contenir d'objets permanents
    """

    def __init__(self, salle_manager, max_items=4):
        super().__init__(salle_manager, max_items)
        self.cout = 1

    def ouvrir(self, inventaire: Inventaire):
        if self.ouvert:
            return True

        if inventaire.objets_consommables["Clés"].quantite >= self.cout:
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
            return True

        return False

    def generer_contenu(self, salle_ID):
        if self.genere:
            return

        self.genere = True
        n_items = random.randint(0, self.max_items)

        item_weights = self.salle_manager.get_item_weights(salle_ID)
        if not item_weights:
            return

        objets = list(item_weights.keys())
        poids = list(item_weights.values())

        for _ in range(n_items):
            choix = random.choices(objets, weights=poids, k=1)[0]

            # Consommables
            if choix in ["Pièces", "Gemmes", "Clés", "Dés"]:
                if choix == "Pièces":
                    quantite = random.randint(5, 20)
                else:
                    quantite = random.randint(1, 10)
                self.contenu.append((choix, quantite))

            # Nourriture
            elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]:
                self.contenu.append(Nourriture(choix, 1))

            # Objets permanents -> casier n'en donne pas
            else:
                continue


class Digspot(Conteneur):
    """
    Digspot :
        - nécessite la pelle (Shovel) pour être ouvert
        - ne contient PAS d'objets permanents
    """

    def __init__(self, salle_manager, max_items=3):
        super().__init__(salle_manager, max_items)

    def ouvrir(self, inventaire: Inventaire):
        shovel = inventaire.objets_permanents["Shovel"]
        if shovel.obtenu:
            self.ouvert = True
            return True
        return False

    def generer_contenu(self, salle_ID, inventaire: Inventaire):
        if self.genere:
            return

        shovel = inventaire.objets_permanents["Shovel"]
        if not shovel.obtenu:
            return

        self.genere = True
        n_items = random.randint(0, self.max_items)

        item_weights = self.salle_manager.get_item_weights(salle_ID)
        if not item_weights:
            return

        objets = list(item_weights.keys())
        poids = list(item_weights.values())

        for _ in range(n_items):
            choix = random.choices(objets, weights=poids, k=1)[0]

            # Consommables
            if choix in ["Pièces", "Gemmes", "Clés", "Dés"]:
                if choix == "Pièces":
                    quantite = random.randint(5, 20)
                else:
                    quantite = random.randint(1, 10)
                self.contenu.append((choix, quantite))

            # Nourriture
            elif choix in ["Pomme", "Banane", "Gâteau", "Sandwich"]:
                self.contenu.append(Nourriture(choix, 1))

            # Objets permanents -> Digspot n'en donne pas
            else:
                continue
