import pygame
import clavier
from Conteneurs import Casier, Coffre, Digspot
from Boutique import Boutique
from Inventory import Inventaire, ObjetConsommable, ObjetPermanent, Nourriture

def charger_Images_salles():
    return{ #Salle bleue
            "The Foundation":pygame.image.load("images/Images_Chambres/Blue/The_Foundation_Icon.png").convert(),
            "Entrance_hall":pygame.image.load("images/Images_Chambres/Blue/Entrance_Hall_Icon.png"),
            "Spare Room":pygame.image.load("images/Images_Chambres/Blue/Spare_Room_Icon.png"),
            "Rotunda": pygame.image.load("images/Images_Chambres/Blue/Rotunda_Icon.png"),
            "Parlor": pygame.image.load("images/Images_Chambres/Blue/Parlor_Icon.png"),
            "Billiard Room": pygame.image.load("images/Images_Chambres/Blue/Billiard_Room_Icon.png"),
            "Gallery": pygame.image.load("images/Images_Chambres/Blue/Gallery_Icon.png"),
            "Room 8": pygame.image.load("images/Images_Chambres/Blue/Room_8_Icon.png"),
            "Closet": pygame.image.load("images/Images_Chambres/Blue/Closet_Icon.png"),
            "Walk-in Closet": pygame.image.load("images/Images_Chambres/Blue/Walk-in_Closet_Icon.png"),
            "Attic": pygame.image.load("images/Images_Chambres/Blue/Attic_Icon.png"),
            "Storeroom": pygame.image.load("images/Images_Chambres/Blue/Storeroom_Icon.png"),
            "Nook": pygame.image.load("images/Images_Chambres/Blue/Nook_Icon.png"),
            "Garage": pygame.image.load("images/Images_Chambres/Blue/Garage_Icon.png"),
            "Music Room": pygame.image.load("images/Images_Chambres/Blue/Music_Room_Icon.png"),
            "Locker Room": pygame.image.load("images/Images_Chambres/Blue/Locker_Room_Icon.png"),
            "Den": pygame.image.load("images/Images_Chambres/Blue/Den_Icon.png"),
            "Wine Cellar": pygame.image.load("images/Images_Chambres/Blue/Wine_Cellar_Icon.png"),
            "Trophy Room": pygame.image.load("images/Images_Chambres/Blue/Trophy_Room_Icon.png"),
            "Ballroom": pygame.image.load("images/Images_Chambres/Blue/Ballroom_Icon.png"),
            "Pantry": pygame.image.load("images/Images_Chambres/Blue/Pantry_Icon.png"),
            "Rumpus Room": pygame.image.load("images/Images_Chambres/Blue/Rumpus_Room_Icon.png"),
            "Vault": pygame.image.load("images/Images_Chambres/Blue/Vault_Icon.png"),
            "Office": pygame.image.load("images/Images_Chambres/Blue/Office_Icon.png"),
            "Drawing Room": pygame.image.load("images/Images_Chambres/Blue/Drawing_Room_Icon.png"),
            "Study": pygame.image.load("images/Images_Chambres/Blue/Study_Icon.png"),
            "Library": pygame.image.load("images/Images_Chambres/Blue/Library_Icon.png"),
            "Chamber of Mirrors": pygame.image.load("images/Images_Chambres/Blue/Chamber_of_Mirrors_Icon.png"),
            "The Pool": pygame.image.load("images/Images_Chambres/Blue/The_Pool_Icon.png"),
            "Drafting Studio": pygame.image.load("images/Images_Chambres/Blue/Drafting_Studio_Icon.png"),
            "Utility Closet": pygame.image.load("images/Images_Chambres/Blue/Utility_Closet_Icon.png"),
            "Boiler Room": pygame.image.load("images/Images_Chambres/Blue/Boiler_Room_Icon.png"),
            "Pump Room": pygame.image.load("images/Images_Chambres/Blue/Pump_Room_Icon.png"),
            "Security": pygame.image.load("images/Images_Chambres/Blue/Security_Icon.png"),
            "Workshop": pygame.image.load("images/Images_Chambres/Blue/Workshop_Icon.png"),
            "Laboratory": pygame.image.load("images/Images_Chambres/Blue/Laboratory_Icon.png"),
            "Sauna": pygame.image.load("images/Images_Chambres/Blue/Sauna_Icon.png"),
            "Coat Check": pygame.image.load("images/Images_Chambres/Blue/Coat_Check_Icon.png"),
            "Mail Room": pygame.image.load("images/Images_Chambres/Blue/Mail_Room_Icon.png"),
            "Freezer": pygame.image.load("images/Images_Chambres/Blue/Freezer_Icon.png"),
            "Dining Room": pygame.image.load("images/Images_Chambres/Blue/Dining_Room_Icon.png"),
            "Observatory": pygame.image.load("images/Images_Chambres/Blue/Observatory_Icon.png"),
            "Conference Room": pygame.image.load("images/Images_Chambres/Blue/Conference_Room_Icon.png"),
            "Aquarium": pygame.image.load("images/Images_Chambres/Blue/Aquarium_Icon.png"),
            "Antechamber": pygame.image.load("images/Images_Chambres/Blue/Antechamber_Icon.png"),
        
            #Salle violet
            "Bedroom": pygame.image.load("images/Images_Chambres/Purple/Bedroom_Icon.png"),
            "Boudoir": pygame.image.load("images/Images_Chambres/Purple/Boudoir_Icon.png"),
            "Guest Bedroom": pygame.image.load("images/Images_Chambres/Purple/Guest_Bedroom_Icon.png"),
            "Nursery": pygame.image.load("images/Images_Chambres/Purple/Nursery_Icon.png"),
            "Servant's Quarters": pygame.image.load("images/Images_Chambres/Purple/Servants_Quarters_Icon.png"),
            "Bunk Room": pygame.image.load("images/Images_Chambres/Purple/Bunk_Room_Icon.png"),
            "Her Ladyship's Chamber": pygame.image.load("images/Images_Chambres/Purple/Her_Ladyships_Chamber_Icon.png"),
            "Master Bedroom": pygame.image.load("images/Images_Chambres/Purple/Master_Bedroom_Icon.png"),
        
            #Salle Orange
            "Hallway": pygame.image.load("images/Images_Chambres/Orange/Hallway_Icon.png"),
            "West Wing Hall": pygame.image.load("images/Images_Chambres/Orange/West_Wing_Hall_Icon.png"),
            "East Wing Hall": pygame.image.load("images/Images_Chambres/Orange/East_Wing_Hall_Icon.png"),
            "Corridor": pygame.image.load("images/Images_Chambres/Orange/Corridor_Icon.png"),
            "Passageway": pygame.image.load("images/Images_Chambres/Orange/Passageway_Icon.png"),
            "Secret Passage": pygame.image.load("images/Images_Chambres/Orange/Secret_Passage_Icon.png"),
            "Foyer": pygame.image.load("images/Images_Chambres/Orange/Foyer_Icon.png"),
            "Great Hall": pygame.image.load("images/Images_Chambres/Orange/Great_Hall_Icon.png"),

            #Salle Vert
            "Terrace": pygame.image.load("images/Images_Chambres/Green/Terrace_Icon.png"),
            "Patio": pygame.image.load("images/Images_Chambres/Green/Patio_Icon.png"),
            "Courtyard": pygame.image.load("images/Images_Chambres/Green/Courtyard_Icon.png"),
            "Cloister": pygame.image.load("images/Images_Chambres/Green/Cloister_Icon.png"),
            "Veranda": pygame.image.load("images/Images_Chambres/Green/Veranda_Icon.png"),
            "Greenhouse": pygame.image.load("images/Images_Chambres/Green/Greenhouse_Icon.png"),
            "Morning Room": pygame.image.load("images/Images_Chambres/Green/Morning_Room_Icon.png"),
            "Secret Garden": pygame.image.load("images/Images_Chambres/Green/Secret_Garden_Icon.png"),

            #Salle Jaune
            "Commissary": pygame.image.load("images/Images_Chambres/Yellow/Commissary_Icon.png"),
            "Kitchen": pygame.image.load("images/Images_Chambres/Yellow/Kitchen_Icon.png"),
            "Locksmith": pygame.image.load("images/Images_Chambres/Yellow/Locksmith_Icon.png"),
            "Showroom": pygame.image.load("images/Images_Chambres/Yellow/Showroom_Icon.png"),
            "Laundry Room": pygame.image.load("images/Images_Chambres/Yellow/Laundry_Room_Icon.png"),
            "Bookshop": pygame.image.load("images/Images_Chambres/Yellow/Bookshop_Icon.png"),
            "The Armory": pygame.image.load("images/Images_Chambres/Yellow/The_Armory_Icon.png"),
            "Mount Holly Gift Shop": pygame.image.load("images/Images_Chambres/Yellow/Mount_Holly_Gift_Shop_Icon.png"),

            #Salle rouge
            "Lavatory": pygame.image.load("images/Images_Chambres/Red/Lavatory_Icon.png"),
            "Chapel": pygame.image.load("images/Images_Chambres/Red/Chapel_Icon.png"),
            "Maid's Chamber": pygame.image.load("images/Images_Chambres/Red/Maids_Chamber_Icon.png"),
            "Archives": pygame.image.load("images/Images_Chambres/Red/Archives_Icon.png"),
            "Gymnasium": pygame.image.load("images/Images_Chambres/Red/Gymnasium_Icon.png"),
            "Darkroom": pygame.image.load("images/Images_Chambres/Red/Darkroom_Icon.png"),
            "Weight Room": pygame.image.load("images/Images_Chambres/Red/Weight_Room_Icon.png"),
            "Furnace": pygame.image.load("images/Images_Chambres/Red/Furnace_Icon.png"),
}

