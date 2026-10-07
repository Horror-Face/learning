# Raphaël Desjardins
# 2026-09-30
# Examen 1 - parti pratique

#imports
import math
from colorama import Fore, Back, Style, init
init(autoreset=True)

#constante
GOMME_VALIDE = False
JOURS_VALIDE = False
RECETTE_VALIDE = False


#demande de saveur
while not GOMME_VALIDE :
    saveur = input("Saveur de gomme (menthe, fraise, raisin) : ").lower().strip()
    if saveur == "menthe" or saveur == "fraise" or saveur == "raisin" :
        GOMME_VALIDE = True
    elif saveur == "vanille":
        print(Fore.RED + "Basic, prend quelque chose dans les choix VALIDE")
    else :
        print(Fore.RED + "Cette saveur n'est pas offert, veuiller réessayer svp")

#temporaire, confirmer que sa marche
print("merci")

#objectif


#demande nombre de jour
while not JOURS_VALIDE :
    try:
        jours = int(input("Nombre de jours de vente cette semaine : "))

        if 1 <= jours <= 7 :
            JOURS_VALIDE = True

        else:
            print(Fore.RED + "Ce nombre est invalide, recommencer svp")

    except ValueError:
        print(Fore.RED + "Veuiller entrer un nombre entre 1 et 7")

    except AttributeError:
        print(Fore.RED + "Veuiller entrer un nombre entre 1 et 7")

#temporaire, confirmer que sa marche
print(f"Good, recette de {jours} jours")

#recette de chaque jours
NB_RECETTE = jours
recette_jour = 1

while recette_jour <= jours :
    try:
        nombre = float(input(f"Recette de jour {recette_jour} ($): "))
        if nombre > 20:
           print("entrer un nombre entre 0 et 20")
        elif nombre <= 20 and nombre >= 0:
            print("good")
            recette_jour += 1
    except ValueError :
        print("veuiller entrer un nombre")

print("suite en construction, revenez dans 2-3 mois et tout devrais marcher, peut-être.")

#pas été capable de garder les input de la variable "nombre" et de donc faire la suite
