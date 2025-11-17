import random
from SalleManager import SalleManager
from Inventory import Inventaire, Objet, ObjetConsommable, ObjetPermanent, Nourriture
from RoomCell import RoomCell, DoorState
from Conteneurs import Coffre, Casier, Digspot

class Manoir:
    """
    Gère la grille du manoir et l'état des salles :
        - stocke la RoomCell pour chaque coordonnée
        - gère les portes et leur tirage (sauvegardé en RAM)
        - gère l'exploration
        - gère le loot de salle
    """

    def __init__(self, salle_manager:SalleManager):
        self.largeur = 5
        self.hauteur = 9
        self.salle_manager = salle_manager  

        # Grille du jeu : dictionnaire {(x, y): RoomCell}
        self.grid = {}
        for x in range(1, self.largeur + 1):
            for y in range(1, self.hauteur + 1):
                self.grid[(x, y)] = RoomCell((x, y))


    # Methodes relatives aux portes :

    def set_door_exists(self, coord, direction, exists=True): # Verifie si une porte existe à la position donnée
        """direction = 0: Nord, 1: Est, 2: Sud, 3: Ouest"""
        self.grid[coord].doors[direction].exists = exists

    def get_door(self, coord, direction): # 
        return self.grid[coord].doors[direction]


    def enter_room(self, coord):
        """
        Appelé quand le joueur entre dans une salle.
        Si première visite :
            - créer la salle (tirer ID)
            - générer le loot de sallgie
            - générer les conteneurs (mais pas leur contenu)
        Sinon, on ne change rien : on revient dans l'état précédent.
        """
        cell = self.grid[coord]

        if not cell.explored:
            # 1) Tirer une salle 
            cell.room_id = self.salle_manager.tirage_salles(coord)

            # 2) Générer loot de salle
            cell.loot_on_ground = self.salle_manager.generer_contenu(cell.room_id)

            # 3) Générer conteneurs dans cette salle
            cell.containers = self.salle_manager.generer_conteneurs(cell.room_id)

            cell.digspots = self.salle_manager.generer_digspots(cell.room_id)

            # Salle maintenant explorée
            cell.explored = True

        return cell

    def open_door(self, coord, direction):
        """
        Lorsqu'on ouvre une porte :
            - Si le tirage n'a pas été fait : tirer les 3 salles
            - Sinon : récupérer les résultats existants
        """
        cell = self.grid[coord]
        door = cell.doors[direction]

        if not door.exists:
            return None  # pas de porte ici

        if not door.tirage_done:
            results = self.salle_manager.tirage_salles(coord, direction)
            door.tirage_results = results
            door.tirage_done = True
            door.opened = True
        else:
            results = door.tirage_results

        return results

    def get_containers(self, coord):
        return self.grid[coord].containers
    
    def get_digspots(self, coord):
        return self.grid[coord].digspots
    

    
