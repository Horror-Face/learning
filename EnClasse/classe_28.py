# Raphael Desjardins
# 2026-10-28
# constante et menu

NOM_ELEVE = "Henri"

def demande_choix(valeur_minimal, valeur_maximal):
    valide = False
    while not valide:
        try:
            choix = int(input(f"Entrez votre choix ({valeur_minimal} à {valeur_maximal}): ")) # ou conversion avec float()
            if valeur_minimal <= choix <= valeur_maximal:
                valide = choix
            else:
                print(f"La choix doit être entre {valeur_minimal} et {valeur_maximal}.")
        except ValueError:
            print("Ce n'est pas un nombre entier.")

def afficher_menu(prenom, option):
    print(f"bienvenue {prenom} dans mon programme!")
    for i in range(len(option)):
        print(option[i])
    print("--------------------------------------------------")
    
    valeur = demande_choix(1,len(option))
    return valeur

def option1():
    print("choix 1")

def option2():
    print("choix 2")
    
def option3():
    print("Choix 3")


############################## Programme principale ###############################

liste_option = []
liste_option.append("Modifier")
liste_option.append("Supprimer")
liste_option.insert(0,"Ajouter")

# afficher_menu("Raph")

option_choisis = afficher_menu("David", liste_option)
print(option_choisis)

match option_choisis:
    case 1:
        print("option 1")
    case 2:
        print("option 2")
    case 3:
        print("option 3")