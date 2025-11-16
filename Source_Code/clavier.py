import pygame
from Salles import Case

def gerer_clavier(joueur,tirage_salle,salle_catalogue, salle_selectionnee,tirage_effectuee,direction_choisi,plateau):
    continuer=True
    #Déplacement du joueur et sélection de la pièce aléatoire avec le clavier
    for evenement in pygame.event.get():
        if evenement.type==pygame.QUIT:
            continuer=False

        if evenement.type==pygame.KEYDOWN and not tirage_effectuee:
            direction=None
            if evenement.key==pygame.K_q:
                direction="gauche"
            elif evenement.key==pygame.K_d:
                direction="droite"
            elif evenement.key==pygame.K_z:
                direction="haut"
            elif evenement.key==pygame.K_s:
                direction="bas"

            #Si une des touches de déplacement est appuyé
            if direction:
                #On enregistre la position actuelle du joueur
                x_actu, y_actu=joueur.x,joueur.y

                if direction=="gauche":
                    new_pos=(x_actu-60,y_actu)
                elif direction=="droite":
                    new_pos=(x_actu+60,y_actu)
                elif direction=="haut":
                    new_pos=(x_actu,y_actu-60)
                elif direction=="bas":
                    new_pos=(x_actu,y_actu+60)
                
                #Vérifie si la salle existe déjà sur le plateau
                if new_pos in plateau:
                    #Salle déjà posée: on se déplace sans tirage
                    joueur.x,joueur.y=new_pos
                    print(f"Déplacement dans une salle existante:{plateau[new_pos]}")
                    salle_selectionnee=None
                    tirage_effectuee=False
                    direction_choisi=None
                else:
                    case_test = Case([120,480])

                    tirage=tirage_salle.tirage_salles(coordonnees=[120,480], porte_index=2, case_obj=case_test)

                    if tirage :
                        salle_selectionnee=tirage
                        print("Tirage effectuee à ({direction})", tirage)
                        tirage_effectuee=True
                        direction_choisi=direction
                    else:
                        print("Aucun tirage")

        elif evenement.type == pygame.KEYDOWN and tirage_effectuee:
            choix=None
            if evenement.key==pygame.K_q:
                 choix=0
            elif evenement.key==pygame.K_s:
                choix=1
            elif evenement.key==pygame.K_d:
                choix=2

            if choix is not None and salle_selectionnee and choix<len(salle_selectionnee):
                salle_choisie=salle_selectionnee[choix]
                nom_salle=salle_catalogue.salles_names_dict.get(salle_choisie,"Inconnue")
                print(f"Salle choisie : {salle_choisie} ({nom_salle})")

                #On enregistre l'ancienne position du joueur
                x_old, y_old=joueur.x,joueur.y

                if direction_choisi=="gauche":
                    joueur.deplacement(-1,0)
                elif direction_choisi=="droite":
                    joueur.deplacement(1,0)
                elif direction_choisi=="haut":
                    joueur.deplacement(0,-1)
                elif direction_choisi=="bas":
                    joueur.deplacement(0,1)
                
                #On enregistre les nouvelles position du joueur=emplacement de la salle choisi
                new_pos_x,new_pos_y=joueur.x,joueur.y

                #On enregistre la salle choisie sur le plateau
                plateau[(new_pos_x,new_pos_y)]=nom_salle

                    #Réinitialisation de tous les état
                salle_selectionnee=None
                tirage_effectuee=False
                direction_choisi=None
    
    return continuer,salle_selectionnee,tirage_effectuee, direction_choisi
