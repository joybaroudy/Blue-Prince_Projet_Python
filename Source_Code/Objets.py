# from Inventory import Inventaire

# class Objet:
#     """Classe de base pour tout objet du jeu."""
#     def __init__(self, nom=None):
#         self.nom = nom

# class ObjetConsommable(Objet):
#     """Objets consommables (Pas, Pièces, Gemmes, Clés, Dés)."""
#     def __init__(self, nom, quantite=0):
#         super().__init__(nom)
#         self.quantite = quantite

#     def changer_solde(self, changement):
#         """Augmente ou diminue la quantité."""
#         self.quantite = self.quantite + changement
        
# class ObjetPermanent(Objet):
#     """Objet permanent (Shovel, Hammer, etc.)."""
#     def __init__(self, nom, obtenu=False):
#         super().__init__(nom)
#         self.obtenu = obtenu

#     def debloquer(self):
#         self.obtenu = True

# class Nourriture(Objet):
#     """Nourriture - donne des pas."""
#     def __init__(self, nom, gain):
#         super().__init__(nom)
#         self.gain = gain

#     def consommer(self, inventaire : Inventaire ):
#         inventaire.objets_consommables["Pas"].changer_solde(self.gain)

