"""Boîte à outils : fonctions prêtes à l'emploi pour les programmes du cours.

Regroupe des fonctions réutilisables (saisies validées, menus, affichage en
couleur, chaînes, listes, calculs, dates, fichiers texte, CSV et JSON) qui
reprennent les notions des cours 1 à 10 et les fiches « Outils ».

Utilisation :
    import boite_outils as bo
    choix = bo.choisir_dans_menu("MENU", ["Jouer", "Quitter"])

Dépendance : colorama  (pip install colorama)
Aucune fonction ne dépend d'une variable globale du programme appelant.
"""

import csv
import json
import math
import os
import random
from datetime import date, datetime

from colorama import Fore, Style, init

init(autoreset=True)

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
LARGEUR_DEFAUT = 78
FORMAT_DATE = "%Y-%m-%d"
ENCODAGE = "utf-8"
LETTRES_AVEC_ACCENT = "àâäéèêëîïôöùûüÿç"
LETTRES_SANS_ACCENT = "aaaeeeeiioouuuyc"


# ===========================================================================
# 1. AFFICHAGE ET COULEURS  (fiches 3.2, 3.3 et colorama)
# ===========================================================================
def afficher_erreur(message):
    """Affiche un message d'erreur en rouge.

    Args:
        message (str): Le texte à afficher.
    """
    print(Fore.RED + message)


def afficher_succes(message):
    """Affiche un message de succès en vert.

    Args:
        message (str): Le texte à afficher.
    """
    print(Fore.GREEN + message)


def afficher_avertissement(message):
    """Affiche un avertissement en jaune.

    Args:
        message (str): Le texte à afficher.
    """
    print(Fore.YELLOW + message)


def afficher_info(message):
    """Affiche une information en cyan.

    Args:
        message (str): Le texte à afficher.
    """
    print(Fore.CYAN + message)


def afficher_separateur(caractere="-", largeur=LARGEUR_DEFAUT):
    """Affiche une ligne de séparation.

    Args:
        caractere (str, optional): Le caractère répété. Par défaut "-".
        largeur (int, optional): La longueur de la ligne. Par défaut 78.
    """
    print(caractere * largeur)


def afficher_titre(titre, caractere="=", largeur=LARGEUR_DEFAUT):
    """Affiche un titre centré entre deux lignes de séparation.

    Args:
        titre (str): Le titre à afficher.
        caractere (str, optional): Le caractère des lignes. Par défaut "=".
        largeur (int, optional): La largeur totale. Par défaut 78.
    """
    afficher_separateur(caractere, largeur)
    print(f"{titre:^{largeur}}")
    afficher_separateur(caractere, largeur)


def afficher_banniere(lignes, largeur=LARGEUR_DEFAUT):
    """Affiche une bannière encadrée contenant des lignes de texte centrées.

    Args:
        lignes (list): Les lignes de texte à centrer.
        largeur (int, optional): La largeur totale du cadre. Par défaut 78.
    """
    interieur = largeur - 2
    print("/" + "-" * interieur + "\\")
    for ligne in lignes:
        print("|" + f"{ligne:^{interieur}}" + "|")
    print("\\" + "-" * interieur + "/")


def afficher_tableau(entetes, lignes, largeurs=None):
    """Affiche un tableau aligné à gauche avec une ligne d'en-têtes.

    Args:
        entetes (list): Les titres des colonnes.
        lignes (list): Une liste de listes : les valeurs de chaque ligne.
        largeurs (list, optional): La largeur de chaque colonne. Par défaut,
            calculée selon le contenu le plus long de chaque colonne.
    """
    if largeurs is None:
        largeurs = []
        for col in range(len(entetes)):
            plus_long = len(str(entetes[col]))
            for ligne in lignes:
                plus_long = max(plus_long, len(str(ligne[col])))
            largeurs.append(plus_long)

    texte = ""
    for col in range(len(entetes)):
        texte += f"{str(entetes[col]):<{largeurs[col]}} | "
    print(texte.rstrip(" |"))
    afficher_separateur("-", sum(largeurs) + 3 * (len(largeurs) - 1))
    for ligne in lignes:
        texte = ""
        for col in range(len(entetes)):
            texte += f"{str(ligne[col]):<{largeurs[col]}} | "
        print(texte.rstrip(" |"))


