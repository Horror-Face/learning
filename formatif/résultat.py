"""Résultats d'un groupe : tableau des notes et statistiques.

Affiche les notes de six étudiants à quatre évaluations, leur moyenne,
la meilleure note de chaque évaluation, la note la plus faible du groupe
et le nombre d'échecs. Le programme s'adapte au nombre d'évaluations.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
ETUDIANTS = ("Alice", "Benoit", "Chloé", "David", "Emma", "Frédéric")
NOTES = [
    [78, 85, 92, 74],
    [55, 62, 48, 70],
    [91, 88, 95, 90],
    [64, 59, 71, 66],
    [82, 77, 69, 88],
    [47, 68, 58, 61],
]
SEUIL_REUSSITE = 60
LARGEUR = 54


# ---------------------------------------------------------------------------
# Fonctions fournies
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation.

    Args:
        caractere (str): Le caractère répété.
    """
    print(caractere * LARGEUR)


def calculer_moyenne(ligne):
    """Calcule la moyenne d'une liste de notes.

    Args:
        ligne (list): Les notes.

    Returns:
        float: La moyenne.
    """
    total = 0
    for note in ligne:
        total += note
    return total / len(ligne)


# ---------------------------------------------------------------------------
# TODO 1 : afficher_tableau
# ---------------------------------------------------------------------------
def afficher_tableau(etudiants, notes, seuil):
    """Affiche le tableau des résultats, une ligne par étudiant.

    Une note sous le seuil est suivie d'un x. La moyenne est affichée
    avec une décimale.

    Args:
        etudiants (tuple): Les noms des étudiants.
        notes (list): Une liste 2D : une ligne de notes par étudiant.
        seuil (int): La note minimale de réussite.
    """
    # Ligne des titres (fournie)
    print(f"{'Étudiant':<12}", end="")
    for evaluation in range(len(notes[0])):
        print(f"{'E' + str(evaluation + 1):>7} ", end="")
    print(f"{'Moyenne':>9}")
    afficher_separateur("-")

    for i in range(len(etudiants)):
        print(f"{etudiants[i]:<12}", end="")
        for j in range(len(notes[i])):
            marque = "x" if notes[i][j] < seuil else " "
            print(f"{notes[i][j]:>7}{marque}", end="")
        print(f"{calculer_moyenne(notes[i]):>9.1f}")


# ---------------------------------------------------------------------------
# TODO 2 : trouver_maximum_evaluation
# ---------------------------------------------------------------------------
def trouver_maximum_evaluation(notes, no_col):
    """Trouve la meilleure note d'une évaluation (une colonne).

    Args:
        notes (list): Une liste 2D de notes.
        no_col (int): L'index de l'évaluation.

    Returns:
        int: La meilleure note de cette évaluation.
    """
    maximum = notes[0][no_col]
    for i in range(len(notes)):
        if notes[i][no_col] > maximum:
            maximum = notes[i][no_col]
    return maximum


# ---------------------------------------------------------------------------
# TODO 3 : trouver_note_minimale
# ---------------------------------------------------------------------------
def trouver_note_minimale(notes):
    """Trouve la note la plus faible du groupe.

    En cas d'égalité, la première rencontrée est conservée.

    Args:
        notes (list): Une liste 2D de notes.

    Returns:
        tuple: (index de l'étudiant, index de l'évaluation, note minimale).
    """
    index_etudiant = 0
    index_evaluation = 0
    minimum = notes[0][0]
    for i in range(len(notes)):
        for j in range(len(notes[i])):
            if notes[i][j] < minimum:
                minimum = notes[i][j]
                index_etudiant = i
                index_evaluation = j
    return index_etudiant, index_evaluation, minimum


# ---------------------------------------------------------------------------
# TODO 4 : compter_echecs
# ---------------------------------------------------------------------------
def compter_echecs(notes, seuil):
    """Compte les notes inférieures au seuil de réussite.

    Args:
        notes (list): Une liste 2D de notes.
        seuil (int): La note minimale de réussite.

    Returns:
        int: Le nombre de notes sous le seuil.
    """
    nb_echecs = 0
    for ligne in notes:
        for note in ligne:
            if note < seuil:
                nb_echecs += 1
    return nb_echecs


# ---------------------------------------------------------------------------
# TODO 5 : main
# ---------------------------------------------------------------------------
def main():
    """Affiche le tableau des résultats puis les statistiques du groupe."""
    # Bannière (fournie)
    afficher_separateur("=")
    print(f"{'RÉSULTATS DU GROUPE':^{LARGEUR}}")
    afficher_separateur("=")

    afficher_tableau(ETUDIANTS, NOTES, SEUIL_REUSSITE)

    # Ligne Maximum : la meilleure note de chaque évaluation
    afficher_separateur("-")
    print(f"{'Maximum':<12}", end="")
    for evaluation in range(len(NOTES[0])):
        print(f"{trouver_maximum_evaluation(NOTES, evaluation):>7} ", end="")
    print()
    afficher_separateur("=")

    # Note la plus faible et échecs
    index_etudiant, index_evaluation, note = trouver_note_minimale(NOTES)
    print(f"Note la plus faible : {note} "
          f"({ETUDIANTS[index_etudiant]}, évaluation {index_evaluation + 1})")
    nb_echecs = compter_echecs(NOTES, SEUIL_REUSSITE)
    print(f"Échecs (moins de {SEUIL_REUSSITE}) : {nb_echecs}")


main()