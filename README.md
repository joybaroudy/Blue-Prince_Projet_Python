Blue Prince est un jeu d’exploration en Python utilisant Pygame, inspiré du gameplay du jeu Blue Prince (Gheist).
Le joueur explore un manoir généré dynamiquement, pièce par pièce, en ouvrant des portes, découvrant des salles, collectant du loot, ouvrant des coffres, fouillant des casiers, visitant des boutiques et évitant l’épuisement de ses pas.


👉Le projet est structuré en modules indépendants pour gérer :

🔹les salles et leur tirage
🔹les portes et leur niveau de verrouillage
🔹le loot (au sol, coffres, casiers, digspots)
🔹les effets des salles
🔹l’affichage
🔹les commandes clavier
🔹l’inventaire du joueur
🔹le manoir et sa grille interne


**Arboresance du projet:**
Source_Code/
│
├── affichage.py              # Gestion de l’affichage du jeu (HUD, salles, loot)
├── Boutique.py               # Système de boutique (salles jaunes)
├── clavier.py                # Gestion du clavier, déplacements, ouverture de portes
├── Conteneurs.py             # Coffres, Casier, Digspot + génération de contenu
├── EffetsSalles.py           # Effets appliqués lors de l'entrée dans une salle
├── Inventory.py              # Gestion de l’inventaire (objets permanents/consommables)
├── joueur.py                 # Classe Joueur (position, mouvement)
├── main.py                   # Point d’entrée du jeu (boucle principale)
├── Manoir.py                 # Modèle interne du manoir (RoomCell, portes, loot)
├── Objets.py                 # Définition des objets, nourriture, consommables
├── RoomCell.py               # Modélisation d’une salle du manoir
├── SalleManager.py           # Tirage des salles, loot, conteneurs, digspots
├── Salles.py                 # Catalogue complet des salles (ID, prix, couleur, portes…)
├── TraitementBoutique.py     # Interaction avec la boutique
├── TraitementLoot.py         # Gestion de la prise de loot (sol)
│
└── images/                   # Images d’interface et salles
│    └── Images_Chambres/
│    
└── Image_initial

