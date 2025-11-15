import random
from Inventory import Inventaire, ObjetPermanent, ObjetConsommable


class Case:
    def __init__(self, coordinates):
        """
        coordinates : [row, col] (1-indexed dans ton code d'origine).
        position : "Corner" / "Edge" / "Normal"
        """
        self.coordinates = coordinates
        r, c = coordinates
        # coins : (1,1), (1,5), (9,1), (9,5) selon ton ancien code (5x9 grid)
        if coordinates in ([1,1], [1,5], [9,1], [9,5]):
            self.position = "Corner"
        elif r == 1 or r == 9 or c == 1 or c == 5:
            self.position = "Edge"
        else:   
            self.position = "Normal"

class Salle:
    """
    Contient les dictionnaires de données des salles (names, rarete, count, price, conditions...).
    Chaque instance de Salle représente *le catalogue / données*.
    Pour une salle placée dans la grille on utilisera une autre structure (RoomInstance si besoin).
    """
    def __init__(self):

        # Attribution du nom de la salle à son identidiant
        self.salles_names_dict = {

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

        self.salles_rarete_dict = {
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
        self.salles_count_dict = {
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

        self.salles_price_dict = { #gem
            "ID 1" : 0,
            "ID 2" : 0,
            "ID 3" : 0,
            "ID 4" : 3,
            "ID 5" : 0,
            "ID 6" : 0,
            "ID 7" : 0,
            "ID 8" : 0,
            "ID 9" : 0,
            "ID 10" : 1,
            "ID 11" : 3,
            "ID 12" : 0,
            "ID 13" : 0,
            "ID 14" : 1,
            "ID 15" : 2,
            "ID 16" : 1,
            "ID 17" : 0,
            "ID 18" : 0,
            "ID 19" : 5,
            "ID 20" : 2,
            "ID 21" : 0,
            "ID 22" : 1,
            "ID 23" : 3,
            "ID 24" : 2,
            "ID 25" : 1,
            "ID 26" : 0,
            "ID 27" : 0,
            "ID 28" : 0,
            "ID 29" : 1,
            "ID 30" : 2,
            "ID 31" : 0,
            "ID 32" : 1,
            "ID 33" : 0,
            "ID 34" : 1,
            "ID 35" : 0,
            "ID 36" : 1,
            "ID 37" : 0,
            "ID 38" : 0,
            "ID 39" : 0,
            "ID 40" : 0,
            "ID 41" : 0,
            "ID 42" : 1,
            "ID 43" : 0,
            "ID 44" : 1,
            "ID 45" : 0,
            "ID 46" : 0,
            "ID 47" : 0,
            "ID 48" : 0,
            "ID 49" : 1,
            "ID 50" : 1,
            "ID 51" : 0,
            "ID 52" : 0,
            "ID 53" : 2,
            "ID 54" : 0,
            "ID 55" : 0,
            "ID 56" : 0,
            "ID 57" : 0,
            "ID 58" : 2,
            "ID 59" : 1,
            "ID 60" : 2,
            "ID 61" : 0,
            "ID 62" : 0,
            "ID 63" : 1,
            "ID 64" : 1,
            "ID 65" : 3,
            "ID 66" : 2,
            "ID 67" : 1,
            "ID 68" : 0,
            "ID 69" : 0,
            "ID 70" : 1,
            "ID 71" : 1,
            "ID 72" : 1,
            "ID 73" : 2,
            "ID 74" : 1,
            "ID 75" : 1,
            "ID 76" : 0,
            "ID 77" : 0,
            "ID 78" : 0,
            "ID 79" : 0,
            "ID 80" : 0,
            "ID 81" : 0,
            "ID 82" : 0,
            "ID 83" : 0,
            "ID 84" : 0,
            "ID 85" : 0
        }

        self.salles_conditions_dict = {
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

        self.salle_porte_emplacement_dict = {
            "ID1" : [True, True, False , True],
            "ID2" : [False, True, True, True],
            "ID3" : [True, False, True, False],
            "ID4" : [True, True, False, False],
            "ID5" : [True, True, False, False],
            "ID6" : [True, True, False, False],
            "ID7" : [True, False, True, False],
            "ID8" : [True, True, False, False],
            "ID9" : [True, False, False, False],
            "ID10" : [True, False, False, False],
            "ID11" : [True, False, False, False],
            "ID12" : [True, False, False, False],
            "ID13" : [True, True, False, False],
            "ID14" : [True, False, False, False],
            "ID15" : [True, True, False, False],
            "ID16" : [True, False, True, False],
            "ID17" : [True, True, False, True],
            "ID18" : [True, False, False, False],
            "ID19" : [True, True, False, False],
            "ID20" : [True, False, True, False],
            "ID21" : [True, True, False, False],
            "ID22" : [True, False, True, False],
            "ID23" : [True, False, False, False],
            "ID24" : [True, True, False, False],
            "ID25" : [True, True, False, True],
            "ID26" : [True, False, False, False],
            "ID27" : [True, True, False, False],
            "ID28" : [True, False, False, False],
            "ID29" : [True, True, False, True],
            "ID30" : [True, False, True, False],
            "ID31" : [True, False, False, False],
            "ID32" : [True, True, False, True],
            "ID33" : [True, True, False, False],
            "ID34" : [True, True, False, True],
            "ID35" : [True, False, True, False],
            "ID36" : [True, True, False, False],
            "ID37" : [True, False, False, False],
            "ID38" : [True, False, False, False],
            "ID39" : [True, False, False, False],
            "ID40" : [True, False, False, False],
            "ID41" : [True, True, False, True],
            "ID42" : [True, True, False, False],
            "ID43" : [True, True, False, True],
            "ID44" : [True, True, False, True],
            "ID45" : [True, True, True, True],
            "ID46" : [True, True, False, False],
            "ID47" : [True, True, False, False],
            "ID48" : [True, False, False, False],
            "ID49" : [True, False, False, False],
            "ID50" : [True, False, False, False],
            "ID51" : [True, False, False, False],
            "ID52" : [True, False, False, False],
            "ID53" : [True, False, False, False],
            "ID54" : [True, True, False, True],
            "ID55" : [True, True, False, True],
            "ID56" : [True, True, False, True],
            "ID57" : [True, False, True, False],
            "ID58" : [True, True, True, True],
            "ID59" : [True, False, False, False],
            "ID60" : [True, False, True, False],
            "ID61" : [True, False, False, False],
            "ID62" : [True, False, False, False],
            "ID63" : [True, True, False, False],
            "ID64" : [True, True, False, True],
            "ID65" : [True, True, True, True],
            "ID66" : [True, False, True, False],
            "ID67" : [True, False, False, False],
            "ID68" : [True, True, False, False],
            "ID69" : [True, True, False, True],
            "ID70" : [True, True, False, False],
            "ID71" : [True, True, False, False],
            "ID72" : [True, False, False, False],
            "ID73" : [True, False, True, False],
            "ID74" : [True, False, False, False],
            "ID75" : [True, True, False, False],
            "ID76" : [True, True, False, False],
            "ID77" : [True, True, False, True],
            "ID78" : [True, False, False, False],
            "ID79" : [True, True, False, True],
            "ID80" : [True, True, False, False],
            "ID81" : [True, True, True, True],
            "ID82" : [True, True, False, True],
            "ID83" : [True, True, False, True],
            "ID84" : [True, True, True, True],
            "ID85" : [True, False, False, False]

        }

        self.salle_couleur_dict = {

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

        # Liste d'IDs disponibles 
        self.IDs = [k for k in self.salles_names_dict.keys()]

    def peut_etre_placee(self, ID, case: Case):
        cond = self.salles_conditions_dict.get(ID)
        if cond is None:
            return True
        if cond == "Not Edge":
            return case.position != "Edge" and case.position != "Corner"
        return cond == case.position





class Porte:
    """
    Porte : statut verrouillage 0/1/2 (0=open, 1=locked, 2=double lock)
    Ne doit PAS hériter de Salle.
    """
    def __init__(self, coordonnees):
        # coordonnees : [row, col] 
        r, c = coordonnees
        # probabilité de cout 0 diminue quand on monte dans le manoir (col plus élevé)
        weight_cout_0 = 1 * (1 - (c / 9))
        weight_cout_1 = 1 * (c / 9)
        cout = random.choices([0, 1], weights=[weight_cout_0, weight_cout_1], k=1)[0]
        self.cout = cout  # 0 ou 1 ; si 1 il faudra une clé (ou kit crochetage si level 1)
        self.ouvert = False

        proba_DT = 0.5 * (c / 9)  # proba d'avoir double-tour si cout==1

        if self.cout == 1:
            self.double_tour = random.choices([False, True], weights=[1 - proba_DT, proba_DT], k=1)[0]
            # niveau : 1 (locked) ou 2 (double tour), on encode via self.level
            if self.double_tour :
                self.level = 2 
            else :
                self.level = 1
        else:
            self.double_tour = False
            self.level = 0

    def ouvrir_porte(self, inventaire: Inventaire):
        """
        Tentative d'ouverture:
        - si kit de crochetage obtenu et level == 1 -> ouvre
        - sinon si clés suffisantes -> dépense
        - sinon si level == 0 -> ouvre gratuitement
        """
        if self.ouvert:
            return True

        if self.level == 0:
            self.ouvert = True
            return True

        # level 1 ou 2
        kit = inventaire.objets_permanents["Lockpick Kit"]
        if self.level == 1 and isinstance(kit, ObjetPermanent) and kit.obtenu:
            self.ouvert = True
            return True

        # sinon tenter avec clés
        if inventaire.objets_consommables["Clés"].quantite >= self.cout:
            inventaire.objets_consommables["Clés"].changer_solde(-self.cout)
            self.ouvert = True
            return True

        return False

