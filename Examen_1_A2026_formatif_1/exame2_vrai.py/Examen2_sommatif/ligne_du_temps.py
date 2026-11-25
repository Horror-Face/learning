"""Examen 2 - Programme 1 - Quiz : la ligne du temps du Québec (420-116-RI, A2026).

Le joueur doit deviner l'année de grands événements de l'histoire du Québec,
tirés au hasard. Une réponse exacte vaut 3 points et une réponse à 5 ans près
vaut 1 point. Les événements et leurs années sont dans donnees_examen_2.py.
Après chaque partie, on affiche le pointage et les événements à
réviser. À la fin, on affiche le nombre de parties et le meilleur résultat.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# TODO 1 : importer RANDOM, les fonctions lire_entier() et
#          lire_oui_non() de utilitaires.py, puis les listes QUESTIONS
#          et REPONSES de donnees_examen_2.py
import random
from utilitaires import (lire_entier, lire_oui_non)

from donnees_examen_2 import (EVENEMENTS, ANNEES)
# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 60
ANNEE_MIN = 1500
ANNEE_MAX = 2026
NB_QUESTIONS_MIN = 3
POINTS_EXACT = 3
POINTS_PROCHE = 1
ECART_TOLERE = 5
SEMENCE = 66          # pour avoir les mêmes questions que l'exemple de l'énoncé


# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_bienvenue():
    """Affiche la bannière et les règles du jeu."""
    print("=" * LARGEUR)
    print(f"{'QUIZ — LA LIGNE DU TEMPS DU QUÉBEC':^{LARGEUR}}")
    print("=" * LARGEUR)
    print(f"Réponse exacte : {POINTS_EXACT} points. "
          f"À {ECART_TOLERE} ans près : {POINTS_PROCHE} point.")


def calculer_pourcentage(points, points_max):
    """Calcule un pourcentage de réussite, arrondi à l'entier.

    Args:
        points (int): Les points obtenus.
        points_max (int): Le nombre maximal de points.

    Returns:
        int: Le pourcentage de réussite.
    """
    return round(points / points_max * 100)


def afficher_revision(evenements_rates, annees_rates):
    """Affiche la liste des événements à réviser.

    Args:
        evenements_rates (list): Les événements pour lesquels le joueur
            n'a obtenu aucun point.
        annees_rates (list): Les années de ces événements, associées par
            l'index à evenements_rates.
    """
    print()
    print("À RÉVISER")
    print("-" * LARGEUR)
    if len(evenements_rates) == 0:
        print("Rien à réviser, bravo!")
    else:
        for i in range(len(evenements_rates)):
            print(f"{annees_rates[i]}  {evenements_rates[i]}")
    print("-" * LARGEUR)


def calculer_points(reponse, annee):
    """Calcule les points obtenus pour une réponse.

    Args:
        reponse (int): L'année donnée par le joueur.
        annee (int): L'année exacte de l'événement.

    Returns:
        int: POINTS_EXACT si la réponse est exacte, POINTS_PROCHE si elle
            est à ECART_TOLERE ans près ou moins, 0 sinon.
    """
    # TODO 2 : indice : abs(x) renvoie la valeur absolue de x
    # if reponse == annee:
    #     return POINTS_EXACT
    # elif abs(reponse - annee) <= 5 or abs(reponse - annee) <= -5:
    #     return POINTS_PROCHE
    # else :
    #     return 0

    points = 0
    if reponse == annee:
        points = POINTS_EXACT
    elif annee != 0:
        ecart_relatif = abs(reponse - annee) / annee * 100
        if ecart_relatif <= ECART_TOLERE:
            points = POINTS_PROCHE
    return points
    
    pass

def jouer_partie(nb_questions):
    """Joue une partie, puis affiche le pointage et la révision.

    Les événements sont tirés au hasard, sans répétition.

    Args:
        nb_questions (int): Le nombre de questions de la partie.

    Returns:
        int: Le pourcentage de réussite de la partie.
    """
    # TODO 3 : voir l'énoncé (tirage avec random.sample(), questions
    #          numérotées, rétroaction, listes des événements ratés, bilan)
    points = 0
    points_max = nb_questions * POINTS_EXACT
    questions_ratees = []
    reponses_ratees = []

    # Tirage des index : une même question ne revient pas deux fois
    indexes = random.sample(range(len(EVENEMENTS)), nb_questions)

    for numero in range(nb_questions):
        index = indexes[numero]
        bonne_reponse = ANNEES[index]
        print()
        print(f"Question {numero + 1} de {nb_questions} — {EVENEMENTS[index]}")
        reponse = lire_entier("Réponse : ", ANNEE_MIN, ANNEE_MAX)

        gain = calculer_points(reponse, bonne_reponse)
        points += gain
        if gain == POINTS_EXACT:
            print(f"Exact! +{gain} points")
        elif gain == POINTS_PROCHE:
            print(f"Presque! C'était {bonne_reponse}. +{gain} point")
        else:
            print(f"Non, c'était {bonne_reponse}.")
            questions_ratees.append(EVENEMENTS[index])
            reponses_ratees.append(bonne_reponse)

    pourcentage = calculer_pourcentage(points, points_max)
    print()
    print(f"Pointage : {points} sur {points_max} ({pourcentage} %)")
    print()
    afficher_revision(questions_ratees, reponses_ratees)
    return pourcentage






    # indexes = random.sample(range(len(EVENEMENTS)), nb_questions)
    # for numero in range(nb_questions):
    #     index = indexes[numero]
    #     print()
    #     print(f"Question {numero + 1} de {nb_questions} — {EVENEMENTS[index]}")
    # calculer_points()
    pass

# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Déroule la session : bienvenue, parties à répétition, bilan final."""
    resultats = []

    afficher_bienvenue()
    random.seed()
#ajouter semence : random.seed(SEMENCE)
    rejouer = True
    while rejouer:
        print()
        nb_questions = lire_entier(
            f"Nombre de questions ({NB_QUESTIONS_MIN} à {len(EVENEMENTS)}) : ",
            NB_QUESTIONS_MIN, len(EVENEMENTS))
        resultats.append(jouer_partie(nb_questions))
        print()
        rejouer = lire_oui_non("Voulez-vous rejouer? (o/n) : ")

    print()
    print(f"Parties jouées : {len(resultats)}")
    print(f"Meilleur résultat : {max(resultats)} %")
    print("Merci d'avoir joué!")

if __name__ == "__main__":
    main()
