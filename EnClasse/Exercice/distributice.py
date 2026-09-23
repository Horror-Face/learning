# Raphael Desjardins
# 2026-09-23
# exercice de la distributrice

PRIX_AVANT_TAXES = 100  # en cents
TAUX_TPS = 0.05
TAUX_TVQ = 0.09975

PRIX_EXACT = PRIX_AVANT_TAXES * (1 + TAUX_TPS + TAUX_TVQ)
PRIX_CAFE = round(PRIX_EXACT / 5) * 5  # 115 cents, soit 1.15 $

PIECE_TOONIE = 200   # 2.00 $
PIECE_LOONIE = 100   # 1.00 $
PIECE_QUART = 25     # 0.25 $
PIECE_DIX = 10       # 0.10 $
PIECE_CINQ = 5       # 0.05 $

GOBELETS_DEPART = 5
CAISSE_DEPART = 1000 

acceuil = "DISTRIBUTRICE"

valide = False

while not valide :
    try:
        print(f"={acceuil:=^40}=")
        print("1 - acheter un café ..... 1.15$")
        print("2 - Rapport des ventes")
        print("0 - Quitter")
        print("=" * 40)
        choix = int(input("Entrer votre choix : "))
    except :
        print("Entrer un choix valid")
    if choix == 1 or choix == 2 or choix == 0:
        valide = True
    else :
        print("Recommencer")

