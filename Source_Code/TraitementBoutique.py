from Boutique import Boutique, ArticleShop
from Inventory import Inventaire

class TraitementBoutique : 

    def __init__(self, boutique : Boutique) : 
        self.boutique = boutique

    def traitement_boutique(self, inventaire : Inventaire) :
        pass # Ecris ici le traitement de la boutique avec l'inventaire du joueur