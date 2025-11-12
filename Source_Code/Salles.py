import random

class Salle :
    """
    Classe repsentant les salles dans le manoir
    """
    def __init__(self) :

        # Attribution du nom de la salle à son identidiant
        salles_names_dict = {

            "ID1" : "The Foundation",
            "ID2" : "Entrance Hall",
            "ID3" : "Spare Room",
            "ID4" : "Rotunda",
            "ID5" : "Parlor",
            "ID6" : "Billiard Room",
            "ID7" : "Gallery",
            "ID8" : "Room 8",
            "ID9" : "Closet",
            "ID10" : "Walk-in Closet",
            "ID11" : "Attic",
            "ID12" : "Storeroom",
            "ID13" : "Nook",
            "ID14" : "Garage",
            "ID15" : "Music Room",
            "ID16" : "Locker Room",
            "ID17" : "Den",
            "ID18" : "Wine Cellar",
            "ID19" : "Trophy Room",
            "ID20" : "Ballroom",
            "ID21" : "Pantry",
            "ID22" : "Rumpus Room",
            "ID23" : "Vault",
            "ID24" : "Office",
            "ID25" : "Drawing Room",
            "ID26" : "Study",
            "ID27" : "Library",
            "ID28" : "Chamber of Mirrors",
            "ID29" : "The Pool",
            "ID30" : "Drafting Studio",
            "ID31" : "Utility Closet",
            "ID32" : "Boiler Room",
            "ID33" : "Pump Room",
            "ID34" : "Security",
            "ID35" : "Workshop",
            "ID36" : "Laboratory",
            "ID37" : "Sauna",
            "ID38" : "Coat Check",
            "ID39" : "Mail Room",
            "ID40" : "Freezer",
            "ID41" : "Dining Room",
            "ID42" : "Observatory",
            "ID43" : "Conference Room",
            "ID44" : "Aquarium",
            "ID45" : "Antechamber",
            "ID46" : "Bedroom",
            "ID47" : "Boudoir",
            "ID48" : "Guest Bedroom",
            "ID49" : "Nursery",
            "ID50" : "Servant's Quarters",
            "ID51" : "Bunk Room",
            "ID52" : "Her Ladyship's Chamber",
            "ID53" : "Master Bedroom",
            "ID54" : "Hallway",
            "ID55" : "West Wing Hall",
            "ID56" : "East Wing Hall",
            "ID57" : "Corridor",
            "ID58" : "Passageway",
            "ID59" : "Secret Passage",
            "ID60" : "Foyer",
            "ID61" : "Great Hall",
            "ID62" : "Terrace",
            "ID63" : "Patio",
            "ID64" : "Courtyard",
            "ID65" : "Cloister",
            "ID66" : "Veranda",
            "ID67" : "Greenhouse",
            "ID68" : "Morning Room",
            "ID69" : "Secret Garden",
            "ID70" : "Commissary",
            "ID71" : "Kitchen",
            "ID72" : "Locksmith",
            "ID73" : "Showroom",
            "ID74" : "Laundry Room",
            "ID75" : "Bookshop",
            "ID76" : "The Armory",
            "ID77" : "Mount Holly Gift Shop",
            "ID78" : "Lavatory",
            "ID79" : "Chapel",
            "ID80" : "Maid's Chamber",
            "ID81" : "Archives",
            "ID82" : "Gymnasium",
            "ID83" : "Darkroom",
            "ID84" : "Weight Room",
            "ID85" : "Furnace"
            }


        salles_rarete_dict = {
            "ID1" : 3,
            "ID2" : None,
            "ID3" : 0,
            "ID4" : 3,
            "ID5" : 0,
            "ID6" : 0,
            "ID7" : 3,
            "ID8" : 3,
            "ID9" : 0,
            "ID10" : 1,
            "ID11" : 3,
            "ID12" : 0,
            "ID13" : 0,
            "ID14" : 2,
            "ID15" : 2,
            "ID16" : 3,
            "ID17" : 0,
            "ID18" : 2,
            "ID19" : 3,
            "ID20" : 2,
            "ID21" : 0,
            "ID22" : 1,
            "ID23" : 3,
            "ID24" : 1,
            "ID25" : 0,
            "ID26" : 2,
            "ID27" : 2,
            "ID28" : 3,
            "ID29" : 1,
            "ID30" : 3,
            "ID31" : 1,
            "ID32" : 2,
            "ID33" : 2,
            "ID34" : 1,
            "ID35" : 2,
            "ID36" : 1,
            "ID37" : 2,
            "ID38" : 1,
            "ID39" : 2,
            "ID40" : 3,
            "ID41" : 1,
            "ID42" : 1,
            "ID43" : 2,
            "ID44" : 2,
            "ID45" : None,
            "ID46" : 0,
            "ID47" : 1,
            "ID48" : 0,
            "ID49" : 0,
            "ID50" : 2,
            "ID51" : 2,
            "ID52" : 3,
            "ID53" : 3,
            "ID54" : 0,
            "ID55" : 1,
            "ID56" : 2,
            "ID57" : 0,
            "ID58" : 0,
            "ID59" : 2,
            "ID60" : 2,
            "ID61" : 2,
            "ID62" : 1,
            "ID63" : 1,
            "ID64" : 1,
            "ID65" : 2,
            "ID66" : 2,
            "ID67" : 1,
            "ID68" : 3,
            "ID69" : 3,
            "ID70" : 1,
            "ID71" : 0,
            "ID72" : 2,
            "ID73" : 3,
            "ID74" : 3,
            "ID75" : 3,
            "ID76" : 1,
            "ID77" : 3,
            "ID78" : 1,
            "ID79" : 0,
            "ID80" : 2,
            "ID81" : 2,
            "ID82" : 1,
            "ID83" : 1,
            "ID84" : 3,
            "ID85" : 3
        }

        # Initialisation du nombre initial des salles
        salles_count_dict = {
            "ID1" : 2,
            "ID2" : None,
            "ID3" : 10,
            "ID4" : 2,
            "ID5" : 10,
            "ID6" : 10,
            "ID7" : 2,
            "ID8" : 2,
            "ID9" : 10,
            "ID10" : 7,
            "ID11" : 2,
            "ID12" : 10,
            "ID13" : 10,
            "ID14" : 4,
            "ID15" : 4,
            "ID16" : 2,
            "ID17" : 10,
            "ID18" : 4,
            "ID19" : 2,
            "ID20" : 4,
            "ID21" : 10,
            "ID22" : 7,
            "ID23" : 2,
            "ID24" : 7,
            "ID25" : 10,
            "ID26" : 4,
            "ID27" : 4,
            "ID28" : 2,
            "ID29" : 7,
            "ID30" : 2,
            "ID31" : 7,
            "ID32" : 4,
            "ID33" : 4,
            "ID34" : 7,
            "ID35" : 4,
            "ID36" : 7,
            "ID37" : 4,
            "ID38" : 7,
            "ID39" : 4,
            "ID40" : 2,
            "ID41" : 7,
            "ID42" : 7,
            "ID43" : 4,
            "ID44" : 4,
            "ID45" : None,
            "ID46" : 10,
            "ID47" : 7,
            "ID48" : 10,
            "ID49" : 10,
            "ID50" : 4,
            "ID51" : 4,
            "ID52" : 2,
            "ID53" : 2,
            "ID54" : 10,
            "ID55" : 7,
            "ID56" : 4,
            "ID57" : 10,
            "ID58" : 10,
            "ID59" : 4,
            "ID60" : 4,
            "ID61" : 4,
            "ID62" : 7,
            "ID63" : 7,
            "ID64" : 7,
            "ID65" : 4,
            "ID66" : 4,
            "ID67" : 7,
            "ID68" : 2,
            "ID69" : 2,
            "ID70" : 7,
            "ID71" : 10,
            "ID72" : 4,
            "ID73" : 2,
            "ID74" : 2,
            "ID75" : 2,
            "ID76" : 7,
            "ID77" : 2,
            "ID78" : 7,
            "ID79" : 10,
            "ID80" : 4,
            "ID81" : 4,
            "ID82" : 7,
            "ID83" : 7,
            "ID84" : 2,
            "ID85" : 2
        }


        # Attribution du prix des salles 

        salles_price_dict = { #gem
            "ID 1" : 0,
            "ID 2" : 2
        }

        salles_conditions_dict = {
            "ID1" : "Not Edge",
            "ID2" : None,
            "ID3" : "Normal",
            "ID4" : "Normal",
            "ID5" : "Normal",
            "ID6" : "Normal",
            "ID7" : "Normal", # gallery : could be linked to room 46
            "ID8" : "Normal", #room 8 : could be linked to gallery
            "ID9" : "Closet",
            "ID10" : "Walk-in Closet",
            "ID11" : "Attic",
            "ID12" : "Storeroom",
            "ID13" : "Nook",
            "ID14" : "Garage",
            "ID15" : "Music Room",
            "ID16" : "Locker Room",
            "ID17" : "Den",
            "ID18" : "Wine Cellar",
            "ID19" : "Trophy Room",
            "ID20" : "Ballroom",
            "ID21" : "Pantry",
            "ID22" : "Rumpus Room",
            "ID23" : "Vault",
            "ID24" : "Office",
            "ID25" : "Drawing Room",
            "ID26" : "Study",
            "ID27" : "Library",
            "ID28" : "Chamber of Mirrors",
            "ID29" : "The Pool",
            "ID30" : "Drafting Studio",
            "ID31" : "Utility Closet",
            "ID32" : "Boiler Room",
            "ID33" : "Pump Room",
            "ID34" : "Security",
            "ID35" : "Workshop",
            "ID36" : "Laboratory",
            "ID37" : "Sauna",
            "ID38" : "Coat Check",
            "ID39" : "Mail Room",
            "ID40" : "Freezer",
            "ID41" : "Dining Room",
            "ID42" : "Observatory",
            "ID43" : "Conference Room",
            "ID44" : "Aquarium",
            "ID45" : "Antechamber",
            "ID46" : "Bedroom",
            "ID47" : "Boudoir",
            "ID48" : "Guest Bedroom",
            "ID49" : "Nursery",
            "ID50" : "Servant's Quarters",
            "ID51" : "Bunk Room",
            "ID52" : "Her Ladyship's Chamber",
            "ID53" : "Master Bedroom",
            "ID54" : "Hallway",
            "ID55" : "West Wing Hall",
            "ID56" : "East Wing Hall",
            "ID57" : "Corridor",
            "ID58" : "Passageway",
            "ID59" : "Secret Passage",
            "ID60" : "Foyer",
            "ID61" : "Great Hall",
            "ID62" : "Terrace",
            "ID63" : "Patio",
            "ID64" : "Courtyard",
            "ID65" : "Cloister",
            "ID66" : "Veranda",
            "ID67" : "Greenhouse",
            "ID68" : "Morning Room",
            "ID69" : "Secret Garden",
            "ID70" : "Commissary",
            "ID71" : "Kitchen",
            "ID72" : "Locksmith",
            "ID73" : "Showroom",
            "ID74" : "Laundry Room",
            "ID75" : "Bookshop",
            "ID76" : "The Armory",
            "ID77" : "Mount Holly Gift Shop",
            "ID78" : "Lavatory",
            "ID79" : "Chapel",
            "ID80" : "Maid's Chamber",
            "ID81" : "Archives",
            "ID82" : "Gymnasium",
            "ID83" : "Darkroom",
            "ID84" : "Weight Room",
            "ID85" : "Furnace"
        }

        salle_porte_emplacement_dict = {
            "ID 1" : [True, True, False , True],
            "ID 2" : [False, True, True, True],
            "ID 3" : [True, False, True, False],
            "ID 4" : [True, True, False, False],
            "ID 5" : [True, True, False, False],
            "ID 6" : [True, True, False, False],
            "ID 7" : [True, False, True, False],
            "ID 8" : [True, True, False, False],
            "ID 9" : [True, False, False, False],
            "ID 10" : [True, False, False, False],
            "ID 11" : [True, False, False, False],
            "ID 12" : [True, False, False, False],
            "ID 13" : [True, True, False, False],
            "ID 14" : [True, False, False, False],
            "ID 15" : [True, True, False, False],
            "ID 16" : [True, False, True, False],
            "ID 17" : [True, True, False, True],
            "ID 18" : [True, False, False, False],
            "ID 19" : [True, True, False, False],
            "ID 20" : [True, False, True, False],
            "ID 21" : [True, True, False, False],
            "ID 22" : [True, False, True, False],
            "ID 23" : [True, False, False, False],
            "ID 24" : [True, True, False, False],

        }

        salle_couleur_dict = {

            # Blue
            "ID1" : "Blue",
            "ID2" : "Blue",
            "ID3" : "Blue",
            "ID4" : "Blue",
            "ID5" : "Blue",
            "ID6" : "Blue",
            "ID7" : "Blue",
            "ID8" : "Blue",
            "ID9" : "Blue",
            "ID10" : "Blue",
            "ID11" : "Blue",
            "ID12" : "Blue",
            "ID13" : "Blue",
            "ID14" : "Blue",
            "ID15" : "Blue",
            "ID16" : "Blue",
            "ID17" : "Blue",
            "ID18" : "Blue",
            "ID19" : "Blue",
            "ID20" : "Blue",
            "ID21" : "Blue",
            "ID22" : "Blue",
            "ID23" : "Blue",
            "ID24" : "Blue",
            "ID25" : "Blue",
            "ID26" : "Blue",
            "ID27" : "Blue",
            "ID28" : "Blue",
            "ID29" : "Blue",
            "ID30" : "Blue",
            "ID31" : "Blue",
            "ID32" : "Blue",
            "ID33" : "Blue",
            "ID34" : "Blue",
            "ID35" : "Blue",
            "ID36" : "Blue",
            "ID37" : "Blue",
            "ID38" : "Blue",
            "ID39" : "Blue",
            "ID40" : "Blue",
            "ID41" : "Blue",
            "ID42" : "Blue",
            "ID43" : "Blue",
            "ID44" : "Blue",
            "ID45" : "Blue",

            # Purple
            "ID46" : "Purple",
            "ID47" : "Purple",
            "ID48" : "Purple",
            "ID49" : "Purple",
            "ID50" : "Purple",
            "ID51" : "Purple",
            "ID52" : "Purple",
            "ID53" : "Purple",

            # Orange
            "ID54" : "Orange",
            "ID55" : "Orange",
            "ID56" : "Orange",
            "ID57" : "Orange",
            "ID58" : "Orange",
            "ID59" : "Orange",
            "ID60" : "Orange",
            "ID61" : "Orange",

            # Green
            "ID62" : "Green",
            "ID63" : "Green",
            "ID64" : "Green",
            "ID65" : "Green",
            "ID66" : "Green",
            "ID67" : "Green",
            "ID68" : "Green",
            "ID69" : "Green",

            # Yellow
            "ID70" : "Yellow",
            "ID71" : "Yellow",
            "ID72" : "Yellow",
            "ID73" : "Yellow",
            "ID74" : "Yellow",
            "ID75" : "Yellow",
            "ID76" : "Yellow",
            "ID77" : "Yellow",

            # Red
            "ID78" : "Red",
            "ID79" : "Red",
            "ID80" : "Red",
            "ID81" : "Red",
            "ID82" : "Red",
            "ID83" : "Red",
            "ID84" : "Red",
            "ID85" : "Red"
        }

        self.IDs = list(self.salles_names_dict.keys())