def charger_images():
    return{
        #Faudra faire attention avec les lien de sources d'images
        #Salle à placé dans la partie jeu au tout début
        "Antechamber": pygame.image.load("Image_initial/Antechamber_Icon.webp").convert(),
        "entrance_room":pygame.image.load("Image_initial/entrance_hall.png").convert(),

        #Objet consommable dans l'inventaire
        "pas_img":pygame.image.load("Image_initial/pas.jpeg").convert(),
        "piece_img":pygame.image.load("Image_initial/pieces.png").convert(),
        "gemme_img":pygame.image.load("Image_initial/gemme.png").convert(),
        "cle_img":pygame.image.load("Image_initial/cle.png").convert(),
        "des_img":pygame.image.load("Image_initial/des.png").convert()
    }

#On afiche la direction du joueur qu'il souhaite aller
def afficher_direction(screen, direction_choisi,font,joueur):
    if not direction_choisi:
        return
    
    #Position du joueur pour dessiner la flèche
    x,y=joueur.x+30,joueur.y+30
    couleur=(0,255,0)
    taille=15

    fleche=[]
    #Forme de la flèche selon la direction
    if direction_choisi=="haut":
        fleche=[(x,y-taille),(x-taille,y+taille),(x+taille,y+taille)]
    elif direction_choisi=="bas":
        fleche=[(x,y+taille),(x-taille,y-taille),(x+taille,y-taille)]
    elif direction_choisi=="gauche":
        fleche=[(x-taille,y),(x+taille,y-taille),(x+taille,y+taille)]
    elif direction_choisi=="droite":
        fleche=[(x+taille,y),(x-taille,y-taille),(x-taille,y+taille)]
    else:
        return
    
    #Dessine le triangle
    pygame.draw.polygon(screen,couleur,fleche)

