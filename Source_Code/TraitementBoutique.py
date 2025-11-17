import pygame
from Boutique import Boutique
from Inventory import Inventaire


class TraitementBoutique:

    def __init__(self, boutique: Boutique):
        self.boutique = boutique

    def traitement_boutique(self, inventaire: Inventaire):
        """
        Affiche une petite fenêtre Pygame de boutique :
        - flèches HAUT / BAS pour changer d'article
        - ENTREE pour acheter
        - ESC ou sélectionner "Quitter" pour sortir
        """

        # Récupérer la liste des articles [(index, nom, prix), ...]
        articles = self.boutique.lister_articles()
        if not articles:
            print("Cette salle ne contient pas de boutique.")
            return

        # --- Initialisation Pygame de la fenêtre de shop ---
        WIDTH, HEIGHT = 600, 400
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(f"Boutique - {self.boutique.nom_salle}")

        font = pygame.font.SysFont(None, 28)
        clock = pygame.time.Clock()

        selection = 0             # index de l’article sélectionné
        running = True
        message = ""              # message d’info (achat réussi / refusé)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_UP:
                        selection = (selection - 1) % len(articles)

                    elif event.key == pygame.K_DOWN:
                        selection = (selection + 1) % len(articles)

                    elif event.key == pygame.K_RETURN:
                        idx, nom, prix = articles[selection]

                        # Tentative d’achat
                        succes = self.boutique.acheter_index(inventaire, idx)
                        if succes:
                            message = f"Achat de '{nom}' réussi !"
                            # Recharger la liste (l’article peut être retiré ou non
                            # selon ta logique future)
                            articles = self.boutique.lister_articles()
                            if not articles:
                                running = False
                                continue
                            selection = min(selection, len(articles) - 1)
                        else:
                            message = f"Pas assez de pièces pour '{nom}'."

            # ---- AFFICHAGE ----
            screen.fill((30, 30, 30))

            titre = font.render(
                f"Boutique - {self.boutique.nom_salle}", True, (255, 255, 0)
            )
            screen.blit(titre, (WIDTH // 2 - titre.get_width() // 2, 20))

            # Affichage du nombre de pièces du joueur
            nb_pieces = inventaire.objets_consommables["Pièces"].quantite
            txt_pieces = font.render(
                f"Pièces : {nb_pieces}", True, (255, 255, 255)
            )
            screen.blit(txt_pieces, (20, 60))

            # Liste des articles
            start_y = 110
            for i, (idx, nom, prix) in enumerate(articles):
                # Préfixe > pour l’article sélectionné
                prefix = "> " if i == selection else "  "
                txt = font.render(f"{prefix}{nom}  -  {prix} pièces", True, (200, 200, 200))
                screen.blit(txt, (60, start_y + i * 30))

            # Message d’info
            if message:
                txt_msg = font.render(message, True, (0, 200, 0))
                screen.blit(
                    txt_msg,
                    (WIDTH // 2 - txt_msg.get_width() // 2, HEIGHT - 60),
                )

            pygame.display.flip()
            clock.tick(30)

      