class Case : 
    def _init_(self,coordinates) : 
        self.coordinates = coordinates
        if coordinates == [1,1] or coordinates == [1,5] or coordinates == [9,1] or coordinates == [9,5] : 
            self.position = "Corner"
        elif coordinates[0] == 1 or coordinates[0] == 9 or coordinates[1] == 1 or coordinates[1] == 5 : 
            self.position = "Edge"
        else : 
            self.position = "Normal"


class Porte(Salle) : 
    """
    Classe pour les portes et leur methodes
    """

    def __init__(self, coordonnees) : 
        weight_cout_0 = 1 * (1 - (coordonnees[1]/9)) # Probabilité que le cout soit 0
        weight_cout_1 = 1 * ((coordonnees[1]/9)) # Probabilité que le coup soit 1
        
        cout = random.choices([0, 1], weights=[weight_cout_0, weight_cout_1], k=1)[0]

        self.cout = cout
        self.ouvert = False

        proba_DT = 0.3*(coordonnees[1]/9)

        if self.cout == 1 :
            self.double_tour = random.choices([False, True], weights=[1-proba_DT, proba_DT ], k=1)[0]
        else : 
            self.double_tour = False 
    
    def OuvrirPorte(self, inventaire) : 
        if inventaire.objets_permanents["Lockpick Kit"] == True : 
            self.ouvert = True
        elif inventaire.objets_consommables["Clés"] < self.cout and self.ouvert == True : 
            inventaire.objets_consommables["Clés"].changer_solde(self.cout)
            self.ouvert = True