def affichage_interface(screen, font, joueur, inventaire, salle_selectionnee, salle_catalogue, images, images_salles,plateau,direction_choisi,contenu_salle=None):

    ecran_jeu=300
    width,height=screen.get_size()

    #zone_jeu
    game_zone=pygame.Rect(0,0,ecran_jeu,height)
    #Inventaire
    inventaire_zone=pygame.Rect(ecran_jeu,0, height-ecran_jeu,height)
    screen.fill((0,0,0))

    # Fond
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #Dessiner 2 rectangle l'un représente le jeu et l'autre l'inventaire
    pygame.draw.rect(screen,(0,0,0),game_zone)
    pygame.draw.rect(screen,(255,255,255),inventaire_zone)

    #On affiche les salles contenu dans le dictionnaire plateau qu'on a crée dans l'écran jeu
    for (x,y), nom_salle in plateau.items():
        if nom_salle in images_salles:
            salle_img=pygame.transform.scale(images_salles[nom_salle],(60,60))
            screen.blit(salle_img,(x,y))

    #Dans l'inventaire
    #Texte dans l'inventaire
    text = font.render("Inventaire:", True, (0, 0, 0))
    #Position du texte
    screen.blit(background, (ecran_jeu, 0))
    screen.blit(text, (ecran_jeu+20, 20))

    #Si on obtient des objets permanents, on l'affiche dans l'inventaire
    y_permanent=50
    x_permanent=ecran_jeu+20

    for nom,obj in inventaire.objets_permanents.items():
        if obj.obtenu:
            texte=font.render(f"{nom}",True,(0,0,0))
            screen.blit(texte,(x_permanent+10,y_permanent))
            y_permanent+=20

    entree=font.render("Salle entrée:",True,(0,0,0))
    screen.blit(entree, (ecran_jeu+20, height//2-80))

    #Inital
    objet=[("Pas",images["pas_img"]),
           ("Pièces",images["piece_img"]),
           ("Gemmes",images["gemme_img"]),
           ("Clés",images["cle_img"]),
           ("Dés",images["des_img"])]
    
    #Score initial
    for i,(nom,image) in enumerate(objet):
        image=pygame.transform.scale(image, (28,28))
        y=30+i*30
        screen.blit(image,(width-120,y))
        quantite_init=inventaire.objets_consommables[nom].quantite
        texte=font.render(str(quantite_init),True,(0,0,0))
        screen.blit(texte,(width-90,y))
    
    

    #Placement de la salle finale
    finale_room=pygame.transform.scale(images["Antechamber"],(60,60))
    screen.blit(finale_room, (120, 0))

    #Placement de la salle initial
    entrance_hall=pygame.transform.scale(images["entrance_room"],(60,60))
    screen.blit(entrance_hall, (120, 480))
    
    #Lorsqu'un tirage est fait
    if salle_selectionnee:
        Salle_tiree=font.render("Tirage de salles:",True,(0,0,0))
        screen.blit(Salle_tiree, (ecran_jeu+20, (height//2-80)+40))

        Instruction=font.render("Q et D pour bouger la molette, R pour refaire le tirage",True,(0,0,0))
        screen.blit(Instruction, (ecran_jeu+20, (height//2-80)+80))
        
        pos_y=(height//2-80)+120
        pos_x=ecran_jeu+20

        #On affiche les images des salles tirées dans la zone inventaire en bas à droite
        for i,salle_id in enumerate(salle_selectionnee):
            salle_nom=salle_catalogue.salles_names_dict.get(salle_id,"Inconnue")
            img=pygame.transform.scale(images_salles[salle_nom], (160,160))

            #Position dans l'inventaire
            x=pos_x+i*200
            y=pos_y
            screen.blit(img, (x,y))

            #Partie gemmes
            prix = salle_catalogue.salles_price_dict.get(salle_id, 0)
            if prix > 0:
                texte_prix = font.render(f"{prix} gemmes", True, (150, 0, 0))
            else:
                texte_prix = font.render("Gratuit", True, (0, 120, 0))

            
            screen.blit(texte_prix, (x, y + 165))
            #fin partie gemmes


            # Si c’est la salle actuellement sélectionnée, on dessine un cadre rouge
            if i == getattr(clavier.gerer_clavier, "index_selection", 0):
                pygame.draw.rect(screen, (255, 0, 0), (x - 5, y - 5, 170, 170), 4)

        texte_quitter=font.render("Quitter",True,(255,0,0))
        x_quitter=pos_x+len(salle_selectionnee)*200
        y_quitter=pos_y+60
        screen.blit(texte_quitter,(x_quitter,y_quitter))

        #On adapte la taille du texte en fonction de la taille du rectangle
        largeur_texte, hauteur_texte=texte_quitter.get_size()

        # Si c’est la salle actuellement sélectionnée, on dessine un cadre rouge
        if getattr(clavier.gerer_clavier, "index_selection", 0)==len(salle_selectionnee):
            pygame.draw.rect(screen, (255, 0, 0), (x_quitter-5, y_quitter, largeur_texte+10, hauteur_texte+10), 3)

            """#On ajoute le nom des salles en dessous
            texte_salle=font.render(f"{salle_nom}",True, (0,0,0))
            screen.blit(texte_salle,(x, y+105))"""
    
    joueur.position_initial(screen)
    if direction_choisi:
        afficher_direction(screen,direction_choisi,font,joueur)
    
    
       # Afficher le contenu de la salle s'il contient quelque chose
    if contenu_salle and not salle_selectionnee:
        titre = font.render("Contenu de la salle :", True, (0, 0, 0))
        screen.blit(titre, (320, 300))

        pos_y = 330

        for element in contenu_salle:

            # 1) Loot simple : tuples ("Pièces", 10), ("Gemmes", 2), etc.
            if isinstance(element, tuple):
                nom, quantite = element
                texte = font.render(f"{nom} : {quantite}", True, (0, 0, 0))
                screen.blit(texte, (320, pos_y))
                pos_y += 25

            # 2) Conteneurs : Coffre, Casier, Digspot
            elif isinstance(element, (Coffre, Casier, Digspot)):
                nom_type = element.__class__.__name__
                etat = "ouvert" if element.ouvert else "fermé"
                texte = font.render(f"Conteneur : {nom_type} ({etat})", True, (0, 0, 0))
                screen.blit(texte, (320, pos_y))
                pos_y += 25

                # Si le conteneur est ouvert et que son contenu est généré,
                # on affiche ce qu'il contient, indenté.
                if element.ouvert and element.genere and element.contenu:
                    for contenu in element.contenu:
                        # cas tuple ("Pièces", 10) ou ("Shovel", 1)
                        if isinstance(contenu, tuple):
                            nom_c, q = contenu
                            ligne = f"- {nom_c} : {q}"
                        # Nourriture sous forme d'objet
                        elif isinstance(contenu, Nourriture):
                            ligne = f"- {contenu.nom} (+{contenu.gain} pas)"
                        # Objet permanent sous forme d'objet
                        elif isinstance(contenu, ObjetPermanent):
                            ligne = f"- {contenu.nom} (permanent)"
                        else:
                            ligne = f"- {str(contenu)}"

                        texte_contenu = font.render(ligne, True, (80, 80, 80))
                        screen.blit(texte_contenu, (340, pos_y))
                        pos_y += 20

            # 3) Boutique dans la salle
            elif isinstance(element, Boutique):
                texte = font.render("Boutique disponible (appuyer sur T pour l'ouvrir)", True, (0, 0, 150))
                screen.blit(texte, (320, pos_y))
                pos_y += 25

            # 4) Loot simple sous forme de string ("Pomme", "Shovel", etc.)
            elif isinstance(element, str):
                texte = font.render(element, True, (0, 0, 0))
                screen.blit(texte, (320, pos_y))
                pos_y += 25

            # 5) Fallback générique
            else:
                texte = font.render(str(element), True, (0, 0, 0))
                screen.blit(texte, (320, pos_y))
                pos_y += 25

        # Message pour ramasser
        hint = font.render("Presser T pour ramasser", True, (0, 100, 0))
        screen.blit(hint, (320, pos_y + 20))


    pygame.display.flip()
