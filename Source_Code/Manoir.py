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

    def get_door(self, coord : list, direction): # 
        return self.grid[coord].doors[direction]


    def enter_room(self, coord, new_room_ID):
        """
        Appelé quand le joueur entre dans une salle.
        Si première visite :
            - créer la salle (tirer ID)
            - générer le loot de salle
            - générer les conteneurs (mais pas leur contenu)
        Sinon, on ne change rien : on revient dans l'état précédent.
        """
        cell = self.grid[coord]

        # 1) ID de la salle entrée
        cell.room_id = new_room_ID

        # Initialiser l'existence des portes SANS rotation
        template_ports = self.salle_manager.catalogue.salle_porte_emplacement_dict[str(int(cell.room_id))]

        if template_ports:
            # template_ports est dans l'ordre : [Sud, Ouest, Nord, Est]
            for i in range(4):
                cell.doors[i].exists = bool(template_ports[i])

        if not cell.explored:
  


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
            results = self.salle_manager.tirage_salles(coordonnees=coord, porte_index=direction)
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
    
    
    def set_room(self, coord, salle_id):
        """
        Assigne manuellement un ID de salle à une RoomCell existante.
        Utilisé lorsqu'une salle est choisie depuis un tirage.
        """
        cell = self.grid[coord]
        cell.room_id = salle_id
        cell.explored = True

    def setup_room_content(self, coord):
        """
        Génère loot + conteneurs + digspots pour une salle existante.
        """
        cell = self.grid[coord]
        salle_id = cell.room_id

        cell.loot_on_ground = self.salle_manager.generer_contenu(salle_id)
        cell.containers = self.salle_manager.generer_conteneurs(salle_id)
        cell.digspots = self.salle_manager.generer_digspots(salle_id)

        return cell

    def has_room(self, coord):
        """Retourne True si une salle est déjà posée ici."""
        return self.grid[coord].room_id is not None

    def get_room_id(self, coord):
        """Retourne l'ID de salle stocké à une coordonnée."""
        return self.grid[coord].room_id

    def enter_existing_room(self, coord):
        """Retourne la RoomCell existante."""
        return self.grid[coord]

    

    
