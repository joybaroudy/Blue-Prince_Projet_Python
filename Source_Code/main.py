import pygame
from pygame.locals import QUIT
from joueur import Joueur
from Inventory import Inventaire
from SalleManager import SalleManager
from Salles import Salle, Case
from clavier import gerer_clavier
from affichage import affichage_interface, charger_images, charger_Images_salles

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

#Position de départ: salle d'entrée
plateau[(120,480)]="Entrance_hall"
#Salle final
plateau[(120,0)]="Antechamber"

salle_selectionnee=None
tirage_effectuee=False #Sert à dire si la tirage des salle est effectué
direction_choisi=None

#Boucle du jeu
continuer = True
while continuer:
    #Gestion du clavier
    continuer,salle_selectionnee,tirage_effectuee, direction_choisi=gerer_clavier(
        joueur,tirage_salle,salle_catalogue, salle_selectionnee,tirage_effectuee,direction_choisi,plateau)

    #Affichage de l'écran
    affichage_interface(screen, font, joueur, inventaire, salle_selectionnee, salle_catalogue, images, images_salles,plateau)

pygame.quit()