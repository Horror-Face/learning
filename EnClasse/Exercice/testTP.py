mois = int(input("Entrez un nombre de mois : "))

annee = mois // 12
mois2 = mois % 12

print(f"{mois} fais exactement {annee} ans et {mois2} mois")