class Traitement_Salle(Case, Salle) : 

    def __init__(self,salles_liste) :
        self.salles_liste = salles_liste

    def Condition_Met(self, ID, case) : # MEthode OBSOLETE A REVOIR !!!!!!!!!!!! NE PRends pas en comptes BCP DE facteurs
        condition_met = False
        if self.salles_conditions_dict[ID] == case.position : 
            condition_met = True
        return condition_met

    def Pooling_salle(self, coordonnees, porte_index) :
        """
        Mehtode qui cree une base de salle dont on pourra tirer 3 salle au sort
        """

        if porte_index == 0 : 
            porte_index_match = 2
        elif porte_index == 1 :
            porte_index_match = 3
        elif porte_index == 2 :
            porte_index_match = 0
        else : 
            porte_index_match = 1

        pool = []
        probabilites = []
        facteur = 1 # Variable à ajuster durant les test

        for ID in self.IDs : 
            if self.salles_count_dict[ID] > 0 : 
                if self.salle.emplacement_porte[ID][porte_index_match] == True :
                    if self.salle.Condition_Met(ID,coordonnees) :
                        
                        poids =  1/(3**self.salles_rarete_dict[ID]) * (1 + facteur*(coordonnees[1]/9)*self.salles_price_dict[ID])

                    pool.append(ID)
                    probabilites.append(poids)
        salle_pool = [pool,probabilites]   
        return salle_pool

    def Tirage_salle(self, coordonnees) : 
        """ 
        Methode qui tire au sort 3 salles à montrer apres ouvire une porte,  
        dependement des probabilités de tirer une salle specifique et 
        et du poids de tirer cette salle à une rangée donnée dans le manoir
        
        salle_pool est une matrice de dimension 2*Nb de salles dont la première 
        colonne est le type de la salle et la deuxieme est la probabilité de la tirer 
        """

        pool, poids = self.Pooling_salle(coordonnees)
        total_poids = sum(poids)
        poids_norm = [p / total_poids for p in poids] # Normalisation des probabilités de tirage

        tirage = []

        for i in range(0,3):
            salle_tiree = random.choices(pool, weights=poids_norm, k=1)[0]
            tirage.append(salle_tiree)

            index = pool.index(salle_tiree)
            pool.pop(index)
            poids.pop(index)

            total_poids = sum(poids_norm)
            poids_norm = [p / total_poids for p in poids_norm] # Renormalisation des probabilités de tirage
        
        if coordonnees[1] == 1 and not (self.salles_price_dict(tirage[0] == 0) or self.salles_price_dict(tirage[1] == 0) or self.salles_price_dict(tirage[2] == 0)) :

            pool_free = []
            
            for ID in pool : 
                if self.salles_price_dict[ID] == 0 : 
                    pool_free.append(ID)

            tirage[0] = random.choice(pool_free)

        return tirage

    def Generation_salle (coordonnes, salle_ID) : 
        """"
        Methode qui a pour but de creer la salle et de generer les objets à l'interieur
        """
        


