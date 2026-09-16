# Raphael  Desjardins
# 2026-09-16
# boucle while

# import time

# compteur = 0

# while compteur < 5 :
#     compteur += 1
#     print("hello")
#     time.sleep(0.5)

# print("finis")

continuer = "oui"

while continuer == "oui" :
    valeur = int(input("Inscrire un nombre : "))
    valeur *= 2
    print(valeur)

    continuer = input("voulez-vous continuer? oui/non : ").lower().strip()
    # continuer = continuer.lower() # permet de mettre en minuscule l'input

print("fin")
