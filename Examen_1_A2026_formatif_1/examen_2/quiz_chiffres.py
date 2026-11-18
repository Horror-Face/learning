"""Examen 2 formatif - Programme 1 - Quiz : la culture générale en chiffres
(420-116-RI, A2026).

Le joueur doit trouver la réponse (un nombre entier) à des questions de
culture générale, tirées au hasard. Une réponse exacte vaut 3 points et une
réponse à 10 % près vaut 1 point. Les questions et leurs réponses sont dans
donnees_examen_2.py. Après chaque partie, on affiche le pointage et les
questions à réviser. À la fin, on affiche le nombre de parties et le
meilleur résultat.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# TODO 1 : importer RANDOM, les fonctions lire_entier() et
#          lire_oui_non() de utilitaires.py, puis les listes QUESTIONS
#          et REPONSES de donnees_examen_2.py
import random
from examen_2.utilitaires import (lire_entier, lire_oui_non)

from examen_2.donnees_examen_2 import (QUESTIONS, REPONSES)





# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 60
REPONSE_MIN = 0
REPONSE_MAX = 100000
NB_QUESTIONS_MIN = 3
POINTS_EXACT = 3
POINTS_PROCHE = 1
ECART_TOLERE = 10     # en % de la bonne réponse
SEMENCE = 66          # pour avoir les mêmes questions que l'exemple de l'énoncé
TITRE_JEU = ""


# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_bienvenue():
    """Affiche la bannière et les règles du jeu."""
    print("=" * LARGEUR)
    print(f"{'QUIZ — LA CULTURE GÉNÉRALE EN CHIFFRES':^{LARGEUR}}")
    print("=" * LARGEUR)
    print(f"Réponse exacte : {POINTS_EXACT} points. "
          f"À {ECART_TOLERE} % près : {POINTS_PROCHE} point.")


def calculer_pourcentage(points, points_max):
    """Calcule un pourcentage de réussite, arrondi à l'entier.

    Args:
        points (int): Les points obtenus.
        points_max (int): Le nombre maximal de points.

    Returns:
        int: Le pourcentage de réussite.
    """
    return round(points / points_max * 100)


def afficher_revision(questions_ratees, reponses_ratees):
    """Affiche la liste des questions à réviser.

    Args:
        questions_ratees (list): Les questions pour lesquels le joueur
            n'a obtenu aucun point.
        reponses_ratees (list): Les réponses de ces questions, associées par
            l'index à questions_ratees.
    """
    print()
    print("À RÉVISER")
    print("-" * LARGEUR)
    if len(questions_ratees) == 0:
        print("Rien à réviser, bravo!")
    else:
        for i in range(len(questions_ratees)):
            print(f"{reponses_ratees[i]:>6}  {questions_ratees[i]}")
    print("-" * LARGEUR)


def calculer_points(reponse, bonne_reponse):
    """Calcule les points obtenus pour une réponse.

    L'écart est relatif : il est calculé en pourcentage de la bonne réponse.

    Args:
        reponse (int): La réponse donnée par le joueur.
        bonne_reponse (int): La bonne réponse.

    Returns:
        int: POINTS_EXACT si la réponse est exacte, POINTS_PROCHE si l'écart
            est de ECART_TOLERE % ou moins de la bonne réponse, 0 sinon.
    """
    # TODO 2 : écart relatif (en %) = |reponse - bonne_reponse| / bonne_reponse * 100
    #          indice : abs(x) renvoie la valeur absolue de x
    pass

def jouer_partie(nb_questions):
    """Joue une partie, puis affiche le pointage et la révision.

    Les questions sont tirées au hasard, sans répétition.

    Args:
        nb_questions (int): Le nombre de questions de la partie.

    Returns:
        int: Le pourcentage de réussite de la partie.
    """
    # TODO 3 : voir l'énoncé (tirage avec random.sample(), questions
    #          numérotées, rétroaction, listes des questions ratées, bilan)
    pass

# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Fait jouer des parties tant que le joueur veut rejouer."""
    afficher_bienvenue()
    random.seed(SEMENCE) # À commenter pour avoir des questions aléatoires

    # TODO 4 : voir l'énoncé (nombre de questions, rejouer, résultats)

main()
