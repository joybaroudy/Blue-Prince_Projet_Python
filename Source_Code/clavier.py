import pygame
from Salles import Case
from Boutique import Boutique
from TraitementBoutique import TraitementBoutique
from EffetsSalles import EffetsSalles
from Salles import Porte


# ordre des portes : [Sud, Ouest, Nord, Est]
DIRECTION_TO_PORTE_INDEX = {
    "bas": 0,      # Sud
    "gauche": 1,   # Ouest
    "haut": 2,     # Nord
    "droite": 3,   # Est
}

def pixel_to_case(x, y, cell_size=60):
    col = x // cell_size + 1
    row = y // cell_size + 1
    return (col, row)


def lancer_boutique_si_jaune(room_id, salle_catalogue, inventaire):
    if room_id is None:
        return
    couleur = salle_catalogue.salle_couleur_dict.get(room_id)
    if couleur != "Yellow":
        return
    nom_salle = salle_catalogue.salles_names_dict.get(room_id)
    boutique = Boutique(nom_salle)
    tb = TraitementBoutique(boutique)
    tb.traitement_boutique(inventaire)



def gerer_clavier(joueur, manoir, salle_catalogue, salle_selectionnee,
                  tirage_effectuee, direction_choisi, plateau, inventaire):

    continuer = True

    if not hasattr(gerer_clavier, "index_selection"):
        gerer_clavier.index_selection = 0
    

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:
            continuer = False

        # ==== 1) MOUVEMENT + PAS DE TIRAGE ACTUEL ====
        if evenement.type == pygame.KEYDOWN and not tirage_effectuee:

            direction = None
            if evenement.key in (pygame.K_q, pygame.K_LEFT):
                direction = "gauche"
            elif evenement.key in (pygame.K_d, pygame.K_RIGHT):
                direction = "droite"
            elif evenement.key in (pygame.K_z, pygame.K_UP):
                direction = "haut"
            elif evenement.key in (pygame.K_s, pygame.K_DOWN):
                direction = "bas"

            if not direction:
                continue

            x_actu, y_actu = joueur.x, joueur.y
            porte_index_depart = DIRECTION_TO_PORTE_INDEX[direction]

            # ==== CALCUL NEW POSITION ====
            if direction == "gauche":
                new_pos = (x_actu - 60, y_actu)
            elif direction == "droite":
                new_pos = (x_actu + 60, y_actu)
            elif direction == "haut":
                new_pos = (x_actu, y_actu - 60)
            elif direction == "bas":
                new_pos = (x_actu, y_actu + 60)

            x_new, y_new = new_pos

            # Limites
            if x_new < 0 or x_new > 240 or y_new < 0 or y_new > 480:
                continue

            # ==== COORDONNÉES GRILLE ====
            coord_actu = pixel_to_case(x_actu, y_actu)
            coord_new = pixel_to_case(x_new, y_new)

            porte = manoir.get_door(coord_actu, porte_index_depart)

            if not porte.exists:
                print("Pas de porte dans cette direction.")
                continue

            # ==== PORTE NON OUVERTE → POPUP ====
            if not porte.opened:

                if not porte.demander_ouverture_porte(inventaire):
                    print("Vous avez refusé d'ouvrir la porte.")
                    continue

                # Essai d'ouverture
                if not porte.ouvrir_porte(inventaire):
                    print("Impossible d'ouvrir la porte.")
                    continue

                porte.opened = True

            # ==== PORTE OUVERTE ====

            # CAS 1 : La salle existe déjà → déplacement simple
            if manoir.has_room(coord_new):

                joueur.x, joueur.y = new_pos
                cell = manoir.enter_existing_room(coord_new)

                # effets d'entrée
                effet = EffetsSalles(cell.room_id, salle_catalogue)
                effet.apply_entry_effects(inventaire)

                # boutique jaune
                lancer_boutique_si_jaune(cell.room_id, salle_catalogue, inventaire)

                # consommation pas
                inventaire.objets_consommables["Pas"].changer_solde(-1)

                continue

            # CAS 2 : Nouvelle salle → tirage via Manoir
            tirage = manoir.open_door(coord_actu, porte_index_depart)

            if not tirage:
                print("Pas de tirage possible.")
                continue

                    # Ici, les deux salles ont bien une porte face à face → déplacement autorisé
                    joueur.x, joueur.y = new_pos
                    print(f"Déplacement dans une salle existante : {nom_salle_voisine}")

                    # Appliquer les effets d'entrée de la salle

                    effet = EffetsSalles(salle_id_voisine, salle_catalogue)
                    effet.apply_entry_effects(inventaire)

                    print(f"[EFFET] Effets appliqués : {effet.name}")

                    

                    salle_selectionnee = None
                    tirage_effectuee = False
                    direction_choisi = None
                    gerer_clavier.index_selection = 0
                    continue

                salle_choisie = salle_selectionnee[choix]
                nom_salle = salle_catalogue.salles_names_dict.get(salle_choisie)

                # === DÉPLACEMENT ===
                if direction_choisi == "gauche":
                    joueur.x -= 60
                elif direction_choisi == "droite":
                    joueur.x += 60
                elif direction_choisi == "haut":
                    joueur.y -= 60
                elif direction_choisi == "bas":
                    joueur.y += 60

                coord_new = pixel_to_case(joueur.x, joueur.y)

                # enregistre la salle
                manoir.set_room(coord_new, salle_choisie)

                # génère son loot
                manoir.setup_room_content(coord_new)

                # applique effets
                effet = EffetsSalles(salle_choisie, salle_catalogue)
                effet.apply_entry_effects(inventaire)

                print(f"[EFFET] Effets appliqués : {effet.name}")

                

                new_pos=(joueur.x,joueur.y)
                #Si on attaint l'antichambre
                if plateau.get(new_pos)=="Antechamber" and inventaire.objets_consommables["Pas"].quantite>=0:
                    print("Partie gagné")
                    continuer=False
                #Si plus de pas = partie perdue
                elif inventaire.objets_consommables["Pas"].quantite<=0:
                    print("VOus n'avez plus de pas.Vous avez perdue la partie") 
                    continuer=False

                #On enregistre les nouvelles position du joueur=emplacement de la salle choisi
                new_pos_x,new_pos_y=joueur.x,joueur.y

                #On enregistre la salle choisie sur le plateau
                plateau[(new_pos_x,new_pos_y)]=nom_salle

                lancer_boutique_si_jaune(nom_salle, salle_catalogue, inventaire)

                    #Réinitialisation de tous les état
                salle_selectionnee=None
                tirage_effectuee=False
                direction_choisi=None
                gerer_clavier.index_selection=0
    
    return continuer,salle_selectionnee,tirage_effectuee, direction_choisi

