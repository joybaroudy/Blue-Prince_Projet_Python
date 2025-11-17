from Salles import Salle

class EffetsSalles : 

    def __init__(self, ID, salles : Salle) : 
         
         self.couleur = salles.salle_couleur_dict[str(ID)]
         self.effet = None

         if self.couleur == "Blue" : 
              pass
              
         elif self.couleur == "Purple" : 
              pass
         
         elif self.couleur == "Orange" : 
              pass
         
         elif self.couleur == "Green" : 
              pass
         
         elif self.couleur == "Yellow" : 
              self.effet = "Boutique"
         
         elif self.couleur == "Red" : 
              pass
              
        
