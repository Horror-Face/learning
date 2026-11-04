import random
from TP2.donnees_tp2 import LISTE_PAYS, LISTE_CAPITALES

#CONSTANTE
#############
#Jeu
NB_QUESTION = 10
GRAINE = None
#saisie
LONGUEUR_NOM_MAX = 40
REPONSE_OUI = "oui"
REPONSE_NON = "non"
#Affichage
TITRE = "Jeu des capitals - Édition 2026"
AUTEUR = "Raphaël Desjardins"
LIGNE_ETOILE = "*" * 60

# Variables
############
rejouer = True

# Une seule initialisation du générateur, avant la toute premiere partir
random.seed(GRAINE )

#Fonction


