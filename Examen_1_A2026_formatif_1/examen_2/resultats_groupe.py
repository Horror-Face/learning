"""Examen 2 formatif - Programme 2 - Résultats d'un groupe (420-116-RI, A2026).

Affiche les résultats d'un groupe (une ligne par étudiant, une colonne par
évaluation) avec la moyenne de chaque étudiant, puis la meilleure note de
chaque évaluation, la note la plus faible et le nombre d'échecs.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 53
ETUDIANTS = ("Alice", "Benoît", "Chloé", "David", "Emma", "Frédéric")
# NOTES[l][c] : note (sur 100) de ETUDIANTS[l] à l'évaluation c + 1
NOTES = [
    [78, 85, 92, 74],
    [55, 62, 48, 70],
    [91, 88, 95, 90],
    [64, 59, 71, 66],
    [82, 77, 69, 88],
    [47, 68, 58, 61],
]
SEUIL_REUSSITE = 60


# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation.

    Args:
        caractere (str): Le caractère répété LARGEUR fois.
    """
    print(caractere * LARGEUR)


def calculer_moyenne(ligne):
    """Calcule la moyenne d'une liste de valeurs.

    Args:
        ligne (list): Les valeurs d'une ligne.

    Returns:
        float: La moyenne des valeurs.
    """
    total = 0
    for valeur in ligne:
        total += valeur
    return total / len(ligne)


def afficher_tableau(etudiants, notes, seuil):
    """Affiche le tableau des résultats du groupe.

    Chaque ligne contient le nom de l'étudiant, ses notes à chaque évaluation (suivies d'une marque « x »
    si elles sont sous le seuil de réussite) et sa moyenne.

    Args:
        etudiants (tuple): Le nom des étudiants.
        notes (list): La liste 2D des notes (une ligne par étudiant).
        seuil (int): La note minimale pour réussir.
    """
    # Ligne des titres : une colonne par évaluation
    print(f"{'Étudiant':<12}", end="")
    for no_col in range(len(notes[0])):
        print(f"{'E' + str(no_col + 1):>8}", end="")
    print(f"{'Moyenne':>9}")
    afficher_separateur("-")

    # TODO 1 : afficher une ligne par étudiant : son nom,
    #          ses notes à chaque évaluation (chacune suivie
    #          de « x » si elle est sous le seuil, d'une espace sinon),
    #          puis sa moyenne, obtenue avec calculer_moyenne().
    pass


def trouver_maximum_evaluation(notes, no_col):
    """Trouve la meilleure note d'une évaluation (une colonne).

    Args:
        notes (list): La liste 2D des notes.
        no_col (int): L'index de la colonne (0 pour la première).

    Returns:
        int: La meilleure note de cette évaluation.
    """
    # TODO 2
    pass


def trouver_note_minimale(notes):
    """Trouve la note la plus faible du groupe et sa position.

    En cas d'égalité, on garde la première rencontrée.

    Args:
        notes (list): La liste 2D des notes.

    Returns:
        tuple: L'index de l'étudiant, l'index de l'évaluation et la note.
    """
    # TODO 3 : parcours par index, sans min()
    pass


def compter_echecs(notes, seuil):
    """Compte les échecs (notes sous le seuil de réussite).

    Args:
        notes (list): La liste 2D des notes.
        seuil (int): La note minimale pour réussir.

    Returns:
        int: Le nombre de valeurs inférieures au seuil.
    """
    # TODO 4
    pass


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Affiche les résultats du groupe."""
    afficher_separateur("=")
    print(f"{'RÉSULTATS DU GROUPE':^{LARGEUR}}")
    afficher_separateur("=")
    afficher_tableau(ETUDIANTS, NOTES, SEUIL_REUSSITE)
    afficher_separateur("-")

    # TODO 5 : afficher la ligne « Maximum » (la meilleure note de chaque évaluation),
    #          une ligne de « = », la note la plus faible
    #          et le nombre d'échecs.


main()
