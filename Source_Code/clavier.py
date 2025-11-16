import pygame
from Salles import Case

def gerer_clavier(joueur,tirage_salle,salle_catalogue, salle_selectionnee,tirage_effectuee,direction_choisi,plateau,inventaire):
    continuer=True
    #Déplacement du joueur et sélection de la pièce aléatoire avec le clavier
    for evenement in pygame.event.get():
        if evenement.type==pygame.QUIT:
            continuer=False

        if evenement.type==pygame.KEYDOWN and not tirage_effectuee:
            direction=None
            if evenement.key==pygame.K_q or evenement.key==pygame.K_LEFT:
                direction="gauche"
            elif evenement.key==pygame.K_d or evenement.key==pygame.K_RIGHT:
                direction="droite"
            elif evenement.key==pygame.K_z or evenement.key==pygame.K_UP:
                direction="haut"
            elif evenement.key==pygame.K_s or evenement.key==pygame.K_DOWN:
                direction="bas"

            #Si une des touches de déplacement est appuyé
            if direction:
                #On enregistre l'ancienne position du joueur
                x_old, y_old=joueur.x,joueur.y

                if direction=="gauche":
                    new_pos=(x_old-60,y_old)
                elif direction=="droite":
                    new_pos=(x_old+60,y_old)
                elif direction=="haut":
                    new_pos=(x_old,y_old-60)
                elif direction=="bas":
                    new_pos=(x_old,y_old+60)

                #Limites de la zone de jeu
                limite_gauche=0
                limite_droite=300-60
                limite_haut=0
                limite_bas=480
                
                new_pos_x,new_pos_y=new_pos
                if new_pos_x<limite_gauche or new_pos_x>limite_droite or new_pos_y<limite_haut or new_pos_y>limite_bas:
                    print("Vous êtes à la limite de la zone")
                    continue

                #Vérifie si la salle existe déjà sur le plateau
                if new_pos in plateau:
                    #Salle déjà posée: on se déplace sans tirage
                    joueur.x,joueur.y=new_pos
                    print(f"Déplacement dans une salle existante:{plateau[new_pos]}")
                    salle_selectionnee=None
                    tirage_effectuee=False
                    direction_choisi=None

                    #Pour chaque déplacement, on décrémente d'un pas le nombre de pas
                    inventaire.objets_consommables["Pas"].quantite-=1
                    print("Pas restant:{inventaire.objets_consommables['Pas'].quantite}")

                    #Si on attaint l'antichambre
                    if plateau.get(new_pos)=="Antechamber" and inventaire.objets_consommables["Pas"].quantite>=0:
                        print("Partie gagné")
                        continuer=False
                
                    #Si plus de pas = partie perdue
                    elif inventaire.objets_consommables["Pas"].quantite<=0:
                        print("VOus n'avez plus de pas.Vous avez perdue la partie") 
                        continuer=False
                else:
                    case_test = Case([120,480])

                    tirage=tirage_salle.tirage_salles(coordonnees=[120,480], porte_index=2, case_obj=case_test)

                    if tirage :
                        salle_selectionnee=tirage
                        print("Tirage effectuee à ({direction})", tirage)
                        tirage_effectuee=True
                        direction_choisi=direction
                        gerer_clavier.index_selection=0
                    else:
                        print("Aucun tirage")

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

                if direction_choisi=="gauche":
                    joueur.deplacement(-1,0)
                elif direction_choisi=="droite":
                    joueur.deplacement(1,0)
                elif direction_choisi=="haut":
                    joueur.deplacement(0,-1)
                elif direction_choisi=="bas":
                    joueur.deplacement(0,1)

                #Pour chaque déplacement, on décrémente d'un pas le nombre de pas
                inventaire.objets_consommables["Pas"].quantite-=1
                print("Pas restant:{inventaire.objets_consommables['Pas'].quantite}")

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

                    #Réinitialisation de tous les état
                salle_selectionnee=None
                tirage_effectuee=False
                direction_choisi=None
                gerer_clavier.index_selection=0
    
    return continuer,salle_selectionnee,tirage_effectuee, direction_choisi
