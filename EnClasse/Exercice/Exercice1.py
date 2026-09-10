#Raphaël Desjardins
#2026-09-10
#Exercice 4.1
#------------------------------------------
#Exercice 1 / marche
# Nombre = int(input("Entrez un nombre: "))

# if Nombre < 0:
#     print("Le nombre est négatif.")
# else :
#     print("Le nombre est positif.")
#------------------------------------------
#Éxercice 2 / marche
# age = int(input("Entrez votre âge: "))

# if age >= 18:
#     print("Vous êtes majeur.")
# else:
#     print("Vous êtes mineur.")
#---------------------------------------------
#Éxercice 3 / Marche
# MotDePasse = input("Entrez votre mot de passe : ")

# Longueur = len(MotDePasse)

# if Longueur >= 8:
#     print("Mot de passe accepté")
# else:
#     print("Mot de passe trop court")
#---------------------------------------------------
#Éxercice 4
# Unite = int(input("Veuiller rentrer un nombre entier : "))

# if Unite % 3 == 0 :
#     print("Multiple de 3")
# else:
#     print("Pas un multiple de 3")
#------------------------------------------------------
#Éxercice 5
Cote_a = int(input("Entrer le premier coté de votre triangle : "))
Cote_b = int(input("Entrer le deuxieme coté de votre triangle : "))
Cote_c = int(input("Entrer le troisieme coté de votre triangle : "))

if Cote_a == Cote_b or Cote_a == Cote_b or Cote_c == Cote_a :
    print("Triangle isocèle")
else:
    print("Triangle Scalène")