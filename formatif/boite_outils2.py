"""Boîte à outils pour l'examen 2 : patrons prêts à copier et à adapter.

Contenu :
    1. Imports du modèle à plusieurs fichiers
    2. Notation avec écart absolu et relatif
    3. Patron d'une partie (tirage, boucle for numérotée, cumul, questions ratées, bilan)
    4. Patron « rejouer » (while, liste resultats, max)
    5. Opérations sur les listes 2D : lignes, colonnes, toute la liste, comptages

Les fonctions 2D n'utilisent ni min() ni max() : elles se recopient telles quelles
quand l'énoncé interdit ces fonctions. Renomme-les et adapte-les au besoin.

Auteur : Raphaël Desjardins
"""

# ===========================================================================
# 1. IMPORTS (modèle à plusieurs fichiers)
# ===========================================================================
# import random
# from utilitaires import lire_entier, lire_oui_non
# from donnees_examen_2 import QUESTIONS, REPONSES
#
# Rappels :
#   - les fichiers sont dans le MÊME dossier;
#   - lancer le programme principal, pas le module;
#   - random.seed(SEMENCE) UNE seule fois, avant la toute première partie.


# ===========================================================================
# 2. NOTATION AVEC TOLÉRANCE
# ===========================================================================
def calculer_points(reponse, bonne_reponse, points_exact, points_proche,
                    ecart_absolu=0, ecart_relatif=0):
    """Calcule les points d'une réponse numérique avec une tolérance.

    Une réponse est « proche » si son écart absolu (en unités : années,
    dollars...) OU son écart relatif (en % de la bonne réponse) est dans la
    tolérance. Une tolérance à 0 est désactivée.

    Args:
        reponse (int): La réponse du joueur.
        bonne_reponse (int): La bonne réponse.
        points_exact (int): Les points pour une réponse exacte.
        points_proche (int): Les points pour une réponse proche.
        ecart_absolu (float, optional): L'écart permis en unités. Par défaut 0.
        ecart_relatif (float, optional): L'écart permis en %. Par défaut 0.

    Returns:
        int: points_exact, points_proche ou 0.
    """
    points = 0
    ecart = abs(reponse - bonne_reponse)
    if ecart == 0:
        points = points_exact
    elif ecart_absolu > 0 and ecart <= ecart_absolu:
        points = points_proche
    elif ecart_relatif > 0 and bonne_reponse != 0:
        if ecart / bonne_reponse * 100 <= ecart_relatif:
            points = points_proche
    return points


# ===========================================================================
# 3. PATRON D'UNE PARTIE
# ===========================================================================
# def jouer_partie(nb_questions):
#     """Joue une partie et renvoie son pourcentage de réussite."""
#     points = 0
#     points_max = nb_questions * POINTS_EXACT
#     questions_ratees = []
#     reponses_ratees = []
#
#     indexes = random.sample(range(len(QUESTIONS)), nb_questions)   # sans répétition
#
#     for numero in range(nb_questions):
#         index = indexes[numero]
#         print()
#         print(f"Question {numero + 1} de {nb_questions} — {QUESTIONS[index]}")
#         reponse = lire_entier("Réponse : ", REPONSE_MIN, REPONSE_MAX)
#         gain = calculer_points(reponse, REPONSES[index])
#         points += gain                                              # cumul
#         if gain == POINTS_EXACT:
#             print(f"Exact! +{gain} points")
#         elif gain == POINTS_PROCHE:
#             print(f"Presque! C'était {REPONSES[index]}. +{gain} point")
#         else:
#             print(f"Non, c'était {REPONSES[index]}.")
#             questions_ratees.append(QUESTIONS[index])               # liste des ratées
#             reponses_ratees.append(REPONSES[index])
#
#     pourcentage = calculer_pourcentage(points, points_max)
#     print(f"Pointage : {points} sur {points_max} ({pourcentage} %)")
#     afficher_revision(questions_ratees, reponses_ratees)
#     return pourcentage


# ===========================================================================
# 4. PATRON « REJOUER »
# ===========================================================================
# def main():
#     resultats = []
#     afficher_bienvenue()
#     random.seed(SEMENCE)
#     rejouer = True
#     while rejouer:
#         nb = lire_entier(f"Nombre de questions ({MIN} à {len(QUESTIONS)}) : ", MIN, len(QUESTIONS))
#         resultats.append(jouer_partie(nb))
#         rejouer = lire_oui_non("Voulez-vous rejouer? (o/n) : ")
#     print(f"Parties jouées : {len(resultats)}")
#     print(f"Meilleur résultat : {max(resultats)} %")       # max() permis ici
#     print("Merci d'avoir joué!")


# ===========================================================================
# 5. LISTES 2D
# ===========================================================================
# --- Par ligne -------------------------------------------------------------
def somme_ligne(ligne):
    """Additionne les valeurs d'une ligne.

    Args:
        ligne (list): Une liste de nombres.

    Returns:
        float: La somme.
    """
    total = 0
    for valeur in ligne:
        total += valeur
    return total


def moyenne_ligne(ligne):
    """Calcule la moyenne d'une ligne.

    Args:
        ligne (list): Une liste de nombres (non vide).

    Returns:
        float: La moyenne.
    """
    return somme_ligne(ligne) / len(ligne)


