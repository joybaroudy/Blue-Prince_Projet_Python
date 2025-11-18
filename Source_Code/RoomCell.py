from Salles import Salle, Porte

# Etat des portes (existantes ou pas)

class DoorState:
    """
    Représente l'état d'une porte autour d'une case :
        - exists : est-ce qu'une porte existe physiquement ?
        - opened : est-ce qu'elle a été ouverte ?
        - roll_done : est-ce que le tirage des salles a déjà été fait ?
        - rolled_results : liste des résultats (3 ID de salle) tirés lors de l'ouverture
    """
    def __init__(self, exists=False):
        self.exists = exists
        self.opened = False
        self.tirage_done = False
        self.tirage_results = None  # Ex: ["ID14", "ID4", "ID22"]
        self.generated = False



class RoomCell:
    """
    Contient l'état permanent d'une salle dans le manoir :
        - explored : True si on est déjà entré dedans au moins une fois
        - room_id : ID de la salle attribuée à cette case
        - loot_on_ground : objets générés par generer_contenu()
        - containers : liste d'objets Coffre / Casier / Digspot non encore ouverts
        - doors : liste de 4 DoorState (haut, droite, bas, gauche)
    """

    def __init__(self, coordonnees, rotation=0):
        self.coordonnees = coordonnees
        self.rotation = rotation

        self.explored = False
        self.room_id = None
        self.loot_on_ground = []
        self.containers = []
        self.digspots = []
        self.all_loot = self.loot_on_ground + self.containers + self.digspots

        # --- 1) INITIALISATION DES VRAIES PORTES ---
        # 4 portes : direction = 0:Sud, 1:Ouest, 2:Nord, 3:Est
        # On leur donne la coordonnée de la salle
        self.doors = [Porte(coordonnees) for _ in range(4)]

        # --- 2) INITIALISATION DES ETATS DE TIRAGE ---
        self.doorstates = [DoorState() for _ in range(4)]

        # --- 3) CAS SPÉCIAL : ENTRANCE HALL ---
        if self.coordonnees == (1, 3):
            self.explored = True
            self.room_id = "ID2"
            # les portes sont "ouvertes" dans le gameplay
            for porte in self.doors:
                porte.ouvert = True
                porte.level = 0
                porte.cout = 0
            # et on considère que leur tirage n'existe pas
            for ds in self.doorstates:
                ds.exists = False


    def add_loot(self, item):
        """Ajoute un objet au loot de la salle"""
        self.loot_on_ground.append(item)

    def remove_loot(self, item):
        """Enlève un objet du loot si ramassé"""
        if item in self.loot_on_ground:
            self.loot_on_ground.remove(item)

    def add_container(self, container):
        self.containers.append(container)

    def remove_container(self, container):
        if container in self.containers:
            self.containers.remove(container)




        


