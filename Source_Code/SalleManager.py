import random

from Salles import Salle, Case
from Boutique import Boutique
from Inventory import ObjetConsommable, ObjetPermanent, Nourriture 
from Salles import Coffre, Casier, Digspot
class SalleManager:
    """
    Classe qui gère le tirage / pool des salles à proposer lors de l'ouverture d'une porte.
    Utilise les données de la classe Salle (catalogue).
    """
    def __init__(self, salle_catalogue: Salle):
        self.catalogue = salle_catalogue

    def pooling_salle(self, coordonnees, porte_index):
        """
        Retourne pool (IDs) et poids (probabilities) selon :
         - count > 0
         - la salle a une porte correspondante (porte_index_match)
         - condition de placement (bord/normal/...): utilise peut_etre_placee()
         - poids dépend de rareté et du prix (gemmes) et de la rangée (coordonnees[1])
        """
        # mapping pour match de porte : si ouverture depuis une porte côté p, la salle candidate doit
        # posséder la porte opposée.
        # On suppose index: 0=N,1=E,2=S,3=W ; lorsque la porte ouverte a un index = p , 
        # la salle candidate doit avoir index p opposé

        if porte_index == 0:
            porte_index_match = 2
        elif porte_index == 1:
            porte_index_match = 3
        elif porte_index == 2:
            porte_index_match = 0
        else:
            porte_index_match = 1

        pool = []
        poids = []
        facteur = 1.0 # facteur à ajuster pdnt la periode de test

        for ID in self.catalogue.IDs:
            count = self.catalogue.salles_count_dict.get(ID)
            if count is None or count <= 0:
                continue
            portes = self.catalogue.salle_porte_emplacement_dict.get(ID)
            if not portes[porte_index_match]:
                continue
            # vérifier condition placement (Case doit être fourni par l'appelant, nous recevrons coordinates)
            # ici nous ne connaissons pas la case; on laisse la validation à l'appelant via peut_etre_placee()
            # mais on ajoute le poids:
            rarete = self.catalogue.salles_rarete_dict.get(ID)
            if rarete is None:
                rarete = 0
            prix = self.catalogue.salles_price_dict.get(ID, 0)
            # plus la rangée (coordonnees[1]) est élevée, plus le prix pèse (ex: coord[1]/9)
            poids_ID = 1.0 / (3 ** rarete) * (1 + facteur * (coordonnees[1] / 9) * prix)
            pool.append(ID)
            poids.append(poids_ID)

        return pool, poids

    def tirage_salles(self, coordonnees, porte_index, case_obj: Case):
        """
        Tire 3 salles en respectant:
         - filtrage par condition de placement (case_obj)
         - renormalisation des poids
         - s'assure qu'au moins une salle gratuite (price == 0) si coordonnees[1] == 1
        """
        pool, poids = self.pooling_salle(coordonnees, porte_index)

        # filtrer pool par condition de placement
        pool_filtered = []
        poids_filtered = []
        for ID, p in zip(pool, poids):
            if self.catalogue.peut_etre_placee(ID, case_obj):
                pool_filtered.append(ID)
                poids_filtered.append(p)

        if not pool_filtered:
            return []

        # normaliser
        total = sum(poids_filtered)
        poids_norm = [p / total for p in poids_filtered]

        tirage = []
        pool_temp = pool_filtered.copy()
        poids_temp = poids_norm.copy()

        for _ in range(min(3, len(pool_temp))):
            choix = random.choices(pool_temp, weights=poids_temp, k=1)[0]
            tirage.append(choix)
            idx = pool_temp.index(choix)
            pool_temp.pop(idx)
            poids_temp.pop(idx)
            if poids_temp:
                s = sum(poids_temp)
                poids_temp = [p / s for p in poids_temp]

        # s'assurer d'avoir au moins une salle avec prix==0 si on est sur la première rangée (col==1)
        if coordonnees[1] == 1:
            if not any(self.catalogue.salles_price_dict.get(ID, 0) == 0 for ID in tirage):
                # trouver candidates gratuites encore dans pool_filtered
                pool_free = [ID for ID in pool_filtered if self.catalogue.salles_price_dict.get(ID, 0) == 0]
                if pool_free:
                    tirage[0] = random.choice(pool_free)

        return tirage

    def generer_salle(self, coordonnees, salle_ID):
        """
        Créer un dictionnaire représentant l'instance de salle placée (portail/objets...).
        """
        instance = {
            "ID": salle_ID,
            "name": self.catalogue.salles_names_dict.get(salle_ID),
            "color": self.catalogue.salle_couleur_dict.get(salle_ID),
            "price": self.catalogue.salles_price_dict.get(salle_ID),
            "portes": self.catalogue.salle_porte_emplacement_dict.get(salle_ID),
            "effect": self.catalogue.salles_conditions_dict.get(salle_ID),
            "contenu": [],   # objets générés plus tard
            "shop": None,    # sera une Boutique si Yellow room
        }

        # Lier une boutique si c'est une Yellow room
        if instance["color"] == "Yellow":
            instance["shop"] = Boutique(instance["name"])

        return instance
    