def min_ligne(ligne):
    """Trouve la plus petite valeur d'une ligne.

    Args:
        ligne (list): Une liste de nombres (non vide).

    Returns:
        float: Le minimum.
    """
    minimum = ligne[0]
    for valeur in ligne:
        if valeur < minimum:
            minimum = valeur
    return minimum


def max_ligne(ligne):
    """Trouve la plus grande valeur d'une ligne.

    Args:
        ligne (list): Une liste de nombres (non vide).

    Returns:
        float: Le maximum.
    """
    maximum = ligne[0]
    for valeur in ligne:
        if valeur > maximum:
            maximum = valeur
    return maximum


# --- Par colonne -----------------------------------------------------------
def somme_colonne(liste_2d, no_col):
    """Additionne les valeurs d'une colonne.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        no_col (int): L'index de la colonne.

    Returns:
        float: La somme de la colonne.
    """
    total = 0
    for i in range(len(liste_2d)):
        total += liste_2d[i][no_col]
    return total


def moyenne_colonne(liste_2d, no_col):
    """Calcule la moyenne d'une colonne.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        no_col (int): L'index de la colonne.

    Returns:
        float: La moyenne de la colonne.
    """
    return somme_colonne(liste_2d, no_col) / len(liste_2d)


def min_colonne(liste_2d, no_col):
    """Trouve la plus petite valeur d'une colonne.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        no_col (int): L'index de la colonne.

    Returns:
        float: Le minimum de la colonne.
    """
    minimum = liste_2d[0][no_col]
    for i in range(len(liste_2d)):
        if liste_2d[i][no_col] < minimum:
            minimum = liste_2d[i][no_col]
    return minimum


def max_colonne(liste_2d, no_col):
    """Trouve la plus grande valeur d'une colonne.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        no_col (int): L'index de la colonne.

    Returns:
        float: Le maximum de la colonne.
    """
    maximum = liste_2d[0][no_col]
    for i in range(len(liste_2d)):
        if liste_2d[i][no_col] > maximum:
            maximum = liste_2d[i][no_col]
    return maximum


# --- Sur toute la liste ----------------------------------------------------
def trouver_min(liste_2d):
    """Trouve la plus petite valeur de la liste 2D (la première en cas d'égalité).

    Args:
        liste_2d (list): Une liste de listes de nombres.

    Returns:
        tuple: (index de la ligne, index de la colonne, valeur).
    """
    ligne_min = 0
    col_min = 0
    valeur_min = liste_2d[0][0]
    for i in range(len(liste_2d)):
        for j in range(len(liste_2d[i])):
            if liste_2d[i][j] < valeur_min:
                valeur_min = liste_2d[i][j]
                ligne_min = i
                col_min = j
    return ligne_min, col_min, valeur_min


def trouver_max(liste_2d):
    """Trouve la plus grande valeur de la liste 2D (la première en cas d'égalité).

    Args:
        liste_2d (list): Une liste de listes de nombres.

    Returns:
        tuple: (index de la ligne, index de la colonne, valeur).
    """
    ligne_max = 0
    col_max = 0
    valeur_max = liste_2d[0][0]
    for i in range(len(liste_2d)):
        for j in range(len(liste_2d[i])):
            if liste_2d[i][j] > valeur_max:
                valeur_max = liste_2d[i][j]
                ligne_max = i
                col_max = j
    return ligne_max, col_max, valeur_max


# --- Comptages -------------------------------------------------------------
def compter_au_moins(liste_2d, seuil):
    """Compte les valeurs supérieures ou égales au seuil.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        seuil (float): Le seuil.

    Returns:
        int: Le nombre de valeurs >= seuil.
    """
    compte = 0
    for ligne in liste_2d:
        for valeur in ligne:
            if valeur >= seuil:
                compte += 1
    return compte


def compter_sous(liste_2d, seuil):
    """Compte les valeurs strictement inférieures au seuil.

    Args:
        liste_2d (list): Une liste de listes de nombres.
        seuil (float): Le seuil.

    Returns:
        int: Le nombre de valeurs < seuil.
    """
    compte = 0
    for ligne in liste_2d:
        for valeur in ligne:
            if valeur < seuil:
                compte += 1
    return compte


if __name__ == "__main__":
    # Tests rapides (lancer ce fichier directement)
    notes = [[78, 85, 92, 74], [55, 62, 48, 70], [47, 68, 58, 61]]
    assert somme_ligne(notes[0]) == 329 and moyenne_ligne([60, 70]) == 65
    assert min_ligne(notes[1]) == 48 and max_ligne(notes[1]) == 70
    assert somme_colonne(notes, 0) == 180 and moyenne_colonne(notes, 0) == 60
    assert min_colonne(notes, 1) == 62 and max_colonne(notes, 3) == 74
    assert trouver_min(notes) == (2, 0, 47) and trouver_max(notes) == (0, 2, 92)
    assert compter_au_moins(notes, 70) == 5 and compter_sous(notes, 60) == 4
    assert calculer_points(1500, 1440, 3, 1, ecart_relatif=10) == 1
    assert calculer_points(1440, 1440, 3, 1) == 3 and calculer_points(1900, 1914, 3, 1, ecart_absolu=5) == 0
    assert calculer_points(1910, 1914, 3, 1, ecart_absolu=5) == 1
    print("Tous les tests passent.")