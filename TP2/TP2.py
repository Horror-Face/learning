import random
from donnees_tp2 import PAYS, CAPITALES_PAYS
import utilitaires

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
liste_de_niveau = ["facile", "moyen", "difficile"]
liste_question = [5, 10, 15]

liste_mode = []
liste_option_niveau = []
for i in range(len(liste_de_niveau)):
    option_courante = f"{i+1} - {liste_de_niveau[i]}"
    liste_option_niveau.append(option_courante)

#def afficher_menu

#afficher_menu("NIVEAU" )



