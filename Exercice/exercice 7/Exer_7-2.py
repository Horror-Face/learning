#Exercice 2

# def afficher_menu():
#     print("1. Emprunter un livre")
#     print("2. Retourner un livre")
#     print("3. Quitter")

# def Afficher_Au_Revoir():
#     print("Merci et à bientôt!")

# afficher_menu()
# Afficher_Au_Revoir()

#exercice 3

ANNONCE = "RÈGLE DE LA BIBLIOTHÈQUE"
LARGEUR = 40
def afficher_ligne():
    print("-" * LARGEUR)

def afficher_regles():
    print("1. Parler à voix basse.")
    print("2. Aucune nourriture près des ordinateurs.")
    print("3. Rapporter les livres au comptoir.")
    print("4. Réserver les salles de travail en ligne.")

afficher_ligne()
print(f"{ANNONCE: ^40}")
afficher_ligne()
afficher_regles()
afficher_ligne()