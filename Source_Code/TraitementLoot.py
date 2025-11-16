from Inventory import Inventaire, Objet, ObjetConsommable, ObjetPermanent, Nourriture
from Conteneurs import Coffre, Casier, Digspot
from RoomCell import RoomCell
from Manoir import Manoir
import pygame



class TraitementLoot : 

    def get_loot_from_container(cell : RoomCell, container, inventaire : Inventaire):

        if container.ouvert == True :

            if container.genere == False :
                container.generer_contenu(cell.room_id)
                container.genere = True
            
            loot = container.contenu
            loot_restant = loot.copy()
            
            for item in loot:
                if isinstance(item, Nourriture):
                    # Ajouter les pas equivalents dans l'inventaire
                    inventaire.objets_consommables["Pas"].changer_solde(item.gain)
                    loot_restant.remove(item)

                elif isinstance(item, ObjetConsommable): #Ajoute l'objet à l'inventaire
                    inventaire.objets_consommables[item.nom].changer_solde(item.quantite)
                    loot_restant.remove(item)

                elif isinstance(item, ObjetPermanent): # Ajoute l'objet permanent
                    inventaire.objets_permanents[item.nom].debloquer()
                    loot_restant.remove(item)
                    


        return loot_restant

    # Prendre le loot au sol dans une salle

    def take_loot_from_room(cell : RoomCell, inventaire : Inventaire):
        
        loot = cell.loot_on_ground
        loot_restant = loot.copy()

        for item in loot:
            if isinstance(item, Nourriture):
                # Ajouter les pas equivalents dans l'inventaire
                inventaire.objets_consommables["Pas"].changer_solde(item.gain)
                loot_restant.remove(item)

            elif isinstance(item, ObjetConsommable): #Ajoute l'objet à l'inventaire
                inventaire.objets_consommables[item.nom].changer_solde(item.quantite)
                loot_restant.remove(item)

            elif isinstance(item, ObjetPermanent): # Ajoute l'objet permanent
                inventaire.objets_permanents[item.nom].debloquer()
                loot_restant.remove(item)
            
            elif isinstance(item, (Coffre, Casier, Digspot)):

                # siLe conteneur est fermé :
                if not item.ouvert:

                    # UI : demander à l'utilisateur
                    doit_ouvrir = TraitementLoot.demander_ouverture_conteneur(item, inventaire)


                    if not doit_ouvrir:
                        # On laisse l'objet au sol
                        continue

                    # Sinon : tentative d'ouverture (selon type)
                    ouvert = item.ouvrir(inventaire)
                   
                    if not ouvert:
                        # Joueur n'a pas marteau/clés/pelle
                        print(f"Impossible d'ouvrir {type(item).__name__}")
                        continue

                # --- 2) Si ouvert, générer le contenu si nécessaire ---
                if not item.genere:
                    if isinstance(item, Digspot):
                        item.generer_contenu(cell.room_id, inventaire)
                    else:
                        item.generer_contenu(cell.room_id)
                    item.genere = True

                # --- 3) Distribuer le contenu ---
                for contenu in item.contenu:
                    if isinstance(contenu, tuple):
                        nom, q = contenu
                        inventaire.ajouter_objet_consommable(nom, q)
                    elif isinstance(contenu, Nourriture):
                        inventaire.objets_consommables["Pas"].changer_solde(contenu.gain)
                    elif isinstance(contenu, ObjetPermanent):
                        inventaire.debloquer_permanent(contenu.nom)

                # Le conteneur est vidé -> on retire du sol
                loot_restant.remove(item)
                continue

        cell.loot_on_ground = loot_restant


@staticmethod
def demander_ouverture_conteneur(container, inventaire):
    """
    Popup Pygame : demande au joueur s'il veut ouvrir le conteneur.
    Le texte dépend automatiquement du type de conteneur.
    """

    pygame.init()

    # Fenêtre
    WIDTH, HEIGHT = 500, 240
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Confirmation d'ouverture")

    font = pygame.font.SysFont(None, 28)

    # ---- TEXTE SPÉCIFIQUE SELON LE TYPE DE CONTENEUR ----
    nom = type(container).__name__

    if nom == "Casier":
        texte_str = "Voulez-vous ouvrir le casier pour 1 clé ?"

    elif nom == "Coffre":
        hammer = inventaire.objets_permanents["Hammer"]
        if hammer.obtenu:
            texte_str = "Voulez-vous ouvrir le coffre gratuitement (Marteau Débloqué) ?"
        else:
            texte_str = "Voulez-vous ouvrir le coffre pour 1 clé ?"

    elif nom == "Digspot":
        texte_str = "Voulez-vous creuser ?"

    texte = font.render(texte_str, True, (255, 255, 255))


    # Boutons
    bouton_oui = pygame.Rect(80, 150, 150, 50)
    bouton_non = pygame.Rect(270, 150, 150, 50)

    clock = pygame.time.Clock()

    # ---- BOUCLE DU POPUP ----
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_oui.collidepoint(event.pos):
                    pygame.quit()
                    return True

                if bouton_non.collidepoint(event.pos):
                    pygame.quit()
                    return False

        # ---- AFFICHAGE ----
        screen.fill((30, 30, 30))

        # Texte
        screen.blit(
            texte,
            (WIDTH // 2 - texte.get_width() // 2, 60)
        )

        # Boutons OUI / NON
        pygame.draw.rect(screen, (0, 150, 0), bouton_oui)
        pygame.draw.rect(screen, (150, 0, 0), bouton_non)

        txt_oui = font.render("OUI", True, (255, 255, 255))
        txt_non = font.render("NON", True, (255, 255, 255))

        screen.blit(txt_oui, (bouton_oui.x + 55, bouton_oui.y + 12))
        screen.blit(txt_non, (bouton_non.x + 50, bouton_non.y + 12))

        pygame.display.flip()
        clock.tick(30)

