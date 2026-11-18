"""Fonctions utilitaires de saisie validée.

Module du Cours 07 : ces fonctions ne dépendent d'aucun programme en
particulier. Ce fichier est fourni tel quel et ne doit pas être modifié.
"""


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


# Tests rapides : exécutés seulement si on lance ce fichier directement,
# jamais lorsqu'il est importé par un autre fichier.
if __name__ == "__main__":
    print("Entier lu :", lire_entier("Nombre (1 à 10) : ", 1, 10))
    print("Réponse :", lire_oui_non("Continuer? (o/n) : "))
