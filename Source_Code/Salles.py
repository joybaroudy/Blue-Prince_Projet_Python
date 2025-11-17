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

        self.name_to_id = {nom: ID for ID, nom in self.salles_names_dict.items()}

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
            "ID1" : 1,
            "ID2" : 0,
            "ID3" :3,
            "ID4" :3,
            "ID5" : 3,
            "ID6" : 3,
            "ID7" : 1,
            "ID8" : 1,
            "ID9" : 3,
            "ID10" : 2,
            "ID11" : 1,
            "ID12" : 3,
            "ID13" : 3,
            "ID14" : 2,
            "ID15" : 2,
            "ID16" : 1,
            "ID17" : 3,
            "ID18" : 1,
            "ID19" : 1,
            "ID20" : 2,
            "ID21" : 3,
            "ID22" : 2,
            "ID23" : 2,
            "ID24" : 2,
            "ID25" : 3,
            "ID26" : 2,
            "ID27" : 2,
            "ID28" : 1,
            "ID29" : 2,
            "ID30" : 1,
            "ID31" : 2,
            "ID32" : 1,
            "ID33" : 1,
            "ID34" : 2,
            "ID35" : 2,
            "ID36" : 2,
            "ID37" : 2,
            "ID38" : 3,
            "ID39" : 2,
            "ID40" : 1,
            "ID41" : 2,
            "ID42" : 2,
            "ID43" : 1,
            "ID44" : 1,
            "ID45" : 0,
            "ID46" : 3,
            "ID47" : 2,
            "ID48" : 3,
            "ID49" : 3,
            "ID50" : 2,
            "ID51" : 1,
            "ID52" : 1,
            "ID53" : 1,
            "ID54" : 3,
            "ID55" : 2,
            "ID56" : 1,
            "ID57" : 3,
            "ID58" : 3,
            "ID59" : 2,
            "ID60" : 2,
            "ID61" : 2,
            "ID62" : 2,
            "ID63" : 2,
            "ID64" : 2,
            "ID65" : 1,
            "ID66" : 1,
            "ID67" : 2,
            "ID68" : 1,
            "ID69" : 1,
            "ID70" : 2,
            "ID71" : 3,
            "ID72" : 2,
            "ID73" : 1,
            "ID74" : 1,
            "ID75" : 1,
            "ID76" : 2,
            "ID77" : 1,
            "ID78" : 2,
            "ID79" : 3,
            "ID80" : 2,
            "ID81" : 2,
            "ID82" : 2,
            "ID83" : 2,
            "ID84" : 1,
            "ID85" : 1
        }

        # Attribution du prix des salles 

        self.salles_price_dict = { #gem
            "ID1" : 0,
            "ID2" : 0,
            "ID3" : 0,
            "ID4" : 3,
            "ID5" : 0,
            "ID6" : 0,
            "ID7" : 0,
            "ID8" : 0,
            "ID9" : 0,
            "ID10" : 1,
            "ID11" : 3,
            "ID12" : 0,
            "ID13" : 0,
            "ID14" : 1,
            "ID15" : 2,
            "ID16" : 1,
            "ID17" : 0,
            "ID18" : 0,
            "ID19" : 5,
            "ID20" : 2,
            "ID21" : 0,
            "ID22" : 1,
            "ID23" : 3,
            "ID24" : 2,
            "ID25" : 1,
            "ID26" : 0,
            "ID27" : 0,
            "ID28" : 0,
            "ID29" : 1,
            "ID30" : 2,
            "ID31" : 0,
            "ID32" : 1,
            "ID33" : 0,
            "ID34" : 1,
            "ID35" : 0,
            "ID36" : 1,
            "ID37" : 0,
            "ID38" : 0,
            "ID39" : 0,
            "ID40" : 0,
            "ID41" : 0,
            "ID42" : 1,
            "ID43" : 0,
            "ID44" : 1,
            "ID45" : 0,
            "ID46" : 0,
            "ID47" : 0,
            "ID48" : 0,
            "ID49" : 1,
            "ID50" : 1,
            "ID51" : 0,
            "ID52" : 0,
            "ID53" : 2,
            "ID54" : 0,
            "ID55" : 0,
            "ID56" : 0,
            "ID57" : 0,
            "ID58" : 2,
            "ID59" : 1,
            "ID60" : 2,
            "ID61" : 0,
            "ID62" : 0,
            "ID63" : 1,
            "ID64" : 1,
            "ID65" : 3,
            "ID66" : 2,
            "ID67" : 1,
            "ID68" : 0,
            "ID69" : 0,
            "ID70" : 1,
            "ID71" : 1,
            "ID72" : 1,
            "ID73" : 2,
            "ID74" : 1,
            "ID75" : 1,
            "ID76" : 0,
            "ID77" : 0,
            "ID78" : 0,
            "ID79" : 0,
            "ID80" : 0,
            "ID81" : 0,
            "ID82" : 0,
            "ID83" : 0,
            "ID84" : 0,
            "ID85" : 0
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
            "ID9" : "Normal",
            "ID10" : "Normal",
            "ID11" : "Normal",
            "ID12" : "Normal",
            "ID13" : "Normal",
            "ID14" : "Edge",
            "ID15" : "Normal",
            "ID16" : "Normal", # Can be changed to "Pool" but for less complexity I would rather not
            "ID17" : "Normal", 
            "ID18" : "Normal",
            "ID19" : "Normal",
            "ID20" : "Normal",
            "ID21" : "Normal",
            "ID22" : "Normal",
            "ID23" : "Normal",
            "ID24" : "Normal",
            "ID25" : "Normal",
            "ID26" : "Normal",
            "ID27" : "Normal",
            "ID28" : "Normal",
            "ID29" : "Normal",
            "ID30" : "Normal",
            "ID31" : "Normal",
            "ID32" : "Normal",
            "ID33" : "Normal",
            "ID34" : "Normal",
            "ID35" : "Normal",
            "ID36" : "Normal",
            "ID37" : "Normal",
            "ID38" : "Normal",
            "ID39" : "Normal",
            "ID40" : "Normal",
            "ID41" : "Normal",
            "ID42" : "Edge",
            "ID43" : "Normal",
            "ID44" : "Normal",
            "ID45" : None,
            "ID46" : "Normal",
            "ID47" : "Normal",
            "ID48" : "Normal",
            "ID49" : "Normal",
            "ID50" : "Normal",
            "ID51" : "Normal",
            "ID52" : "Normal",
            "ID53" : "Normal",
            "ID54" : "Normal",
            "ID55" : "Normal",
            "ID56" : "Normal",
            "ID57" : "Not Edge",
            "ID58" : "Normal",
            "ID59" : "Normal",
            "ID60" : "Normal",
            "ID61" : "Not Edge",
            "ID62" : "Edge",
            "ID63" : "Edge",
            "ID64" : "Edge",
            "ID65" : "Edge",
            "ID66" : "Edge",
            "ID67" : "Edge",
            "ID68" : "Normal",
            "ID69" : "Edge",
            "ID70" : "Normal",
            "ID71" : "Normal",
            "ID72" : "Normal",
            "ID73" : "Normal",
            "ID74" : "Normal",
            "ID75" : "Edge",
            "ID76" : "Corner",
            "ID77" : "Corner",
            "ID78" : "Normal",
            "ID79" : "Normal",
            "ID80" : "Normal",
            "ID81" : "Normal",
            "ID82" : "Normal",
            "ID83" : "Normal",
            "ID84" : "Normal",
            "ID85" : "Normal"
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

        if cond is None : 
            return False
        elif cond == "Normal" :
            return True
        elif cond == "Edge" : 
            return case.position == "Edge"
        elif cond == "Corner" :
            return case.position == "Corner"
        else : 
            return case.position != "Edge" and case.position != "Corner"








        # if cond is None:
        #     return True
        # if cond == "Not Edge":
        #     return case.position != "Edge" and case.position != "Corner"
        # return cond == case.position





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

