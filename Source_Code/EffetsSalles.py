from Salles import Salle
from Inventory import Inventaire

class EffetsSalles : 

    def __init__(self, ID, salles : Salle) : 
         
         self.couleur = salles.salle_couleur_dict[str(ID)]
         self.name = salles.salles_names_dict[str(ID)]
         self.dining = False
    
    def apply_entry_effects(self, inventaire : Inventaire) :
         
        if self.couleur == "Purple" :
            inventaire.objets_consommables["Pas"].changer_solde(int(+2))
         
        elif self.name == "Weight Room" : 
            pas_total = inventaire.objets_consommables["Pas"].quantite
            inventaire.objets_consommables["Pas"].changer_solde(int(-pas_total /2))
        
        elif self.name == "Gymnasium" : 
            inventaire.objets_consommables["Pas"].changer_solde(int(-2))
        
        elif self.name == "Chapel" : 
            if inventaire.objets_consommables["Pièces"].quantite > 0:
                inventaire.objets_consommables["Pièces"].changer_solde(int(-1))

        elif self.name == "Dining Room" : 
            self.dining = True
            print("Vous êtes dans la Dining Room. Vous gagnerez un repas une fois arrivé à la 7ème rangée.")

    def apply_weights_effects(self, weights) :

        if self.name == "Maid's Chamber" : 
            for key in weights :
                weights[key] = 0

    def apply_over_time_effects(self, inventaire : Inventaire, coordonnes) :
        r, c = coordonnes

        if self.dining == True :
            first_time_dining = True
            if r == 7 and first_time_dining : 
                inventaire.objets_consommables["Pas"].changer_solde(int(+25))
                print("Vous avez gagné 25 pas en mangeant dans la Dining Room.")
                first_time_dining = False







              
        