class SalleManager:

  # Poids des probabilitées de tirer chaque item

    def get_item_weights(self, salle_ID):

        rarete = self.catalogue.salles_rarete_dict.get(salle_ID)
        couleur = self.catalogue.salle_couleur_dict.get(salle_ID)
        condition = self.catalogue.salles_conditions_dict.get(salle_ID)

        # TIERS (Common / Rare / Epic / Legendary)
        weights = {
            # COMMON
            "Pièces": 55,
            "Clés": 25,
            "Pomme": 16,
            "Banane": 12,
            "Dés": 8,

            # RARE
            "Sandwich": 5,
            "Gâteau": 4,
            "Gemmes": 13,

            # EPIC / LEGENDARY (permanents à 3%)
            "Shovel": 3,
            "Hammer": 3,
            "Metal Detector": 3,
            "Lockpick Kit": 3,
            "Lucky Rabbit Foot": 3,
        }


        # Bonus par couleurs

        if couleur == "Red":
            weights["Gemmes"] *= 3
            weights["Shovel"] *= 3
            weights["Hammer"] *= 3

        elif couleur == "Green":
            weights["Pomme"] *= 1.4
            weights["Banane"] *= 1.3


        if rarete >= 2: # Bonus pour salles rares
            for item in ["Shovel", "Hammer", "Metal Detector", "Lockpick Kit", "Lucky Rabbit Foot"]:
                weights[item] *= 1.5

        return weights


    #  Lucky bonus (augmente la probabilité d’objets rares)
    def apply_lucky_bonus(self, weights, bonus_factor):
        
        premium_items = [
            "Gemmes", "Shovel", "Hammer", "Metal Detector",
            "Lockpick Kit", "Lucky Rabbit Foot", "Gâteau"
        ]

        for item in premium_items:
            if item in weights:
                weights[item] *= (1 + bonus_factor)
        return weights

    def generer_digspots(self, salle_ID): # endroits ou creuser

        digspots = []

        # Couleur must be Green
        couleur = self.catalogue.salle_couleur_dict.get(salle_ID, "Blue")
        if couleur != "Green":
            return digspots

        # Green rooms : 0  3 dig spots
        nb = random.randint(0, 4)
        for _ in range(nb) : 
            digspots.append[Digspot()]
        return digspots


    def generer_conteneurs(self, salle_ID): # Coffres ou casiers

        rarete = self.catalogue.salles_rarete_dict.get(salle_ID, 0)
        condition = self.catalogue.salles_conditions_dict.get(salle_ID, None)
        conteneurs = []

        # Locker Room → 1 à 3 casiers garantis
        if condition == "Locker Room":
            nb = random.randint(1, 3)
            for _ in range(nb):
                conteneurs.append(Casier())

        # Coffre → rare + rareté
        proba_coffre = 0.1 + 0.05 * rarete
        if random.random() < proba_coffre:
            conteneurs.append(Coffre())

        return conteneurs
    
    def generer_contenu(self, salle_ID, inventaire=None, lucky_bonus=0.0):
        """
        Génère :
        - conteneurs
        - digspots
        - objets au sol
        """

        contenu = []

     # 1) Conteneurs
        contenu.extend(self.generer_conteneurs(salle_ID))

      # 2) Digspots
        if inventaire is not None:
            contenu.extend(self.generer_digspots(salle_ID, inventaire))

  
        # 3) poids des loots + bonus
    
        weights = self.get_item_weights(salle_ID)
        weights = self.apply_lucky_bonus(weights, lucky_bonus)

        total = sum(weights.values())
        nb_items = random.randint(1, 3)

      # 4) tirage du floor loot
      
        for _ in range(nb_items):

            r = random.uniform(0, total)
            cumul = 0
            item_choose = None

            for item, weight in weights.items():
                cumul += weight
                if r <= cumul:
                    item_choose = item
                    break

            # OBJETS
            if item_choose == "Pièces":
                contenu.append(("Pièces", random.randint(5, 20)))

            elif item_choose == "Clés":
                contenu.append(("Clés", random.randint(1,4)))

            elif item_choose == "Gemmes":
                contenu.append(("Gemmes", random.randint(1,3)))

            elif item_choose == "Dés":
                contenu.append(("Dés", random.randint(1,2)))

            # NOURRITURE
            elif item_choose in ["Pomme", "Banane", "Gâteau", "Sandwich"]:
                contenu.append((item_choose))

            # OBJETS PERMANENTS
            else:
                contenu.append(item_choose)

        return contenu


    

    