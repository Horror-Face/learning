"""Bulletin de notes.

Saisit les notes de plusieurs cours pour un étudiant, calcule les moyennes,
puis affiche un bulletin avec la mention de chaque cours.

Exemple de révision qui réutilise les notions des cours 1 à 7.
"""

# ---------------------------------------------------------------------------
# Constantes (cours 2.3)
# ---------------------------------------------------------------------------
COURS = ("Programmation", "Mathématiques", "Français")   # tuple (5.3)
NB_NOTES = 3
NOTE_MAX = 100
NOTE_PASSAGE = 60
LARGEUR = 40


# ---------------------------------------------------------------------------
# Fonctions de saisie : while + drapeau + try/except (cours 5.1 à 5.3)
# ---------------------------------------------------------------------------
def lire_entier(message, minimum=0, maximum=99):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché à l'utilisateur.
        minimum (int, optional): La plus petite valeur acceptée. Par défaut 0.
        maximum (int, optional): La plus grande valeur acceptée. Par défaut 99.

    Returns:
        int: L'entier saisi, compris entre minimum et maximum.
    """
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return valeur


def lire_texte(message):
    """Demande un texte jusqu'à ce qu'il ne soit pas vide.

    Args:
        message (str): Le message affiché à l'utilisateur.

    Returns:
        str: Le texte saisi, sans espaces au début ni à la fin.
    """
    texte = input(message).strip()
    while texte == "":
        print("Erreur : la saisie ne peut pas être vide.")
        texte = input(message).strip()
    return texte


def lire_oui_non(message):
    """Pose une question fermée jusqu'à obtenir « o » ou « n ».

    Args:
        message (str): La question affichée à l'utilisateur.

    Returns:
        bool: True si l'utilisateur répond « o », False s'il répond « n ».
    """
    reponses_valides = ("o", "n")
    reponse = input(message).strip().lower()
    while reponse not in reponses_valides:
        print("Erreur : répondez par o ou n.")
        reponse = input(message).strip().lower()
    return reponse == "o"


def saisir_notes():
    """Demande les notes de chaque cours (boucles for imbriquées, cours 6.3).

    Returns:
        list: Une liste de listes : les notes de chaque cours, dans l'ordre
            de COURS.
    """
    notes = []
    for cours in COURS:
        print(f"\n{cours}")
        notes_cours = []
        for i in range(NB_NOTES):
            note = lire_entier(f"  Note {i + 1} sur {NOTE_MAX} : ", 0, NOTE_MAX)
            notes_cours.append(note)          # on construit la liste (6.2)
        notes.append(notes_cours)
    return notes


# ---------------------------------------------------------------------------
# Fonctions de calcul : elles renvoient une valeur (cours 7.4)
# ---------------------------------------------------------------------------
def calculer_moyenne(notes, decimales=1):
    """Calcule la moyenne d'une liste de nombres.

    Args:
        notes (list): Les nombres dont on veut la moyenne.
        decimales (int, optional): Le nombre de décimales. Par défaut 1.

    Returns:
        float: La moyenne, arrondie.
    """
    return round(sum(notes) / len(notes), decimales)


def calculer_moyennes(notes):
    """Calcule la moyenne de chaque cours.

    Args:
        notes (list): Les notes de chaque cours (liste de listes).

    Returns:
        list: La moyenne de chaque cours, dans le même ordre.
    """
    moyennes = []
    for notes_cours in notes:
        moyennes.append(calculer_moyenne(notes_cours))
    return moyennes


def determiner_mention(moyenne):
    """Détermine la mention associée à une moyenne (conditions enchaînées, 4.2).

    Args:
        moyenne (float): La moyenne du cours.

    Returns:
        str: La mention : Excellent, Très bien, Réussi ou Échec.
    """
    if moyenne >= 90:
        return "Excellent"
    elif moyenne >= 75:
        return "Très bien"
    elif moyenne >= NOTE_PASSAGE:
        return "Réussi"
    else:
        return "Échec"


def calculer_statistiques(moyennes):
    """Calcule la meilleure, la pire et la moyenne générale.

    Args:
        moyennes (list): La moyenne de chaque cours.

    Returns:
        tuple: La meilleure moyenne, la pire moyenne et la moyenne générale,
            dans cet ordre.
    """
    return max(moyennes), min(moyennes), calculer_moyenne(moyennes)


def compter_echecs(moyennes):
    """Compte les cours dont la moyenne est sous la note de passage.

    Args:
        moyennes (list): La moyenne de chaque cours.

    Returns:
        int: Le nombre de cours échoués.
    """
    nb_echecs = 0
    for moyenne in moyennes:
        if moyenne < NOTE_PASSAGE:
            nb_echecs += 1                    # affectation composée (2.5)
    return nb_echecs


# ---------------------------------------------------------------------------
# Fonctions d'affichage : elles affichent, sans rien renvoyer
# ---------------------------------------------------------------------------
def afficher_separateur(caractere):
    """Affiche une ligne de séparation de la largeur du bulletin.

    Args:
        caractere (str): Le caractère répété pour former la ligne.
    """
    print(caractere * LARGEUR)


def afficher_bulletin(nom, moyennes):
    """Affiche le bulletin d'un étudiant (f-strings alignées, cours 3.3).

    Args:
        nom (str): Le nom de l'étudiant.
        moyennes (list): La moyenne de chaque cours.
    """
    titre = f"Bulletin de {nom}"
    afficher_separateur("=")
    print(f"{titre:^{LARGEUR}}")
    afficher_separateur("=")

    for i in range(len(COURS)):
        mention = determiner_mention(moyennes[i])
        print(f"{COURS[i]:<18}{moyennes[i]:>6.1f} %   {mention}")
    afficher_separateur("-")

    meilleure, pire, generale = calculer_statistiques(moyennes)
    print(f"{'Meilleure moyenne':<18}{meilleure:>6.1f} %")
    print(f"{'Pire moyenne':<18}{pire:>6.1f} %")
    print(f"{'Moyenne générale':<18}{generale:>6.1f} %")
    afficher_separateur("-")

    nb_echecs = compter_echecs(moyennes)
    # Opérateur ternaire (cours 4.4)
    verdict = "Session réussie!" if nb_echecs == 0 else f"{nb_echecs} cours à reprendre"
    print(f"{verdict:^{LARGEUR}}")
    afficher_separateur("=")


# ---------------------------------------------------------------------------
# Programme principal (cours 7.8)
# ---------------------------------------------------------------------------
def main():
    """Produit le bulletin d'autant d'étudiants que l'utilisateur le souhaite."""
    continuer = True
    while continuer:
        nom = lire_texte("Nom de l'étudiant : ")
        notes = saisir_notes()
        moyennes = calculer_moyennes(notes)
        print()
        afficher_bulletin(nom, moyennes)
        continuer = lire_oui_non("\nAutre étudiant? (o/n) : ")
    print("Au revoir!")


if __name__ == "__main__":
    main()