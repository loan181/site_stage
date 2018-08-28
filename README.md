# Site pour l'apprentissage de Scratch aux jeunes
Site destiné à l'apprantissage de [Scratch](https://scratch.mit.edu/) à des jeunes destiné pour l'A.S.B.L. Roue de Secours.

## Mise en route

### Prérequis
Ce projet nécessite l'installation au préalable de python 3.6.X ainsi que Django version 2.X
###### Python 
Sur le [site officiel de Python](https://www.python.org/downloads/)
###### Django
Avec pip (après avoir installé Python)
```sh
pip install django
```

### Lancement
```sh
cd site_stage
```

#### Local
```sh
python manage.py runserver
```
Le site sera ensuite accessible localement (sur l'adresse [127.0.0.1:8000](127.0.0.1:8000))

#### Réseau local (LAN)
```sh
python manage.py runserver 0.0.0.0:8000
```
Le site sera ensuite accessible dans le réseau local, donc pour tout les ordinateurs également conectés au même réseau que le tiens.
Il faudra que les autre ordinateurs tape l'adresse IP de ton ordinateur dans le réseau suivi de `:8000`.

Tu peux toujours y accéder localement avec [127.0.0.1:8000](127.0.0.1:8000), mais uniquement sur l'ordinateur qui à lancé le site.

##### Windows
Taper dans l'invité de commande `ipconfig`, l'adresse IP devrait apparaitre dans la ligne :
```
(Moyen de connexion) :
   (...)
   Adresse IPv4. . . . . . . . . . . . . .: XXX.XXX.XXX.XXX
   (...)
```

##### Apple
Donner dans l'application "Préférences système" dans "Réseau"

##### GNU+Linux
(pas testé, check sur internet)

## Structure
Le site est structuré avec une disposition bien particulière :
   1) [Concept](#concept)
   2) [Projet personnel](#projet-personnel)
   
Qu'on retrouve disposé sur la page principale du site

### Concept
Les concepts que j'ai jugé fondamentaux sont déjà sur le site, voiçi leur liste :
- (Mouvement) :
    - Orientation
        - Avancer
    - Coordonnée
- Collision
- Variable
- Message
- Clones

Autres idées qui n'ont pas (encore) était ajoutés :
- Stylo
- Temps
- (Création de) bloc
- Entrée(s) de bloc

#### Introduction
On commence par un petit résumé du cas d'utilisation du concept, à quoi va-t'il servir ?
Ensuite vient l'ensemble des blocs qui nous seront utiles pour le concept parfois suivis d'information supplémentaire.

#### Exemple(s)
Vient une série d'exemples qui utilise le concept. Ils servent notamment à l'élève à visualiser dans un contexte utile des cas d'application du concept

#### Défi(s)
Après ça il y à une série de défis qui servent d'exercice à l'élève pour mieux appréhender le concept.


### Projet Personnel
Cette partie consiste à laisser l'élève libre court à son imagination pour qu'il développe son propre projet à l'aide des concepts vus précédemment.

Une première page sert de guide aux élèves pour réaliser à bien leurs projets.

Des propositions de jeux sont données classé par difficulté décroissante. tous ne nécessite que l'utilisation des concepts de mouvements et de collisions.
mais libre à l'élève d'ajouter d'autres concepts s'il à eut le temps de les voir. ils ne servent que de modèles si l'enfant n'à pas d'idées.
Les détails des projets proposés sont exprès très vague et généralement sans code afin de laisser plus de liberté et d'autonomie au jeune.

### Slides
Les slides que j'ai préparé et également disponible depuis la page principale, elles contiennent les corrections des exercices également et des détails sur certaines choses qui ne sont pas mises sur le site

### Mode admin
Certaines choses supplémentaire sont ajouté si vous êtes considéré comme administrateur (c-à-d connecté en `localhost` ou `127.0.0.1`), tel que :
- Corrections des défis des [Concept](#concept)

## Modifier le site

## Auteurs
- Loan Sens - Commencement du site