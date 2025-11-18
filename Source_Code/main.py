import pygame
from pygame.locals import QUIT
from joueur import Joueur
from Inventory import Inventaire
from SalleManager import SalleManager
from Salles import Salle, Case
from clavier import gerer_clavier
from affichage import affichage_interface, charger_images, charger_Images_salles
from Manoir import Manoir




#Initialisation
pygame.init()
width,height=1280,540
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Blue prince')
font = pygame.font.Font(None, 36)
pygame.key.set_repeat(200, 80)

images=charger_images()
images_salles=charger_Images_salles()

#Objets et salles principaux
inventaire=Inventaire()
salle_catalogue=Salle()
tirage_salle=SalleManager(salle_catalogue)

# Blit everything to the screen
#screen.blit(background, (0, 0))

#Position du joueur au tout début du jeu
joueur=Joueur(120,480)

#On crée un plateau pour posée les salles choisie
plateau={}

# Dictionnaire pour mémoriser les portes ouvertes / fermées
portes={}

salle_catalogue = Salle()
salle_manager = SalleManager(salle_catalogue)
manoir = Manoir(salle_manager)

#Position de départ: salle d'entrée
plateau[(120,480)]="Entrance Hall"
#Salle final
plateau[(120,0)]="Antechamber"

salle_selectionnee=None
tirage_effectuee=False #Sert à dire si la tirage des salle est effectué
direction_choisi=None
dernier_contenu_salle=None
derniere_salle=None #Si c'est la dernière salle explorer on affiche le contenu de cette salle

#Boucle du jeu
continuer = True
#Etat de la partie
etat_partie=None #Gagné ou Perdu
while continuer:
    pos_joueur=(joueur.x,joueur.y)
    #Gestion du clavier
    continuer,salle_selectionnee,tirage_effectuee, direction_choisi,contenu_salle=gerer_clavier(
        joueur,tirage_salle,salle_catalogue, salle_selectionnee,tirage_effectuee,direction_choisi,plateau,inventaire, portes, manoir, dernier_contenu_salle)

    #Affichage de l'écran
    affichage_interface(screen, font, joueur, inventaire, salle_selectionnee, salle_catalogue, images, images_salles,plateau, direction_choisi, contenu_salle=dernier_contenu_salle)

    #NOuvelle position du joueur après la gestion du clavier
    nouvelle_pos=(joueur.x,joueur.y)

    #Si un tirage effectuée,  on efface l'ancienne affichage
    if tirage_effectuee:
        dernier_contenu_salle=None
    #Si une nouvelle salle est généré
    elif contenu_salle is not None:
        dernier_contenu_salle=contenu_salle
    #Si le joueur se déplace dans une salle existante, contenu de l'anciennne salle effacé
    elif nouvelle_pos!=pos_joueur and nouvelle_pos in plateau:
        dernier_contenu_salle=None
    
    #Vérification de la partie
    if inventaire.objets_consommables["Pas"].quantite<=0:
        etat_partie="défaite"
        continuer=False
    elif plateau.get((joueur.x,joueur.y))=="Antechamber":
        etat_partie="Victoire"
        continuer=False

screen.fill((0,0,0))
if etat_partie=="défaite":
    texte=font.render("Partie perdu",True,(255,0,0))
elif etat_partie=="Victoire":    
    texte=font.render("Partie gagné",True,(255,0,0))

screen.blit(texte, (width//2-200,height//2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()


