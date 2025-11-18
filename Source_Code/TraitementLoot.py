from Inventory import Inventaire, Objet, ObjetConsommable, ObjetPermanent, Nourriture
from Conteneurs import Conteneur, Coffre, Casier, Digspot
from RoomCell import RoomCell
from Manoir import Manoir
import pygame
from Boutique import Boutique
from TraitementBoutique import TraitementBoutique



class TraitementLoot : 

    def get_loot_from_container(cell : RoomCell, container : Conteneur, inventaire : Inventaire):

        if container.ouvert == True :

            if container.genere == False :
                if isinstance(container, Digspot):
                    container.generer_contenu(cell.room_id)
                else:
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
    def take_loot_from_room(cell: RoomCell, inventaire: Inventaire, screen, room_ID="ID2"):
        
        loot = cell.all_loot
        loot_restant = loot.copy()

        # ID de salle pour générer le contenu des conteneurs
        if cell.room_id is not None:
            room_ID = cell.room_id

        for item in loot:
            # --- 1) Loot au format tuple ("Pièces", 10) ---
            if isinstance(item, tuple):
                nom, quantite = item

                # Consommables (Pièces, Gemmes, Clés, Dés, Pas, etc.)
                if nom in inventaire.objets_consommables:
                    inventaire.ajouter_objet_consommable(nom, quantite)
                    loot_restant.remove(item)

                # Nourriture stockée comme ("Pomme", 1), etc.
                elif nom in inventaire.nourritures:
                    nourriture = inventaire.nourritures[nom]
                    for _ in range(quantite):
                        nourriture.consommer(inventaire)
                    loot_restant.remove(item)

                # Objet permanent stocké comme ("Shovel", 1)
                elif nom in inventaire.objets_permanents:
                    inventaire.debloquer_permanent(nom)
                    loot_restant.remove(item)

            # --- 2) Loot au format string simple ("Pomme", "Shovel", ...) ---
            elif isinstance(item, str):
                # Consommable unique
                if item in inventaire.objets_consommables:
                    inventaire.ajouter_objet_consommable(item, 1)
                    loot_restant.remove(item)

                # Nourriture → donne des pas
                elif item in inventaire.nourritures:
                    nourriture = inventaire.nourritures[item]
                    nourriture.consommer(inventaire)
                    loot_restant.remove(item)

                # Objet permanent
                elif item in inventaire.objets_permanents:
                    inventaire.debloquer_permanent(item)
                    loot_restant.remove(item)

            # --- 3) Conteneurs : Coffre / Casier / Digspot ---
            elif isinstance(item, (Coffre, Casier, Digspot)):

                # 3.a) PREMIER T : conteneur fermé -> on l'ouvre et on génère le contenu,
                # mais on NE ramasse PAS encore.
                if not item.ouvert:
                    doit_ouvrir = TraitementLoot.demander_ouverture_conteneur(item, inventaire, screen)

                    if not doit_ouvrir:
                        # le joueur refuse -> on laisse le conteneur au sol
                        continue

                    ouvert = item.ouvrir(inventaire)
                    if not ouvert:
                        print(f"Impossible d'ouvrir {type(item).__name__} (pas les bons objets).")
                        continue

                    # Générer le contenu si ce n'est pas déjà fait
                    if not item.genere:
                        if isinstance(item, Digspot):
                            item.generer_contenu(room_ID, inventaire)
                        else:
                            item.generer_contenu(room_ID)
                        item.genere = True

                    # Afficher le contenu pour que le joueur sache ce qu'il y a dedans
                    print(f"{type(item).__name__} ouvert. Contenu visible mais non ramassé : {item.contenu}")

                    # On laisse le conteneur au sol, avec son contenu
                    continue

                # 3.b) DEUXIÈME T (et suivants) : conteneur déjà ouvert -> on ramasse le contenu
                else:
                    # sécurité : si jamais contenu pas généré
                    if not item.genere:
                        if isinstance(item, Digspot):
                            item.generer_contenu(room_ID, inventaire)
                        else:
                            item.generer_contenu(room_ID)
                        item.genere = True

                    if not item.contenu:
                        print(f"{type(item).__name__} déjà vide.")
                        # on peut enlever le conteneur du sol s'il est définitivement vide
                        loot_restant.remove(item)
                        continue

                    # Distribuer le contenu du conteneur
                    for contenu in list(item.contenu):
                        # tuples ("Pièces", 10), ("Gemmes", 2), ("Shovel", 1), ...
                        if isinstance(contenu, tuple):
                            nom, quantite = contenu

                            if nom in inventaire.objets_consommables:
                                inventaire.ajouter_objet_consommable(nom, quantite)

                            elif nom in inventaire.nourritures:
                                nourriture = inventaire.nourritures[nom]
                                for _ in range(quantite):
                                    nourriture.consommer(inventaire)

                            elif nom in inventaire.objets_permanents:
                                inventaire.debloquer_permanent(nom)

                        # Nourriture en objet direct
                        elif isinstance(contenu, Nourriture):
                            contenu.consommer(inventaire)

                        # Objet permanent direct
                        elif isinstance(contenu, ObjetPermanent):
                            inventaire.debloquer_permanent(contenu.nom)

                    # Une fois vidé, on enlève le conteneur du sol
                    item.contenu.clear()
                    loot_restant.remove(item)

            # --- 4) Boutique ---
            elif isinstance(item, Boutique):
                tshop = TraitementBoutique(item)
                tshop.traitement_boutique(inventaire)
                loot_restant.remove(item)

        # Mise à jour du loot restant dans la salle
        cell.all_loot = loot_restant
        return loot_restant




    @staticmethod
    def demander_ouverture_conteneur(container, inventaire, screen):
        """
        Popup Pygame : demande au joueur s'il veut ouvrir le conteneur.
        Le texte dépend automatiquement du type de conteneur.
        """

        popup_width, popup_height = 500, 240
        popup_rect = pygame.Rect(0, 0, popup_width+140, popup_height)
        popup_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        font = pygame.font.SysFont(None, 28)


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
        bouton_oui = pygame.Rect(popup_rect.x + 80, popup_rect.y + 150, 150, 50)
        bouton_non = pygame.Rect(popup_rect.x + 270, popup_rect.y + 150, 150, 50)


        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # on ne quitte pas pygame
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_oui.collidepoint(event.pos):
                        return True
                    if bouton_non.collidepoint(event.pos):
                        return False

            # Dessiner le popup
            overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))  # semi-transparent
            screen.blit(overlay, (0, 0))

            pygame.draw.rect(screen, (30, 30, 30), popup_rect)
            screen.blit(font.render(texte_str, True, (255, 255, 255)), (popup_rect.x + 20, popup_rect.y + 20))
            screen.blit(font.render("Cliquer sur oui ou non avec la souris",True,(255, 255, 255)), (popup_rect.x + 40, popup_rect.y + 40))
            pygame.draw.rect(screen, (0, 150, 0), bouton_oui)
            pygame.draw.rect(screen, (150, 0, 0), bouton_non)
            screen.blit(font.render("OUI", True, (255, 255, 255)), (bouton_oui.x + 55, bouton_oui.y + 12))
            screen.blit(font.render("NON", True, (255, 255, 255)), (bouton_non.x + 50, bouton_non.y + 12))

            pygame.display.flip()
            clock.tick(30)
