"""Quiz : la culture générale en chiffres.

Le joueur doit trouver la réponse (un nombre entier) à des questions de
culture générale tirées au hasard. Après chaque partie, on affiche son
pointage et les questions à réviser. Il peut ensuite rejouer.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# TODO 1 : imports
import random

from utilitaires import lire_entier, lire_oui_non
from donnees_examen_2 import QUESTIONS, REPONSES

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
REPONSE_MIN = 0
REPONSE_MAX = 100000
NB_QUESTIONS_MIN = 3
POINTS_EXACT = 3
POINTS_PROCHE = 1
ECART_TOLERE = 10
SEMENCE = 66
LARGEUR = 60


# ---------------------------------------------------------------------------
# Fonctions fournies
# ---------------------------------------------------------------------------
def afficher_bienvenue():
    """Affiche la bannière et les règles du jeu."""
    print("=" * LARGEUR)
    print(f"{'QUIZ - LA CULTURE GÉNÉRALE EN CHIFFRES':^{LARGEUR}}")
    print("=" * LARGEUR)
    print(f"Réponse exacte : {POINTS_EXACT} points. "
          f"À {ECART_TOLERE} % près : {POINTS_PROCHE} point.")


def calculer_pourcentage(points, points_max):
    """Calcule le pourcentage de réussite, arrondi à l'entier.

    Args:
        points (int): Les points obtenus.
        points_max (int): Les points possibles.

    Returns:
        int: Le pourcentage de réussite.
    """
    return round(points / points_max * 100)


def afficher_revision(questions_ratees, reponses_ratees):
    """Affiche les questions à réviser avec leur bonne réponse.

    Args:
        questions_ratees (list): Les questions à 0 point.
        reponses_ratees (list): Les bonnes réponses, dans le même ordre.
    """
    print("À RÉVISER")
    print("-" * LARGEUR)
    if len(questions_ratees) == 0:
        print("Rien à réviser, bravo!")
    else:
        for i in range(len(questions_ratees)):
            print(f"{reponses_ratees[i]:>6}  {questions_ratees[i]}")
    print("-" * LARGEUR)


# ---------------------------------------------------------------------------
# TODO 2 : calculer_points
# ---------------------------------------------------------------------------
def calculer_points(reponse, bonne_reponse):
    """Calcule les points gagnés pour une réponse.

    Args:
        reponse (int): La réponse du joueur.
        bonne_reponse (int): La bonne réponse.

    Returns:
        int: POINTS_EXACT si exacte, POINTS_PROCHE si l'écart relatif est
            d'au plus ECART_TOLERE %, sinon 0.
    """
    points = 0
    if reponse == bonne_reponse:
        points = POINTS_EXACT
    elif bonne_reponse != 0:
        ecart_relatif = abs(reponse - bonne_reponse) / bonne_reponse * 100
        if ecart_relatif <= ECART_TOLERE:
            points = POINTS_PROCHE
    return points


# ---------------------------------------------------------------------------
# TODO 3 : jouer_partie
# ---------------------------------------------------------------------------
def jouer_partie(nb_questions):
    """Joue une partie et affiche le bilan.

    Args:
        nb_questions (int): Le nombre de questions à poser.

    Returns:
        int: Le pourcentage de réussite de la partie.
    """
    points = 0
    points_max = nb_questions * POINTS_EXACT
    questions_ratees = []
    reponses_ratees = []

    # Tirage des index : une même question ne revient pas deux fois
    indexes = random.sample(range(len(QUESTIONS)), nb_questions)

    for numero in range(nb_questions):
        index = indexes[numero]
        bonne_reponse = REPONSES[index]
        print()
        print(f"Question {numero + 1} de {nb_questions} — {QUESTIONS[index]}")
        reponse = lire_entier("Réponse : ", REPONSE_MIN, REPONSE_MAX)

        gain = calculer_points(reponse, bonne_reponse)
        points += gain
        if gain == POINTS_EXACT:
            print(f"Exact! +{gain} points")
        elif gain == POINTS_PROCHE:
            print(f"Presque! C'était {bonne_reponse}. +{gain} point")
        else:
            print(f"Non, c'était {bonne_reponse}.")
            questions_ratees.append(QUESTIONS[index])
            reponses_ratees.append(bonne_reponse)

    pourcentage = calculer_pourcentage(points, points_max)
    print()
    print(f"Pointage : {points} sur {points_max} ({pourcentage} %)")
    print()
    afficher_revision(questions_ratees, reponses_ratees)
    return pourcentage


# ---------------------------------------------------------------------------
# TODO 4 : main
# ---------------------------------------------------------------------------
def main():
    """Déroule la session : bienvenue, parties à répétition, bilan final."""
    resultats = []

    afficher_bienvenue()
    random.seed(SEMENCE)

    rejouer = True
    while rejouer:
        print()
        nb_questions = lire_entier(
            f"Nombre de questions ({NB_QUESTIONS_MIN} à {len(QUESTIONS)}) : ",
            NB_QUESTIONS_MIN, len(QUESTIONS))
        resultats.append(jouer_partie(nb_questions))
        print()
        rejouer = lire_oui_non("Voulez-vous rejouer? (o/n) : ")

    print()
    print(f"Parties jouées : {len(resultats)}")
    print(f"Meilleur résultat : {max(resultats)} %")
    print("Merci d'avoir joué!")


main()