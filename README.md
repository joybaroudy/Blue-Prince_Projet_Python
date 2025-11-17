**README : Blue Prince (Python / Pygame Project)**

Ce projet est un jeu d’exploration en Python utilisant Pygame, inspiré du gameplay du jeu Blue Prince.
Le joueur explore un manoir généré dynamiquement, pièce par pièce, en ouvrant des portes, découvrant des salles, collectant du loot, ouvrant des coffres, fouillant des casiers, visitant des boutiques et évitant l’épuisement de ses pas.

**1. Structure du projet**

Le projet est organisé en modules indépendants qui gèrent :
les salles et leur tirage
les portes et leurs niveaux de verrouillage
le loot (sol, coffres, casiers, digspots)
les effets des salles
l’affichage
les commandes clavier
l’inventaire du joueur
le manoir et sa grille interne


**2. Arborescence du dossier Source_Code/ :**
Source_Code/
│
├── affichage.py              
├── Boutique.py               
├── clavier.py                
├── Conteneurs.py             
├── EffetsSalles.py           
├── Inventory.py              
├── joueur.py                 
├── main.py                   
├── Manoir.py                 
├── Objets.py                 
├── RoomCell.py               
├── SalleManager.py           
├── Salles.py                 
├── TraitementBoutique.py     
├── TraitementLoot.py         
│
└── images/
    │
    ├── Images_Chambres/      
    └── Image_initial/        



**3. Installation**
1. Installer Python
Téléchargement :
https://www.python.org/downloads/

Assurez-vous d’activer “Add to PATH”.

2. Installer les dépendances
Depuis un terminal dans Source_Code :
pip install pygame

-> Lancer le jeu
Toujours dans Source_Code : Ecrire : **python main.py** et executer




**4. Commandes du jeu**
Touche	Action
Z / ↑	Monter
S / ↓	Descendre
Q / ←	Aller à gauche
D / →	Aller à droite
Entrée	Confirmer un choix lors d’un tirage
O	Ouvrir une porte / coffre / conteneur
N	Ne pas ouvrir
Quitter fenêtre	Fermer le jeu




**5. Fonctionnement du manoir**

Le manoir est une grille 5 × 9 gérée par Manoir.py.
Chaque case (RoomCell) contient :

l’ID de la salle
les conteneurs et digspots
le loot au sol
les portes + niveaux de verrouillage
un statut explored persisté
Une salle n’est tirée et générée qu’à la première visite.



**6. Tirage des salles (SalleManager)**

Le tirage dépend de :
la rareté et le prix
les portes disponibles
la position
les conditions (Corner, Edge, Normal)

les règles de priorité (au moins une salle gratuite au début)



**7. Les niveaux des portes :**

0 → gratuit
1 → clé OU lockpick
2 → clé obligatoire



**8. Système de loot**
Loot au sol
Tiré à l'entrée de la salle (rare, aléatoire, modifié par bonus/permanents).
Coffres (Coffre)
1. une clé requise
2. Ouverts gratuitement si Hammer est possédé
Casiers (Casier)
1. uniquement des consommables
2. toujours 1 clé
Digspots (Digspot) :
1. uniquement dans salles Green
2. nécessite Shovel



**9. Boutiques (salles jaunes)**
Ouvrent automatiquement une boutique (gérée dans TraitementBoutique.py).
Permettent d’acheter divers objets.
