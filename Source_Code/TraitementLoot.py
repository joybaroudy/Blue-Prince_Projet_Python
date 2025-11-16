from Inventory import Inventaire
from Objets import ObjetConsommable, ObjetPermanent, Nourriture
from Conteneurs import Coffre, Casier, Digspot
from RoomCell import RoomCell
from Manoir import Manoir




class TraitementLoot : 

    def get_loot_from_container(cell : RoomCell, container, inventaire : Inventaire):

        if container.ouvert == True :

            if container.genere == False :
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

    def take_loot_from_room(cell : RoomCell, inventaire : Inventaire):
        
        loot = cell.loot_on_ground
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
            
            elif isinstance(item, Coffre) :
                
                loot_restant_container = item.get_loot_from_container(item, inventaire)
                if loot_restant_container == [] :
                    loot_restant.remove(item)
            
            elif isinstance(item, Casier) :
                loot_restant_container = item.get_loot_from_container(item, inventaire)
                if loot_restant_container == [] :
                    loot_restant.remove(item)

            elif isinstance(item, Digspot) :
                loot_restant_container = item.get_loot_from_container(item, inventaire)
                if loot_restant_container == [] :
                    loot_restant.remove(item)


            

        cell.loot_on_ground = loot_restant