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
masse_kg = masse * 0.453592

#Faren en celcsius
temp_c = ( temperature - 32) * ( 5 / 9 )

#mois en anne
annee = age // 12
mois = age % 12


# ---------------------------------------------------------------------------
# tableau de résultat
score_vita = 100

maturite = ""

sorte = ""

norme_temp = ""
norme_mass = ""

verdict = "Normal"

limite = "non"

match espece:
    case 1:
        sorte = "requin"
        norme_temp = "22.0-26.0"
        norme_mass = "60.0-150.0"

        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30
            
        if age < 60 :
            maturite = "juvénile"
        elif age >= 60 and age < 240 :
            maturite = "Adulte"
        elif age >= 240 :
            maturite = "Senior"
            
        if temp_c < 26.0 and temp_c > 22.0 :
            verdict = "urgence"
            
        if math.isclose(masse_kg, 150.0) :
            limite = "oui"
        if math.isclose(temp_c, 26.0) :
            limite = "oui"
            
    case 2:
        sorte = "tigre"
        norme_temp = "37.5-39.0"
        norme_mass = "100.0-260.0"

        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30
        if age < 36 :
            maturite = "juvénile"
        elif age >= 36 and age < 144 :
            maturite = "Adulte"
        elif age >= 144 :
            maturite = "Senior"
        if temp_c < 26.0 and temp_c > 22.0 :
            verdict = "urgence"

        if math.isclose(masse_kg, 260.0) :
            limite = "oui"
        if math.isclose(temp_c, 39.0) :
            limite = "oui"

    case 3:
        sorte = "gnou"
        norme_temp = "37.5-39.0"
        norme_mass = "120.0-270.0"

        if masse_kg < 60.0 or masse_kg > 150.0 :
            score_vita -= 20
        if temp_c < 22.0 or temp_c > 26.0 :
            score_vita -= 30
        if age < 36 :
            maturite = "juvénile"
        elif age >= 36 and age < 180 :
            maturite = "Adulte"
        elif age >= 180 :
            maturite = "Senior"
        
        if math.isclose(masse_kg, 270.0) :
            limite = "oui"
        if math.isclose(temp_c, 39.0) :
            limite = "oui"
            
#--------------------------------------------------------
#final

intro1 = "CLINIQUE VÉTÉRINAIRE EXOTIQUE"
intro2 = "DES ÎLES ST-MAURICE"

if score_vita < 100:
    verdict = "surveillance"
    
if score_vita <= 50:
    verdict = "urgence"
    


print("=" * 60)

print(f" {intro1:^58} ")

print(f" {intro2:^58} ")

print("=" * 60)

print(f"Patient :{animal} ({sorte})")
print(f"Âge :{annee} ans et {mois} mois ({maturite})")
print(f"Saisie :Masse en lbs, température en °F")

print("-" * 60)

print("mesure valeur norme")
print(f"tempéranture (°C) {temp_c:.2f} {norme_temp}")
print(f"Masse (KG) {masse_kg:.2f} {norme_mass}")

print("-" * 60)

print("conversion")
print(f"masse : {masse} lbs = {masse_kg:.2f} Kg" )
print(f"Température : {temperature} °F = {temp_c:.2f} °C")

print("-" * 60)

print(f"mesure a la limte :{limite}")

print("-" * 60)

print(f"indice de vitalité : {score_vita}/100")
print(f" VERDICT : {verdict}")

print("=" * 60)

