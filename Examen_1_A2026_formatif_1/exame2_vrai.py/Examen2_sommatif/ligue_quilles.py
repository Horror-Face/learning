"""Examen 2 - Programme 2 - Ligue de quilles du jeudi (420-116-RI, A2026).

Affiche le tableau des pointages de la soirée (une ligne par joueur, une
colonne par partie), puis quelques statistiques : la moyenne de chaque
partie, le meilleur pointage de la soirée et le nombre de parties étoilées.

Auteur : Raphaël Desjardins
Date   : 2026-11-18
"""

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR = 50
JOUEURS = ("Annie", "Bruno", "Carole", "Denis", "Élise", "Félix")
# POINTAGES[l][c] : pointage du joueur JOUEURS[l] à la partie c + 1
POINTAGES = [
    [145, 162, 138],
    [121, 98, 134],
    [187, 205, 176],
    [156, 149, 171],
    [102, 118, 95],
    [168, 174, 190],
]
SEUIL_ETOILE = 150


# ---------------------------------------------------------------------------
# Fonctions
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation.

    Args:
        caractere (str): Le caractère répété LARGEUR fois.
    """
    print(caractere * LARGEUR)


def calculer_total(ligne):
    """Calcule le total d'une liste de pointages.

    Args:
        ligne (list): Les pointages d'un joueur.

    Returns:
        int: La somme des pointages.
    """
    total = 0
    for pointage in ligne:
        total += pointage
    return total


def afficher_tableau(joueurs, pointages, seuil):
    """Affiche le tableau des pointages de la soirée.

    Chaque ligne contient le nom du joueur, ses pointages (suivis d'une
    étoile s'ils atteignent le seuil) et son total.

    Args:
        joueurs (tuple): Le nom des joueurs.
        pointages (list): La liste 2D des pointages (une ligne par joueur).
        seuil (int): Le pointage minimal pour obtenir une étoile.
    """
    # Ligne des titres : une colonne par partie
    print(f"{'Joueur':<10}", end="")
    for no_partie in range(len(pointages[0])):
        print(f"{'P' + str(no_partie + 1):>8}", end="")
    print(f"{'Total':>8}")
    afficher_separateur("-")

    # TODO 1 : afficher une ligne par joueur : son nom, chacun de ses
    #          pointages (suivi de « * » s'il atteint le seuil, d'une espace
    #          sinon), puis son total, obtenu avec calculer_total().
    for i in range(len(joueurs)):
        print(f"{joueurs[i]:<12}", end="")
        for j in range(len(pointages[i])):
            marque = "x" if pointages[i][j] < seuil else " "
            print(f"{pointages[i][j]:>7}{marque}", end="")
        print(f"{calculer_total(pointages[i]):>9.1f}")

    pass

def calculer_moyenne_partie(pointages, no_partie):
    """Calcule la moyenne des joueurs pour une partie (une colonne).

    Args:
        pointages (list): La liste 2D des pointages.
        no_partie (int): L'index de la colonne (0 pour la partie 1).

    Returns:
        float: La moyenne des pointages de cette partie.
    """
    # TODO 2
    maximum = pointages[0][no_partie]
    for i in range(len(pointages)):
        if pointages[i][no_partie] > maximum:
            maximum = pointages[i][no_partie]
    return maximum
    pass

def trouver_meilleur_pointage(pointages):
    """Trouve le meilleur pointage de la soirée et sa position.

    En cas d'égalité, on garde le premier rencontré.

    Args:
        pointages (list): La liste 2D des pointages.

    Returns:
        tuple: L'index du joueur, l'index de la partie et le pointage.
    """
    # TODO 3 : parcours par index, sans max()
    index_joueurs = 0
    index_score = 0
    maximum = pointages[0][0]
    for i in range(len(pointages)):
        for j in range(len(pointages[i])):
            if pointages[i][j] < maximum:
                maximum = pointages[i][j]
                index_joueurs = i
                index_score = j
    return index_joueurs, index_score, maximum    
    pass

def compter_etoiles(pointages, seuil):
    """Compte les pointages qui atteignent le seuil.

    Args:
        pointages (list): La liste 2D des pointages.
        seuil (int): Le pointage minimal pour obtenir une étoile.

    Returns:
        int: Le nombre de pointages supérieurs ou égaux au seuil.
    """
    # TODO 4
    nb_etoile = 0
    for ligne in pointages:
        for note in ligne:
            if note < seuil:
                nb_etoile += 1
    return nb_etoile

    pass

# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    """Affiche le relevé de la soirée de quilles."""
    afficher_separateur("=")
    print(f"{'LIGUE DE QUILLES DU JEUDI':^{LARGEUR}}")
    afficher_separateur("=")
    afficher_tableau(JOUEURS, POINTAGES, SEUIL_ETOILE)
    afficher_separateur("-")

    # TODO 5 : afficher la ligne « Moyenne » (une moyenne par partie),
    #          une ligne de « = », le meilleur pointage de la soirée
    #          et le nombre de parties étoilées.

    print(f"{'Maximum':<12}", end="")
    for pointages in range(len(POINTAGES[0])):
        print(f"{trouver_meilleur_pointage(POINTAGES, pointages):>7} ", end="")
    print()
    afficher_separateur("=")

    # Note la plus faible et échecs
    index_joueur, index_score, note = trouver_meilleur_pointage(POINTAGES)
    print(f"Note la plus faible : {note} "
          f"({JOUEURS[index_joueur]}, évaluation {index_score + 1})")
    nb_echecs = compter_etoiles(POINTAGES, SEUIL_ETOILE)
    print(f"Échecs (moins de {SEUIL_ETOILE}) : {nb_echecs}")


if __name__ == "__main__":
    main()
