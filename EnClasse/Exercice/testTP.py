import datetime

intro1 = "CLINIQUE VÉTÉRINAIRE EXOTIQUE"
intro2 = "DES ÎLES ST-MAURICE"

print("=" * 60)
print(f" {intro1:^58} ")
print(f" {intro2:^58} ")
print("=" * 60)

Date = datetime.datetime.now()

print(f"{Date.strftime("Bilan produit à: %H:%M"):>55}")