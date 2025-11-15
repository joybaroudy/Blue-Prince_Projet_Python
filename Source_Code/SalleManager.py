import random

from Salles import Salle, Case
from Boutique import Boutique



class SalleManager:
    """
    Classe qui gère le tirage / pool des salles à proposer lors de l'ouverture d'une porte.
    Utilise les données de la classe Salle (catalogue).
    """


    def __init__(self, salle_catalogue: Salle):
        self.catalogue = salle_catalogue
        self.rotations = {ID: 0 for ID in self.catalogue.IDs}


    @staticmethod
    def _rotate_ports(ports, k):
        """
        ports : [S, W, N, E] (liste de 4 booléens)
        k : nombre de rotations de 90° dans le sens horaire (0..3)

        Retourne une nouvelle liste [S, W, N, E] après rotation.
        Hypothèse : ordre [Sud, Ouest, Nord, Est].
        Une rotation horaire de 90° donne :
          newS = oldW, newW = oldN, newN = oldE, newE = oldS
        => décalage circulaire vers la gauche.
        """
        k = k % 4
        return [ports[(i + k) % 4] for i in range(4)]


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


        #nouvelle addition pour la rotation aléatoire des salles
        self.rotations = {
            ID: random.randint(0, 3)   # 0,1,2,3 => 0°,90°,180°,270°
            for ID in self.catalogue.IDs
        }

        #fin nouvelle addition

        pool = []
        poids = []
        facteur = 1.0 # facteur à ajuster pdnt la periode de test

        for ID in self.catalogue.IDs:
            count = self.catalogue.salles_count_dict.get(ID)
            rarete = self.catalogue.salles_rarete_dict.get(ID)
            if rarete is None:
                continue
            if count is None or count == 0:
                continue
            portes = self.catalogue.salle_porte_emplacement_dict.get(ID)
            if not portes[porte_index_match]:
                continue
            # vérifier condition placement
            # ici nous ne connaissons pas la case; on laisse la validation à peut_etre_placee()
            # mais on ajoute le poids:
            

            #nouvelle addition pour la rotation aléatoire des salles
            
            k = self.rotations[ID]
            portes = self._rotate_ports(portes, k) # appliquer la rotation tirée pour CE pooling

            # on ne garde que si, une fois tournée, la salle a bien une porte du bon côté
            if not portes[porte_index_match]:
                continue
            
            #fin nouvelle addition
            
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

        #nouvelle addition pour la rotation aléatoire des salles
        # rotation qui a été tirée lors du dernier pooling_salle
        rotation = self.rotations.get(salle_ID, 0)

        base_portes = self.catalogue.salle_porte_emplacement_dict.get(salle_ID, [False]*4)
        portes_rot = self._rotate_ports(base_portes, rotation)
        #fin nouvelle addition

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

    
    
    
    def generer_contenu() :
        pass
    