def afficher_liste_numerotee(elements, depart=1):
    """Affiche les éléments d'une liste, numérotés.

    Args:
        elements (list): Les éléments à afficher.
        depart (int, optional): Le premier numéro. Par défaut 1.
    """
    for i in range(len(elements)):
        print(f"{i + depart}. {elements[i]}")


def afficher_matrice(matrice, largeur_cellule=4):
    """Affiche une liste 2D (lignes et colonnes alignées).

    Args:
        matrice (list): Une liste de listes de valeurs.
        largeur_cellule (int, optional): La largeur de chaque cellule. Par défaut 4.
    """
    for ligne in matrice:
        texte = ""
        for valeur in ligne:
            texte += f"{str(valeur):>{largeur_cellule}}"
        print(texte)


def afficher_barre_progression(valeur, maximum, largeur=30):
    """Affiche une barre de progression en pourcentage.

    Args:
        valeur (int): La valeur actuelle.
        maximum (int): La valeur qui représente 100 %.
        largeur (int, optional): Le nombre de caractères de la barre. Par défaut 30.
    """
    proportion = valeur / maximum if maximum > 0 else 0
    pleins = round(proportion * largeur)
    print(f"[{'#' * pleins}{'.' * (largeur - pleins)}] {round(proportion * 100)} %")


def pause(message="Appuyez sur Entrée pour continuer..."):
    """Attend que l'utilisateur appuie sur Entrée.

    Args:
        message (str, optional): Le message affiché.
    """
    input(message)


# ===========================================================================
# 2. SAISIES VALIDÉES  (cours 5)
# ===========================================================================
def lire_texte(message, longueur_max=None):
    """Demande un texte non vide (au moins un caractère visible).

    Args:
        message (str): Le message affiché.
        longueur_max (int, optional): La longueur maximale permise. Par défaut aucune.

    Returns:
        str: Le texte saisi, sans espaces au début ni à la fin.
    """
    texte = ""
    valide = False
    while not valide:
        texte = input(message).strip()
        if texte == "":
            afficher_erreur("Erreur : la réponse ne peut pas être vide.")
        elif longueur_max is not None and len(texte) > longueur_max:
            afficher_erreur(f"Erreur : {longueur_max} caractères maximum.")
        else:
            valide = True
    return texte


