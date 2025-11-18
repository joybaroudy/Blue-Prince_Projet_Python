import pygame
from Salles import Case
from Inventory import Inventaire
from Boutique import Boutique
from TraitementBoutique import TraitementBoutique
from EffetsSalles import EffetsSalles
from Salles import Porte
from Manoir import Manoir
from Conteneurs import Casier, Coffre, Digspot
from Boutique import Boutique
from TraitementLoot import TraitementLoot

def lancer_boutique_si_jaune(nom_salle, salle_catalogue, inventaire):
    """
    Si la salle est jaune, ouvre la boutique correspondante.
    """
    salle_id = salle_catalogue.name_to_id.get(nom_salle)
    if salle_id is None:
        return

    couleur = salle_catalogue.salle_couleur_dict.get(salle_id)
    if couleur != "Yellow":
        return

    boutique = Boutique(nom_salle)
    tb = TraitementBoutique(boutique)
    tb.traitement_boutique(inventaire)


# ordre des portes : [Sud, Ouest, Nord, Est]
DIRECTION_TO_PORTE_INDEX = {
    "bas": 0,      # Sud
    "gauche": 1,   # Ouest
    "haut": 2,     # Nord
    "droite": 3,   # Est
}

def pixel_to_case(x, y, cell_size=60):
    """
    Convertit une position en pixels (x,y) en coordonnées de grille [row, col] 1..N.
    Tu pourras ajuster si ta grille de niveau n'est pas exactement alignée.
    """
    col = x // cell_size + 1
    row = y // cell_size + 1
    return [row, col]




