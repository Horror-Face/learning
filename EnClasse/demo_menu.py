import csv

produit = []
with open("EnClasse\menu.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    next(lecteur)
    for champ in lecteur:
        print(f"{champ[0]}")



    # fichier.readline()                        # on lit l'en-tête et on l'ignore
    # for ligne in fichier:
    #     champs = ligne.strip().split(",")
    #     produit = champs[0]
    #     prix = float(champs[2])
    #     stock = int(champs[3])
    #     print(f"{produit:<18}{prix:>6.2f} ${stock:>5}")