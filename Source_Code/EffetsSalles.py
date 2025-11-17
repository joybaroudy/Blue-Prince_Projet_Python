from Salles import Salle
from Inventory import Inventaire

class EffetsSalles : 

    def __init__(self, ID, salles : Salle) : 
         
         self.couleur = salles.salle_couleur_dict[str(ID)]
         self.name = salles.salles_names_dict[str(ID)]
    
    def apply_entry_effects(self, inventaire : Inventaire) :
         
        if self.couleur == "Purple" :
            inventaire.objets_consommables["Pas"].changer_solde(int(+2))
         
        elif self.name == "Weight Room" : 
            pas_total = inventaire.objets_consommables["Pas"].quantite
            inventaire.objets_consommables["Pas"].changer_solde(int(-pas_total /2))
        
        elif self.name == "Gymnasium" : 
            inventaire.objets_consommables["Pas"].changer_solde(int(-2))








              
        