def lire_entier(message, minimum=0, maximum=99):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché.
        minimum (int, optional): La plus petite valeur acceptée. Par défaut 0.
        maximum (int, optional): La plus grande valeur acceptée. Par défaut 99.

    Returns:
        int: L'entier saisi, compris entre minimum et maximum.
    """
    valeur = 0
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                afficher_erreur(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            afficher_erreur("Erreur : ce n'est pas un nombre entier.")
    return valeur


def lire_reel(message, minimum=0.0, maximum=1_000_000.0):
    """Demande un nombre réel (la virgule est acceptée) jusqu'à saisie valide.

    Args:
        message (str): Le message affiché.
        minimum (float, optional): La plus petite valeur acceptée. Par défaut 0.0.
        maximum (float, optional): La plus grande valeur acceptée. Par défaut 1 000 000.

    Returns:
        float: Le réel saisi, compris entre minimum et maximum.
    """
    valeur = 0.0
    valide = False
    while not valide:
        try:
            valeur = float(input(message).replace(",", "."))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                afficher_erreur(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            afficher_erreur("Erreur : ce n'est pas un nombre.")
    return valeur


def lire_oui_non(message):
    """Demande une réponse « o » ou « n » (« oui » et « non » sont acceptés).

    Args:
        message (str): Le message affiché.

    Returns:
        bool: True pour oui, False pour non.
    """
    reponse = ""
    while reponse not in ("o", "n", "oui", "non"):
        reponse = input(message).strip().lower()
        if reponse not in ("o", "n", "oui", "non"):
            afficher_erreur("Erreur : répondez par o ou n.")
    return reponse in ("o", "oui")


def lire_choix_dans_liste(message, choix_permis):
    """Demande une réponse qui doit faire partie d'une liste (sans tenir
    compte des majuscules, des accents ni des espaces autour).

    Args:
        message (str): Le message affiché.
        choix_permis (list): Les réponses acceptées.

    Returns:
        str: La réponse correspondante, telle qu'écrite dans choix_permis.
    """
    trouve = None
    while trouve is None:
        reponse = normaliser(input(message))
        for choix in choix_permis:
            if normaliser(choix) == reponse:
                trouve = choix
        if trouve is None:
            afficher_erreur("Erreur : choix invalide (" + ", ".join(choix_permis) + ").")
    return trouve


def lire_date(message, format_date=FORMAT_DATE):
    """Demande une date jusqu'à ce qu'elle soit valide.

    Args:
        message (str): Le message affiché.
        format_date (str, optional): Le format attendu. Par défaut AAAA-MM-JJ.

    Returns:
        datetime.date: La date saisie.
    """
    resultat = None
    while resultat is None:
        resultat = convertir_en_date(input(message).strip(), format_date)
        if resultat is None:
            afficher_erreur("Erreur : date invalide (exemple : 2026-11-17).")
    return resultat


# ===========================================================================
# 3. MENUS  (cours 6 et 7)
# ===========================================================================
def afficher_menu(titre, options, option_quitter=None):
    """Affiche un menu numéroté à partir de 1.

    Args:
        titre (str): Le titre du menu.
        options (list): Les textes des options.
        option_quitter (str, optional): Le texte d'une option 0 (ex. « Quitter »).
    """
    afficher_titre(titre)
    afficher_liste_numerotee(options)
    if option_quitter is not None:
        print(f"0. {option_quitter}")


def choisir_dans_menu(titre, options, option_quitter=None, message="Votre choix : "):
    """Affiche un menu puis lit un choix valide.

    Args:
        titre (str): Le titre du menu.
        options (list): Les textes des options.
        option_quitter (str, optional): Le texte de l'option 0. Par défaut aucune.
        message (str, optional): L'invite de saisie.

    Returns:
        int: Le numéro choisi (0 si l'option « quitter » est choisie).
    """
    afficher_menu(titre, options, option_quitter)
    minimum = 0 if option_quitter is not None else 1
    return lire_entier(message, minimum, len(options))


def construire_options_avec_valeurs(noms, valeurs, suffixe="", gabarit="{nom} ({valeur} {suffixe})"):
    """Construit les textes d'un menu à partir de deux listes associées.

    Exemple : ["Facile", "Normal"] et [5, 10] avec suffixe "questions"
    donnent ["Facile (5 questions)", "Normal (10 questions)"].

    Args:
        noms (list): Les noms des options.
        valeurs (list): Les valeurs associées, dans le même ordre.
        suffixe (str, optional): Un mot placé après la valeur.
        gabarit (str, optional): Le gabarit, avec {nom}, {valeur} et {suffixe}.

    Returns:
        list: Les textes des options.
    """
    options = []
    for i in range(len(noms)):
        options.append(gabarit.format(nom=noms[i], valeur=valeurs[i], suffixe=suffixe).replace(" )", ")"))
    return options


def executer_menu(titre, actions, option_quitter="Quitter"):
    """Boucle de menu : affiche, lit un choix et appelle la fonction associée,
    jusqu'à ce que l'utilisateur choisisse de quitter.

    Args:
        titre (str): Le titre du menu.
        actions (dict): Associe le texte de chaque option à une fonction sans
            paramètre à appeler quand l'option est choisie.
        option_quitter (str, optional): Le texte de l'option 0. Par défaut « Quitter ».
    """
    noms = list(actions.keys())
    choix = choisir_dans_menu(titre, noms, option_quitter)
    while choix != 0:
        actions[noms[choix - 1]]()
        print()
        choix = choisir_dans_menu(titre, noms, option_quitter)


# ===========================================================================
# 4. CHAÎNES DE CARACTÈRES  (fiche « Manipulations de chaînes »)
# ===========================================================================
def normaliser(texte):
    """Prépare un texte pour une comparaison souple.

    Retire les espaces autour, met en minuscules, enlève les accents et
    remplace les traits d'union par des espaces.

    Args:
        texte (str): Le texte à normaliser.

    Returns:
        str: Le texte normalisé.
    """
    resultat = texte.strip().lower().replace("-", " ")
    for i in range(len(LETTRES_AVEC_ACCENT)):
        resultat = resultat.replace(LETTRES_AVEC_ACCENT[i], LETTRES_SANS_ACCENT[i])
    return resultat


def est_vide(texte):
    """Indique si un texte est vide ou ne contient que des espaces.

    Args:
        texte (str): Le texte à vérifier.

    Returns:
        bool: True si aucun caractère visible.
    """
    return texte.strip() == ""


def capitaliser_mots(texte):
    """Met la première lettre de chaque mot en majuscule.

    Args:
        texte (str): Le texte à transformer.

    Returns:
        str: Le texte avec chaque mot capitalisé.
    """
    mots = texte.strip().split()
    resultat = []
    for mot in mots:
        resultat.append(mot[0].upper() + mot[1:].lower())
    return " ".join(resultat)


def tronquer(texte, longueur, suffixe="..."):
    """Coupe un texte trop long et ajoute un suffixe.

    Args:
        texte (str): Le texte à tronquer.
        longueur (int): La longueur maximale du résultat.
        suffixe (str, optional): Ce qu'on ajoute à la fin. Par défaut "...".

    Returns:
        str: Le texte, d'au plus longueur caractères.
    """
    if len(texte) <= longueur:
        return texte
    return texte[:longueur - len(suffixe)] + suffixe


def compter_mots(texte):
    """Compte les mots d'un texte.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        int: Le nombre de mots.
    """
    return len(texte.split())


def est_palindrome(texte):
    """Indique si un texte se lit pareil dans les deux sens (sans accents,
    majuscules ni espaces).

    Args:
        texte (str): Le texte à vérifier.

    Returns:
        bool: True si c'est un palindrome.
    """
    propre = normaliser(texte).replace(" ", "")
    return propre == propre[::-1]


def compter_voyelles(texte):
    """Compte les voyelles d'un texte (accents ignorés).

    Args:
        texte (str): Le texte à analyser.

    Returns:
        int: Le nombre de voyelles.
    """
    total = 0
    for lettre in normaliser(texte):
        if lettre in "aeiouy":
            total += 1
    return total


def formater_argent(montant):
    """Formate un montant en dollars, à la québécoise (ex. 1 234,50 $).

    Args:
        montant (float): Le montant.

    Returns:
        str: Le montant formaté.
    """
    texte = f"{montant:,.2f}".replace(",", " ").replace(".", ",")
    return texte + " $"


# ===========================================================================
# 5. LISTES ET STATISTIQUES  (cours 6)
# ===========================================================================
def somme_liste(nombres):
    """Additionne les nombres d'une liste avec une boucle for.

    Args:
        nombres (list): Les nombres à additionner.

    Returns:
        float: La somme (0 si la liste est vide).
    """
    total = 0
    for nombre in nombres:
        total += nombre
    return total


def moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres.

    Args:
        nombres (list): Les nombres (liste non vide).

    Returns:
        float: La moyenne, ou 0.0 si la liste est vide.
    """
    if len(nombres) == 0:
        return 0.0
    return somme_liste(nombres) / len(nombres)


def mediane(nombres):
    """Calcule la médiane d'une liste de nombres (la liste n'est pas modifiée).

    Args:
        nombres (list): Les nombres (liste non vide).

    Returns:
        float: La médiane, ou 0.0 si la liste est vide.
    """
    if len(nombres) == 0:
        return 0.0
    triee = sorted(nombres)
    milieu = len(triee) // 2
    if len(triee) % 2 == 1:
        return triee[milieu]
    return (triee[milieu - 1] + triee[milieu]) / 2


def index_du_maximum(nombres):
    """Trouve l'index du plus grand nombre (le premier en cas d'égalité).

    Args:
        nombres (list): Les nombres (liste non vide).

    Returns:
        int: L'index du maximum, ou -1 si la liste est vide.
    """
    meilleur = -1
    for i in range(len(nombres)):
        if meilleur == -1 or nombres[i] > nombres[meilleur]:
            meilleur = i
    return meilleur


def index_du_minimum(nombres):
    """Trouve l'index du plus petit nombre (le premier en cas d'égalité).

    Args:
        nombres (list): Les nombres (liste non vide).

    Returns:
        int: L'index du minimum, ou -1 si la liste est vide.
    """
    plus_petit = -1
    for i in range(len(nombres)):
        if plus_petit == -1 or nombres[i] < nombres[plus_petit]:
            plus_petit = i
    return plus_petit


def sans_doublons(elements):
    """Retire les doublons d'une liste en gardant l'ordre d'apparition.

    Args:
        elements (list): La liste d'origine (non modifiée).

    Returns:
        list: Une nouvelle liste sans doublons.
    """
    resultat = []
    for element in elements:
        if element not in resultat:
            resultat.append(element)
    return resultat


def inverser_liste(elements):
    """Renvoie une copie de la liste à l'envers.

    Args:
        elements (list): La liste d'origine (non modifiée).

    Returns:
        list: Une nouvelle liste inversée.
    """
    return elements[::-1]


def decouper_en_morceaux(elements, taille):
    """Découpe une liste en sous-listes de taille donnée (liste 2D).

    Args:
        elements (list): La liste à découper.
        taille (int): Le nombre d'éléments par morceau.

    Returns:
        list: Une liste de sous-listes.
    """
    morceaux = []
    for debut in range(0, len(elements), taille):
        morceaux.append(elements[debut:debut + taille])
    return morceaux


def creer_matrice(nb_lignes, nb_colonnes, valeur=0):
    """Crée une liste 2D remplie d'une valeur (chaque ligne est indépendante).

    Args:
        nb_lignes (int): Le nombre de lignes.
        nb_colonnes (int): Le nombre de colonnes.
        valeur (optional): La valeur initiale. Par défaut 0.

    Returns:
        list: La matrice.
    """
    matrice = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice


# ===========================================================================
# 6. ALÉATOIRE  (fiche « random »)
# ===========================================================================
def tirer_sans_repetition(elements, nombre):
    """Tire des éléments au hasard sans répétition (random.sample).

    Args:
        elements (list): La liste où piocher.
        nombre (int): Le nombre d'éléments à tirer.

    Returns:
        list: Les éléments tirés.
    """
    return random.sample(elements, nombre)


def tirer_index_sans_repetition(taille, nombre):
    """Tire des index au hasard sans répétition.

    Args:
        taille (int): La taille de la liste (les index vont de 0 à taille - 1).
        nombre (int): Le nombre d'index à tirer.

    Returns:
        list: Les index tirés.
    """
    return random.sample(range(taille), nombre)


def element_au_hasard(elements):
    """Choisit un élément au hasard.

    Args:
        elements (list): La liste (non vide).

    Returns:
        L'élément choisi.
    """
    return random.choice(elements)


def melanger_copie(elements):
    """Renvoie une copie mélangée de la liste (l'originale reste intacte).

    Args:
        elements (list): La liste d'origine.

    Returns:
        list: Une nouvelle liste mélangée.
    """
    copie = elements.copy()
    random.shuffle(copie)
    return copie


def lancer_des(nombre_des=1, faces=6):
    """Lance des dés.

    Args:
        nombre_des (int, optional): Le nombre de dés. Par défaut 1.
        faces (int, optional): Le nombre de faces. Par défaut 6.

    Returns:
        list: Le résultat de chaque dé.
    """
    resultats = []
    for _ in range(nombre_des):
        resultats.append(random.randint(1, faces))
    return resultats


def generer_mot_de_passe(longueur=12):
    """Génère un mot de passe aléatoire (lettres, chiffres et symboles).

    Args:
        longueur (int, optional): La longueur voulue. Par défaut 12.

    Returns:
        str: Le mot de passe.
    """
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?#$%&*"
    mot_de_passe = ""
    for _ in range(longueur):
        mot_de_passe += random.choice(caracteres)
    return mot_de_passe


# ===========================================================================
# 7. MATHÉMATIQUES  (cours 2 et fiche « math »)
# ===========================================================================
def calculer_pourcentage(partie, total, decimales=0):
    """Calcule un pourcentage.

    Args:
        partie (float): La partie.
        total (float): Le total.
        decimales (int, optional): Le nombre de décimales. Par défaut 0.

    Returns:
        float: Le pourcentage (0 si le total est 0).
    """
    if total == 0:
        return 0
    resultat = round(partie / total * 100, decimales)
    return int(resultat) if decimales == 0 else resultat


def est_pair(nombre):
    """Indique si un entier est pair.

    Args:
        nombre (int): L'entier à vérifier.

    Returns:
        bool: True si pair.
    """
    return nombre % 2 == 0


def est_premier(nombre):
    """Indique si un entier est premier.

    Args:
        nombre (int): L'entier à vérifier.

    Returns:
        bool: True si premier.
    """
    if nombre < 2:
        return False
    for diviseur in range(2, math.isqrt(nombre) + 1):
        if nombre % diviseur == 0:
            return False
    return True


def factorielle(nombre):
    """Calcule la factorielle d'un entier positif.

    Args:
        nombre (int): L'entier (0 ou plus).

    Returns:
        int: nombre!
    """
    resultat = 1
    for i in range(2, nombre + 1):
        resultat *= i
    return resultat


def pgcd(a, b):
    """Calcule le plus grand commun diviseur de deux entiers.

    Args:
        a (int): Le premier entier.
        b (int): Le deuxième entier.

    Returns:
        int: Le PGCD.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def limiter(valeur, minimum, maximum):
    """Force une valeur à rester entre un minimum et un maximum.

    Args:
        valeur (float): La valeur à limiter.
        minimum (float): La borne inférieure.
        maximum (float): La borne supérieure.

    Returns:
        float: La valeur limitée.
    """
    return max(minimum, min(valeur, maximum))


def convertir_celsius_en_fahrenheit(celsius):
    """Convertit des degrés Celsius en Fahrenheit.

    Args:
        celsius (float): La température en °C.

    Returns:
        float: La température en °F.
    """
    return celsius * 9 / 5 + 32


def calculer_taxes(montant, taux_tps=0.05, taux_tvq=0.09975):
    """Calcule la TPS et la TVQ sur un montant, arrondies au cent.

    Args:
        montant (float): Le montant avant taxes.
        taux_tps (float, optional): Le taux de la TPS. Par défaut 0.05.
        taux_tvq (float, optional): Le taux de la TVQ. Par défaut 0.09975.

    Returns:
        tuple: (tps, tvq).
    """
    return round(montant * taux_tps, 2), round(montant * taux_tvq, 2)


# ===========================================================================
# 8. DATES ET HEURES  (fiche « datetime »)
# ===========================================================================
def date_du_jour():
    """Renvoie la date d'aujourd'hui.

    Returns:
        datetime.date: La date du jour.
    """
    return date.today()


def formater_date(une_date, format_date=FORMAT_DATE):
    """Convertit une date en texte.

    Args:
        une_date (datetime.date): La date à formater.
        format_date (str, optional): Le format. Par défaut AAAA-MM-JJ.

    Returns:
        str: La date en texte.
    """
    return une_date.strftime(format_date)


def convertir_en_date(texte, format_date=FORMAT_DATE):
    """Convertit un texte en date.

    Args:
        texte (str): Le texte à convertir.
        format_date (str, optional): Le format attendu. Par défaut AAAA-MM-JJ.

    Returns:
        datetime.date: La date, ou None si le texte est invalide.
    """
    try:
        return datetime.strptime(texte, format_date).date()
    except ValueError:
        return None


def jours_entre(date_debut, date_fin):
    """Compte les jours entre deux dates.

    Args:
        date_debut (datetime.date): La première date.
        date_fin (datetime.date): La deuxième date.

    Returns:
        int: Le nombre de jours (négatif si date_fin précède date_debut).
    """
    return (date_fin - date_debut).days


def calculer_age(date_naissance, aujourd_hui=None):
    """Calcule un âge en années complètes.

    Args:
        date_naissance (datetime.date): La date de naissance.
        aujourd_hui (datetime.date, optional): La date de référence. Par défaut aujourd'hui.

    Returns:
        int: L'âge en années.
    """
    if aujourd_hui is None:
        aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    return age


def heure_actuelle(format_heure="%H:%M:%S"):
    """Renvoie l'heure actuelle en texte.

    Args:
        format_heure (str, optional): Le format. Par défaut HH:MM:SS.

    Returns:
        str: L'heure.
    """
    return datetime.now().strftime(format_heure)


# ===========================================================================
# 9. FICHIERS TEXTE  (cours 8)
# ===========================================================================
def fichier_existe(chemin):
    """Indique si un fichier existe.

    Args:
        chemin (str): Le chemin du fichier.

    Returns:
        bool: True si le fichier existe.
    """
    return os.path.isfile(chemin)


def lire_lignes(chemin):
    """Lit un fichier texte et renvoie ses lignes sans le saut de ligne.

    Args:
        chemin (str): Le chemin du fichier.

    Returns:
        list: Les lignes du fichier, ou une liste vide si le fichier n'existe pas.
    """
    lignes = []
    if fichier_existe(chemin):
        with open(chemin, "r", encoding=ENCODAGE) as fichier:
            for ligne in fichier:
                lignes.append(ligne.rstrip("\n"))
    return lignes


def ecrire_lignes(chemin, lignes):
    """Écrit des lignes dans un fichier texte (remplace le contenu).

    Args:
        chemin (str): Le chemin du fichier.
        lignes (list): Les lignes à écrire.
    """
    with open(chemin, "w", encoding=ENCODAGE) as fichier:
        for ligne in lignes:
            fichier.write(str(ligne) + "\n")


def ajouter_ligne(chemin, ligne):
    """Ajoute une ligne à la fin d'un fichier texte (le crée au besoin).

    Args:
        chemin (str): Le chemin du fichier.
        ligne (str): La ligne à ajouter.
    """
    with open(chemin, "a", encoding=ENCODAGE) as fichier:
        fichier.write(str(ligne) + "\n")


def sauvegarder_liste(chemin, elements):
    """Sauvegarde une liste, un élément par ligne.

    Args:
        chemin (str): Le chemin du fichier.
        elements (list): La liste à sauvegarder.
    """
    ecrire_lignes(chemin, elements)


def charger_liste_entiers(chemin):
    """Recharge une liste d'entiers sauvegardée un par ligne.

    Args:
        chemin (str): Le chemin du fichier.

    Returns:
        list: Les entiers lus (les lignes invalides sont ignorées).
    """
    nombres = []
    for ligne in lire_lignes(chemin):
        try:
            nombres.append(int(ligne))
        except ValueError:
            pass
    return nombres


def compter_lignes(chemin):
    """Compte les lignes d'un fichier texte.

    Args:
        chemin (str): Le chemin du fichier.

    Returns:
        int: Le nombre de lignes.
    """
    return len(lire_lignes(chemin))


# ===========================================================================
# 10. CSV  (fiche 8.6 et module csv)
# ===========================================================================
def lire_csv(chemin, separateur=","):
    """Lit un fichier CSV (la première ligne est l'en-tête) avec le module csv.

    Args:
        chemin (str): Le chemin du fichier.
        separateur (str, optional): Le séparateur de colonnes. Par défaut ",".

    Returns:
        tuple: (entetes, lignes) : une liste de titres et une liste de listes.
            Renvoie ([], []) si le fichier n'existe pas.
    """
    entetes = []
    lignes = []
    if fichier_existe(chemin):
        with open(chemin, "r", encoding=ENCODAGE, newline="") as fichier:
            lecteur = csv.reader(fichier, delimiter=separateur)
            for numero, ligne in enumerate(lecteur):
                if numero == 0:
                    entetes = ligne
                else:
                    lignes.append(ligne)
    return entetes, lignes


def ecrire_csv(chemin, entetes, lignes, separateur=","):
    """Écrit un fichier CSV avec le module csv.

    Args:
        chemin (str): Le chemin du fichier.
        entetes (list): Les titres des colonnes.
        lignes (list): Une liste de listes de valeurs.
        separateur (str, optional): Le séparateur de colonnes. Par défaut ",".
    """
    with open(chemin, "w", encoding=ENCODAGE, newline="") as fichier:
        ecrivain = csv.writer(fichier, delimiter=separateur)
        ecrivain.writerow(entetes)
        ecrivain.writerows(lignes)


def csv_en_dictionnaires(entetes, lignes):
    """Transforme des lignes CSV en liste de dictionnaires.

    Args:
        entetes (list): Les titres des colonnes (clés).
        lignes (list): Les lignes lues.

    Returns:
        list: Un dictionnaire par ligne.
    """
    resultat = []
    for ligne in lignes:
        enregistrement = {}
        for i in range(len(entetes)):
            enregistrement[entetes[i]] = ligne[i]
        resultat.append(enregistrement)
    return resultat


# ===========================================================================
# 11. DICTIONNAIRES ET JSON  (cours 9)
# ===========================================================================
def compter_occurrences(elements):
    """Compte combien de fois chaque élément apparaît.

    Args:
        elements (list): Les éléments à compter.

    Returns:
        dict: Associe chaque élément à son nombre d'occurrences.
    """
    compteur = {}
    for element in elements:
        compteur[element] = compteur.get(element, 0) + 1
    return compteur


def inverser_dictionnaire(dictionnaire):
    """Échange les clés et les valeurs d'un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire d'origine (valeurs uniques).

    Returns:
        dict: Le dictionnaire inversé.
    """
    inverse = {}
    for cle, valeur in dictionnaire.items():
        inverse[valeur] = cle
    return inverse


def trier_dictionnaire_par_valeur(dictionnaire, decroissant=True):
    """Trie un dictionnaire selon ses valeurs.

    Args:
        dictionnaire (dict): Le dictionnaire à trier.
        decroissant (bool, optional): True pour du plus grand au plus petit.

    Returns:
        list: Une liste de tuples (clé, valeur) triée.
    """
    return sorted(dictionnaire.items(), key=lambda paire: paire[1], reverse=decroissant)


def sauvegarder_json(chemin, donnees):
    """Sauvegarde des données (liste, dictionnaire...) dans un fichier JSON.

    Args:
        chemin (str): Le chemin du fichier.
        donnees: Les données à sauvegarder.
    """
    with open(chemin, "w", encoding=ENCODAGE) as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)


def charger_json(chemin, valeur_par_defaut=None):
    """Charge des données depuis un fichier JSON.

    Args:
        chemin (str): Le chemin du fichier.
        valeur_par_defaut (optional): Renvoyée si le fichier est absent ou invalide.

    Returns:
        Les données lues, ou valeur_par_defaut.
    """
    if not fichier_existe(chemin):
        return valeur_par_defaut
    try:
        with open(chemin, "r", encoding=ENCODAGE) as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        return valeur_par_defaut


def charger_parametres(chemin, parametres_par_defaut):
    """Charge les paramètres d'une application en complétant avec les valeurs
    par défaut pour toute clé manquante.

    Args:
        chemin (str): Le chemin du fichier JSON.
        parametres_par_defaut (dict): Les paramètres par défaut.

    Returns:
        dict: Les paramètres complets.
    """
    parametres = parametres_par_defaut.copy()
    lus = charger_json(chemin, {})
    if isinstance(lus, dict):
        parametres.update(lus)
    return parametres


# ===========================================================================
# Démonstration : exécutée seulement si on lance ce fichier directement
# ===========================================================================
def demo_saisies():
    """Démontre les saisies validées."""
    nom = lire_texte("Nom : ")
    age = lire_entier("Âge (0 à 120) : ", 0, 120)
    afficher_succes(f"Bonjour {capitaliser_mots(nom)}, {age} ans!")


def demo_statistiques():
    """Démontre les fonctions de listes sur 10 nombres aléatoires."""
    nombres = [random.randint(1, 100) for _ in range(10)]
    print("Nombres :", nombres)
    print(f"Moyenne : {moyenne(nombres):.1f} | Médiane : {mediane(nombres)}")
    print("Plus grand à l'index", index_du_maximum(nombres))


def demo_date():
    """Démontre les fonctions de dates."""
    naissance = lire_date("Date de naissance (AAAA-MM-JJ) : ")
    afficher_info(f"Vous avez {calculer_age(naissance)} ans "
                  f"({jours_entre(naissance, date_du_jour())} jours).")


def demo_tableau():
    """Démontre l'affichage d'un tableau."""
    afficher_tableau(["Produit", "Prix"],
                     [["Café", formater_argent(2.25)], ["Muffin", formater_argent(3.5)]])


if __name__ == "__main__":
    afficher_banniere(["Boîte à outils", "Démonstration"])
    executer_menu("DÉMO", {
        "Saisies validées": demo_saisies,
        "Statistiques": demo_statistiques,
        "Dates": demo_date,
        "Tableau": demo_tableau,
    })
    print("À la prochaine!")