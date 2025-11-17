from dataclasses import dataclass
from typing import Callable, List, Tuple
import random



#  BOUTIQUES : achat d'objets avec les pièces d'or

class ArticleShop:
    def __init__(self, nom_affiche: str, prix: int, action):
        """
        nom_affiche : str  → texte affiché dans le shop
        prix        : int  → coût en pièces
        action      : func → fonction(inventaire) appliquant l'effet de l'achat
        """
        self.nom_affiche = nom_affiche
        self.prix = prix
        self.action = action

    def acheter(self, inventaire) -> bool:
        """Tente d'acheter l'article avec l'inventaire donné."""
        if inventaire.depenser_pieces(self.prix):
            self.action(inventaire)
            return True
        return False


# Fonctions d'effet d'achat

def _ajouter_consommable(inv, nom: str, quantite: int = 1):
    inv.objets_consommables[nom].changer_solde(quantite)

def _manger(inv, nom_nourriture: str):
    inv.nourritures[nom_nourriture].consommer(inv)

def _debloquer_permanent(inv, nom: str):
    inv.objets_permanents[nom].debloquer()


# Tables des objets possibles et des prix (version simple)

OBJETS_CONSOMMABLES_SHOP = ["Gemmes", "Clés", "Dés", "Pas"]

NOURRITURES_NOMS = ["Pomme", "Banane", "Gâteau", "Sandwich", "Repas"]

PRIX_CONSOMMABLES = {
    "Gemmes": 5,
    "Clés": 4,
    "Dés": 4,
}

PRIX_NOURRITURE = {
    "Pomme": 3,
    "Banane": 4,
    "Gâteau": 7,
    "Sandwich": 9,
}

LOCKSMITH_NAME = "Locksmith"
KITCHEN_NAME = "Kitchen"

AUTRES_SHOPS_JAUNES = {
    "Commissary",
    "Showroom",
    "Laundry Room",
    "Bookshop",
    "The Armory",
    "Mount Holly Gift Shop",
}


class Boutique:
    """
    Une boutique liée à une Yellow room.
    Kitchen: nourriture uniquement
    Locksmith: clés, hammer, lockpick
    Autres shops jaunes: 3 à 4 items aléatoires
    """
    def __init__(self, nom_salle: str):
        self.nom_salle = nom_salle
        self.articles: List[ArticleShop] = self._generer_articles(nom_salle)

    def _generer_articles(self, nom_salle: str) -> List[ArticleShop]:
        articles: List[ArticleShop] = []

        # 1) Kitchen -> seulement nourriture (3 items au hasard)
        if nom_salle == KITCHEN_NAME:
            choix = random.sample(NOURRITURES_NOMS, k=3)
            for nom in choix:
                prix = PRIX_NOURRITURE[nom]
                articles.append(
                    ArticleShop(
                        nom_affiche=nom,
                        prix=prix,
                        action=lambda inv, n=nom: _manger(inv, n)
                    )
                )
            return articles

        # 2) Locksmith -> clés, hammer, lockpick
        if nom_salle == LOCKSMITH_NAME:
            articles.append(
                ArticleShop(
                    "Clé",
                    5,
                    lambda inv: _ajouter_consommable(inv, "Clés", 1)
                )
            )
            articles.append(
                ArticleShop(
                    "Hammer",
                    100,
                    lambda inv: _debloquer_permanent(inv, "Hammer")
                )
            )
            articles.append(
                ArticleShop(
                    "Lockpick Kit",
                    120,
                    lambda inv: _debloquer_permanent(inv, "Lockpick Kit")
                )
            )
            return articles

        # 3) Autres shops jaunes -> 3 ou 4 items aléatoires (consommables + nourriture)
        if nom_salle in AUTRES_SHOPS_JAUNES:
            nb_items = random.randint(3, 4)
            pool = OBJETS_CONSOMMABLES_SHOP + NOURRITURES_NOMS
            choix = random.sample(pool, k=nb_items)

            for nom in choix:
                if nom in PRIX_CONSOMMABLES:
                    prix = PRIX_CONSOMMABLES[nom]
                    articles.append(
                        ArticleShop(
                            nom_affiche=nom,
                            prix=prix,
                            action=lambda inv, n=nom: _ajouter_consommable(inv, n, 1)
                        )
                    )
                elif nom in PRIX_NOURRITURE:
                    prix = PRIX_NOURRITURE[nom]
                    articles.append(
                        ArticleShop(
                            nom_affiche=nom,
                            prix=prix,
                            action=lambda inv, n=nom: _manger(inv, n)
                        )
                    )
            return articles

        # 4) par défaut : pas de boutique
        return []

    # API publique utilisée par le jeu / l'UI

    def lister_articles(self) -> List[Tuple[int, str, int]]:
        """Renvoie [(index, nom, prix), ...] pour l'affichage."""
        return [(i, a.nom_affiche, a.prix) for i, a in enumerate(self.articles)]

    def acheter_index(self, inventaire, index: int) -> bool:
        """Tente d'acheter l'article d'indice index."""
        if 0 <= index < len(self.articles):
            return self.articles[index].acheter(inventaire)
        return False

