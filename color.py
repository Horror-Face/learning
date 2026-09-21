# Auteur: Raphaël Desjardins
# Date: 2026-09-21
# Description: couleur



# importations "à la pièce"
# on importe seulement ces 4 éléments du module
from colorama import Fore, Back, Style, init
init(autoreset=True)


#Print classic
print ("Hello, World!")

#print avec une value
my_name = "Raph"
print("Hello and welcome " + my_name + "!")

#texte est de couleur
print(Fore.RED + "Texte en rouge")
print(Fore.GREEN + "Texte en vert")

#texte est sur fond de couleur
print(Back.RED + "Texte sur fond rouge")
print(Back.BLUE + "Texte sur fond bleu")

#texte a un style
print(Style.BRIGHT + Fore.CYAN + "Texte vif en cyan")

#combinée
print(Style.BRIGHT + Fore.WHITE + Back.RED + "Erreur critique")

#Exemple
print("1. Facile")
print("2. Intermédiaire")
print("3. Avancé")

choix = input("Quel est votre choix ? ")

if choix == "1":
    print(Fore.GREEN + "Vous avez choisi le niveau Facile.")
elif choix == "2":
    print(Fore.YELLOW + "Vous avez choisi le niveau Intermédiaire.")
elif choix == "3":
    print(Fore.BLUE + "Vous avez choisi le niveau Avancé.")
else:
    print(Back.WHITE + Fore.RED + Style.BRIGHT + "Choix invalide!")