def gerer_clavier(joueur, tirage_salle , salle_catalogue, salle_selectionnee,
                  tirage_effectuee, direction_choisi, plateau,inventaire, screen, portes_dict,manoir:Manoir,contenu_actuel=None):
    continuer = True
    contenu_complet=None

    # Initialiser l'index de sélection une fois
    if not hasattr(gerer_clavier, "index_selection"):
        gerer_clavier.index_selection = 0

    #Initialise l'index de sélections des items
    if not hasattr(gerer_clavier,"index_item_salle"):
        gerer_clavier.index_item_salle=0


    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

        # --- 1) MOUVEMENT + TIRAGE ---
        if evenement.type == pygame.KEYDOWN and not tirage_effectuee:
            direction = None
            if evenement.key == pygame.K_q or evenement.key == pygame.K_LEFT:
                direction = "gauche"
            elif evenement.key == pygame.K_d or evenement.key == pygame.K_RIGHT:
                direction = "droite"
            #Haut et bas uniquement si y'a aucun contenu de salle affiché
            elif evenement.key == pygame.K_UP or evenement.key == pygame.K_z:
                direction = "haut"
            elif evenement.key == pygame.K_DOWN or evenement.key == pygame.K_s:
                direction = "bas"
            
            elif evenement.key == pygame.K_t:

                # Trouver la case du joueur
                row, col = pixel_to_case(joueur.x, joueur.y)
                cell = manoir.grid[(col, row)]  # inversion obligatoire
                cell.room_id = salle_selectionnee  # ou l'ID de la salle actuelle


                # Ramasser le loot
                manoir.grid[(col,row)].all_loot = TraitementLoot.take_loot_from_room(cell, inventaire, screen)
                
                print("Objet(s) ramassé (T)")


            if direction:
                # position actuelle du joueur
                x_actu, y_actu = joueur.x, joueur.y
                print(f"[DEBUG] direction={direction}, pos_actuelle=({x_actu},{y_actu})")

                # 1) récupérer la salle actuelle sur le plateau
                nom_salle_actuelle = plateau.get((x_actu, y_actu))
                print(f"[DEBUG] salle actuelle : {nom_salle_actuelle}")
                if not nom_salle_actuelle:
                    # normalement ça ne devrait pas arriver si le plateau est bien rempli
                    print("Aucune salle à la position actuelle du joueur.")
                    continue

                # 2) récupérer l'ID + portes de la salle actuelle
                salle_id_actuelle = salle_catalogue.name_to_id.get(nom_salle_actuelle)
                if salle_id_actuelle is None:
                    print(f"Nom de salle inconnu côté catalogue : {nom_salle_actuelle}")
                    continue

                portes_salle = salle_catalogue.salle_porte_emplacement_dict.get(salle_id_actuelle)
                if portes_salle is None:
                    print(f"Aucune info de portes pour {salle_id_actuelle}")
                    continue

                porte_index_depart = DIRECTION_TO_PORTE_INDEX[direction]

                # 3) vérifier s'il y a une porte dans cette direction
                if not portes_salle[porte_index_depart]:
                    print(f"Pas de porte vers {direction} pour la salle {nom_salle_actuelle}")
                    continue  # on ignore la touche


                # 4) calculer la nouvelle case en pixels
                if direction == "gauche":
                    new_pos = (x_actu - 60, y_actu)
                elif direction == "droite":
                    new_pos = (x_actu + 60, y_actu)
                elif direction == "haut":
                    new_pos = (x_actu, y_actu - 60)
                elif direction == "bas":
                    new_pos = (x_actu, y_actu + 60)


                x, y = new_pos
                row, col = pixel_to_case(x, y)

                manoir.grid[(col, row)].room_id = salle_id_actuelle 

                print(f"On est dans la salle{salle_catalogue.salles_names_dict[salle_id_actuelle]}")
                
            
                
                #Limite de la zone du jeu
                limite_gauche=0
                limite_droite=300-60
                limite_haut=0
                limite_bas=480

                x_new,y_new=new_pos
                print(f"[DEBUG] new_pos=({x_new},{y_new}), limites=({limite_gauche},{limite_droite},{limite_haut},{limite_bas})")
                if x_new<limite_gauche or x_new>limite_droite or y_new<limite_haut or y_new>limite_bas:
                    print("impossible de dépasser")
                    continue

                # 5) si une salle existe déjà -> déplacement simple
                if new_pos in plateau:

                    # Nom de la salle voisine
                    nom_salle_voisine = plateau[new_pos]
                    salle_id_voisine = salle_catalogue.name_to_id.get(nom_salle_voisine)

                    if salle_id_voisine is None:
                        print(f"[WARN] Salle voisine inconnue dans le catalogue : {nom_salle_voisine}")
                        continue

                    portes_voisine = salle_catalogue.salle_porte_emplacement_dict.get(salle_id_voisine)
                    if portes_voisine is None:
                        print(f"[WARN] Aucune info de portes pour la salle voisine {nom_salle_voisine}")
                        continue

                    # On veut la PORTE OPPOSÉE dans la salle voisine
                    OPPOSITE = {0: 2, 2: 0, 1: 3, 3: 1}
                    porte_index_arrivee = OPPOSITE[porte_index_depart]

                    if not portes_voisine[porte_index_arrivee]:
                        # La salle voisine n'a pas de porte en face → mur
                        print(f"Impossible d'entrer dans {nom_salle_voisine} : pas de porte en face (mur).")
                        continue

                    # Ici, les deux salles ont bien une porte face à face → déplacement autorisé
                    joueur.x, joueur.y = new_pos

                    print(f"Déplacement dans une salle existante : {nom_salle_voisine}")

                    # Appliquer les effets d'entrée de la salle

                    effet = EffetsSalles(salle_id_voisine, salle_catalogue)
                    effet.apply_entry_effects(inventaire)

                    r, c = pixel_to_case(joueur.x, joueur.y)

                    effet.apply_over_time_effects(inventaire, (r, c))

                    print(f"[EFFET] Effets appliqués : {effet.name}")

                    salle_selectionnee = None
                    tirage_effectuee = False
                    direction_choisi = None

                    c, r = pixel_to_case(joueur.x, joueur.y)

                    contenu_complet = manoir.grid[(r, c)].all_loot

                    # Si salle jaune -> lancer la boutique
                    lancer_boutique_si_jaune(nom_salle_voisine, salle_catalogue, inventaire)

                    # Consommation de pas + logique victoire/défaite
                    inventaire.objets_consommables['Pas'].quantite -= 1
                    print(f"Pas restants : {inventaire.objets_consommables['Pas'].quantite}")

                    if plateau.get(new_pos) == "Antechamber" and inventaire.objets_consommables["Pas"].quantite >= 0:
                        print("Partie gagnée")
                        continuer = False
                    elif inventaire.objets_consommables["Pas"].quantite <= 0:
                        print("Vous n'avez plus de pas. Vous avez perdu la partie.")
                        continuer = False


                # 6) sinon -> on tente un tirage de nouvelles salles
                else:
                    # conversion en coordonnées de grille pour les règles de placement
                    row, col = pixel_to_case(x_actu, y_actu)
                    case_test = Case([row, col])

                    coord_manoir = (col, row)  # inversion obligatoire


                    # 1) enregistre l’existence des portes de la salle dans le Manoir
                    for d in range(4):
                        manoir.set_door_exists(coord_manoir, d, portes_salle[d])

                    
                    # 2) Création / récupération de la porte dans le Manoir
                    row, col = pixel_to_case(joueur.x, joueur.y)
                    cell_coord = (col, row)  # inversion obligatoire

                    # conversion direction string end index
                    porte_idx = DIRECTION_TO_PORTE_INDEX[direction]

                    cell = manoir.grid[cell_coord]
                    doorstate = cell.doorstates[porte_idx]
                    porte_temp = cell.doors[porte_idx]

                    # Génération de la porte si pas déjà générée
                    if not doorstate.generated:
                        print("Génération d'une nouvelle porte.")
                        doorstate.generated = True
                        porte_temp = Porte([row, col])
                        cell.doors[porte_idx] = porte_temp

                    # Si la salle actuelle est l'Entrance Hall -> porte forcée niveau 0
                    if plateau.get((joueur.x, joueur.y)) == "Entrance Hall":
                        porte_temp.level = 0
                        porte_temp.cout = 0
                        porte_temp.double_tour = False
                        porte_temp.ouvert = True
                        doorstate.opened = True

                    # --- vérifier si la porte est déjà ouverte ---
                    if porte_temp.ouvert:
                        print("La porte est déjà ouverte, pas de paiement nécessaire.")
                        ouverte = True
                    else:
                        # demander au joueur s'il veut ouvrir et payer
                        ouverte = porte_temp.demander_ouverture_porte(inventaire)
                        if ouverte:
                            porte_temp.ouvert = True
                            doorstate.opened = True

                    if not ouverte:
                        print("Vous laissez la porte fermée, la nouvelle salle n'est pas révélée.")
                        continue

                    # --- Tirage des salles uniquement si pas déjà fait ---
                    if not doorstate.tirage_done:
                        tirage = tirage_salle.tirage_salles(
                            coordonnees=[row, col],
                            porte_index=porte_idx,
                            case_obj=Case([row, col])
                        )
                        doorstate.tirage_results = tirage
                        doorstate.tirage_done = True
                    else:
                        tirage = doorstate.tirage_results

                    if tirage:
                        salle_selectionnee = tirage
                        print(f"Tirage effectué vers {direction} :", tirage)
                        tirage_effectuee = True
                        direction_choisi = direction
                    else:
                        print("Aucun tirage possible dans cette direction.")


        elif evenement.type == pygame.KEYDOWN and tirage_effectuee:

            #On ajoute l'option quitter
            nb_options=len(salle_selectionnee)+1

            if evenement.key==pygame.K_q:
                gerer_clavier.index_selection=(gerer_clavier.index_selection-1)%nb_options
            elif evenement.key==pygame.K_d:
                gerer_clavier.index_selection=(gerer_clavier.index_selection+1)%nb_options
            elif evenement.key==pygame.K_RETURN: #Entrée pour confirmé la salle
                choix=gerer_clavier.index_selection

                if choix==len(salle_selectionnee):
                    print("Tirage annulé")
                    salle_selectionnee=None
                    tirage_effectuee=False
                    direction_choisi=None
                    gerer_clavier.index_selection=0
                    continue    #Onreste sur la même position

                salle_choisie=salle_selectionnee[choix]
                nom_salle=salle_catalogue.salles_names_dict.get(salle_choisie,"Inconnue")
                print(f"Salle choisie : {salle_choisie} ({nom_salle})")

                #On veut affiche ce que contient cette salle
                contenu_salle=tirage_salle.generer_contenu(salle_choisie,inventaire)
                conteneurs_salle=tirage_salle.generer_conteneurs(salle_choisie)

                #On combine les 2
                contenu_complet=contenu_salle+conteneurs_salle



                print("Contenu généré :", contenu_salle)
                print("Conteneurs générés :", conteneurs_salle)
                print("Contenu complet :", contenu_complet)

                #Ajout automatique des gemmes dans l'inventaire
                for element in contenu_salle:
                    if isinstance(element,tuple):
                        nom,quantite=element
                        if nom in inventaire.objets_consommables:
                            inventaire.ajouter_objet_consommable(nom,quantite)
                            print(f"Vous avez gagné {quantite} {nom}")
                    
                    #Si on en gagne qu'un seul
                    elif isinstance(element,str):
                        if element in inventaire.objets_consommables:
                            inventaire.ajouter_objet_consommable(element,1)
                            print(f"vous avez gagné 1 {element}")
                    
                        #Si on gagne de la nourriture, on gagne des pas
                        elif isinstance(element,str) and element in inventaire.nourritures:
                            nourriture=inventaire.nourritures[element]
                            nourriture.consommer(inventaire)
                            print(f"Vous manger {element} et gagnez {nourriture.gain} pas")
                
                        #Si on gagne un objet permanent
                        elif element in inventaire.objets_permanents:
                            #Mettre l'objet permanent
                            row,col=pixel_to_case(joueur.x,joueur.y)
                            cell=manoir.grid[(col,row)]
                            cell.loot_on_ground.append(inventaire.objets_permanents[element])
                            print(f"L'objet permanent : {element} est au sol")

                prix_salle = salle_catalogue.salles_price_dict.get(salle_choisie, 0)

                #partie gemmes
                if prix_salle > 0:
                    # tentative de paiement
                    if not inventaire.depenser_gemmes(prix_salle):
                        print(
                            f"Pas assez de gemmes pour {nom_salle} : "
                            f"{prix_salle} requis, vous avez {inventaire.solde_gemmes()}."
                        )
                        # On laisse le tirage actif, le joueur peut choisir une autre salle
                        continue
                #fin partie gemmes

                if direction_choisi=="gauche":
                    joueur.deplacement(-1,0)
                elif direction_choisi=="droite":
                    joueur.deplacement(1,0)
                elif direction_choisi=="haut":
                    joueur.deplacement(0,-1)
                elif direction_choisi=="bas":
                    joueur.deplacement(0,1)

                cell_coord2 = pixel_to_case(joueur.x, joueur.y)
                col, row = cell_coord2
                manoir.grid[(row,col)].all_loot = contenu_complet
                
                #Pour chaque déplacement, on décrémente d'un pas le nombre de pas
                inventaire.objets_consommables["Pas"].quantite-=1
                print("Pas restant:{inventaire.objets_consommables['Pas'].quantite}")

                #Appliquer les effets d'entrée de la salle
                
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
        
        #Pour la sélection des items contenu dans la salle
        
        """if evenement.type==pygame.KEYDOWN and contenu_actuel:
            if evenement.key==pygame.K_z:
                #Monter 
                gerer_clavier.index_item_salle-=1
                if gerer_clavier.index_item_salle<0:
                    gerer_clavier.index_item_salle=len(contenu_actuel)-1
        
            #Descendre le rectangle
            if evenement.key==pygame.K_s:
                gerer_clavier.index_item_salle+=1
                if gerer_clavier.index_item_salle>=len(contenu_actuel):
                    gerer_clavier.index_item_salle=0"""
            
    
    return continuer,salle_selectionnee,tirage_effectuee, direction_choisi,contenu_complet

