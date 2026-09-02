# Raphaël Desjardins
# 2026-09-02
# cours 3

import time

print("Je vais deviner ton nombre")
#peut pas mettre autre chose que un int / nombre
chiffre = int(input("Donne moi un chiffre ? "))
chiffre = int(chiffre)
print(f"merci pour ce {chiffre}") 

contenue_type = type(chiffre)

compteur = chiffre
compte_final = compteur + 10
"""
while True:
    compteur += 1
    print(compteur)
    time.sleep(0.3)
    if compteur < compte_final:
        continue
    break

print(f"Ton nombre de base étais {chiffre} et c'est désormais {compteur}")
"""