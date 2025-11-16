

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


# -----------------------------------------------------------
#  ===  ETAT D'UNE CASE DU MANOIR  ===
# -----------------------------------------------------------

class RoomCell:
    """
    Contient l'état permanent d'une salle dans le manoir :
        - explored : True si on est déjà entré dedans au moins une fois
        - room_id : ID de la salle attribuée à cette case
        - loot_on_ground : objets générés par generer_contenu()
        - containers : liste d'objets Coffre / Casier / Digspot non encore ouverts
        - doors : liste de 4 DoorState (haut, droite, bas, gauche)
    """
    def __init__(self, coordonnees, rotation = 0):
        self.coordonnees = coordonnees
        self.explored = False
        self.room_id = None  # défini quand on entre pour la première fois
        self.loot_on_ground = []  # objets posés dans la salle
        self.containers = []      # coffres, casiers
        self.digspots = []        # digspots à garder
        self.rotation = rotation # degre de rotation

        self.doors = [DoorState(False) for _ in range(4)]  # [S, O, N, E]

