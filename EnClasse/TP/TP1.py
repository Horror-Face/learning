# Raphaël Desjardins
# 2026-09-14
# TP1-clinique vétérinaire exotique

import math

#Info sur l'animal
animal = input("Entrer le nom de l'animal : ")

print("requin = 1 / tigre = 2 / gnou = 3")

espece= int(input("Entrer le numéro de l'espèce : "))

age = int(input("Entrez l'âge total en mois : "))

temperature = float(input("Entrez la tempéature de l'animal : "))

masse = float(input("entrez la masse de l'animal : "))

info = "INFORMATION SUR LE SPÉCIMEN"

#interface
print(f"{info:-^102}")
print(f"Nom de l'animal : {animal}")
print(f"Espèce de l'animal : {espece}")
print(f"Âge de l'animal (en mois) : {age}")
print(f"Masse de l'animal (en livres) : {masse}")
print(f"Température corporelle de l'animal (en °F) : {temperature}")

#------------------------------------------------------------------------
#convertir mes données

# livre en kilo
masse_kg = masse * 0.45

#Faren en celcsius
temp_c = ( temperature - 32) * ( 5 / 9 )

#mois en anne
annee = age // 12
mois = age % 12

# ---------------------------------------------------------------------------
# tableau de résultat
score_vita = 100

match espece:
    case 1:
        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30
    case 2:
        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30
    case 3:
        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30


print({score_vita})



