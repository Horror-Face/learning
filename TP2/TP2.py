# import random
# from donnees_tp2 import PAYS, CAPITALES_PAYS
# import utilitaires

#CONSTANTE
#############
#Jeu
import random

from colorama import Fore, init

import utilitaires
# ATTENTION : adapter les noms ci-dessous à ceux du fichier donnees_tp2.py fourni
from donnees_tp2 import (PAYS, CAPITALES_PAYS,
                         PROVINCES, CAPITALES_PROVINCES,
                         ETATS, CAPITALES_ETATS)

init(autoreset=True)

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
TITRE = "Jeu des capitales - Édition 2026"
AUTEUR = "Raphaël Desjardins"
GRAINE = None
LARGEUR = 78
MODES = ["Standard", "Aventure"]
DETAILS_MODES = ["{} pays du monde",
                 "{} lieux : pays + provinces et territoires du Canada + États américains"]
NIVEAUX = ["Facile", "Normal", "Avancé"]
NB_QUESTIONS_NIVEAUX = [5, 10, 15]
LONGUEUR_REPONSE_REVISION = 15


# ---------------------------------------------------------------------------
# Affichage
# ---------------------------------------------------------------------------
def afficher_bienvenue():
    """Affiche la bannière du programme avec le nom des auteurs."""
    interieur = LARGEUR - 2
    print("/" + "-" * interieur + "\\")
    print("|" + f"{TITRE:^{interieur}}" + "|")
    print("|" + f"{'réalisé par ' + AUTEUR:^{interieur}}" + "|")
    print("\\" + "-" * interieur + "/")


def afficher_menu(titre, options):
    """Affiche un titre, puis chaque option numérotée à partir de 1.

    Args:
        titre (str): Le titre du menu.
        options (list): Les textes des options, dans l'ordre.
    """
    print(titre)
    for i in range(len(options)):
        print(f"  {i + 1} - {options[i]}")


# ---------------------------------------------------------------------------
# Logique du jeu
# ---------------------------------------------------------------------------
def construire_listes(mode):
    if mode == 1:
        lieux = PAYS.copy()
        capitales = CAPITALES_PAYS.copy()
    else:
        lieux = PAYS + PROVINCES + ETATS
        capitales = CAPITALES_PAYS + CAPITALES_PROVINCES + CAPITALES_ETATS
    return lieux, capitales


def est_bonne_reponse(reponse, capitale):
    bonne = False
    for acceptee in capitale.split("/"):
        if utilitaires.normaliser(reponse) == utilitaires.normaliser(acceptee):
            bonne = True
    return bonne


def calculer_pourcentage(nb_bonnes, nb_questions):
    return round(nb_bonnes / nb_questions * 100)


def obtenir_appreciation(pourcentage):
    if pourcentage == 100:
        message = "Parfait! Un vrai globe-trotter!"
    elif pourcentage >= 80:
        message = "Excellent!"
    elif pourcentage >= 60:
        message = "Bon travail!"
    elif pourcentage >= 40:
        message = "Pas mal, mais l'atlas pourrait vous aider."
    else:
        message = "Il est temps de sortir l'atlas!"
    return message


def afficher_revision(lieux_rates, reponses_donnees, capitales_rates):
    print(f"{'À RÉVISER':^{LARGEUR}}")
    print("-" * LARGEUR)
    if len(lieux_rates) == 0:
        print(Fore.GREEN + "Aucune erreur : rien à réviser!")
    else:
        print(f"{'Lieu':<32}| {'Votre réponse':<15} | {'Bonne réponse':<25}")
        print("-" * LARGEUR)
        for i in range(len(lieux_rates)):
            reponse = reponses_donnees[i][:LONGUEUR_REPONSE_REVISION]
            officielle = capitales_rates[i].split("/")[0]
            print(f"{lieux_rates[i]:<32}| {reponse:<15} | {officielle:<25}")
    print("-" * LARGEUR)


def jouer_partie(lieux, capitales, nb_questions, nom):
    nb_bonnes = 0
    lieux_rates = []
    reponses_donnees = []
    capitales_rates = []

    indexes = random.sample(range(len(lieux)), nb_questions)
    for numero in range(nb_questions):
        index = indexes[numero]
        print()
        print(f"Question {numero + 1} de {nb_questions} — {lieux[index]}")
        reponse = utilitaires.lire_texte("Capitale : ")
        if est_bonne_reponse(reponse, capitales[index]):
            nb_bonnes += 1
            print(Fore.GREEN + f"Bonne réponse! Pointage : {nb_bonnes}/{numero + 1}")
        else:
            attendues = " ou ".join(capitales[index].split("/"))
            print(Fore.RED + f"Mauvaise réponse. On cherchait : {attendues}. "
                  f"Pointage : {nb_bonnes}/{numero + 1}")
            lieux_rates.append(lieux[index])
            reponses_donnees.append(reponse)
            capitales_rates.append(capitales[index])

    pourcentage = calculer_pourcentage(nb_bonnes, nb_questions)
    print()
    print("*" * LARGEUR)
    print(f"{nom}, votre pointage est de {nb_bonnes} sur {nb_questions} ({pourcentage} %).")
    print(obtenir_appreciation(pourcentage))
    print("*" * LARGEUR)
    print()
    afficher_revision(lieux_rates, reponses_donnees, capitales_rates)
    return nb_bonnes


def afficher_historique(nom, modes_joues, niveaux_joues, resultats, totaux):
    print("=" * LARGEUR)
    print(f"{'HISTORIQUE DE LA SESSION':^{LARGEUR}}")
    print("=" * LARGEUR)
    print("Partie | Mode     | Niveau  | Résultat | Réussite")
    print("-" * LARGEUR)

    meilleur_pourcentage = -1
    meilleure_partie = 0
    for i in range(len(resultats)):
        pourcentage = calculer_pourcentage(resultats[i], totaux[i])
        print(f"{i + 1:>6} | {modes_joues[i]:<8} | {niveaux_joues[i]:<7} | "
              f"{resultats[i]:>3} / {totaux[i]:<2} | {pourcentage:>6} %")
        if pourcentage > meilleur_pourcentage:
            meilleur_pourcentage = pourcentage
            meilleure_partie = i + 1

    print("=" * LARGEUR)
    print(f"Meilleure partie : partie {meilleure_partie} ({meilleur_pourcentage} %)")
    print(f"Merci d'avoir joué, {nom}!")


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    # Une seule initialisation du générateur, avant la toute première partie
    random.seed(GRAINE)

    modes_joues = []
    niveaux_joues = []
    resultats = []
    totaux = []

    afficher_bienvenue()
    print()
    nom = utilitaires.lire_texte("Votre nom : ")

    rejouer = True
    while rejouer:
        # Mode de jeu : le nombre de lieux est calculé avec len()
        options_modes = []
        for i in range(len(MODES)):
            lieux, capitales = construire_listes(i + 1)
            details = DETAILS_MODES[i].format(len(lieux))
            options_modes.append(f"{MODES[i]} ({details})")
        print()
        afficher_menu("MODE DE JEU", options_modes)
        mode = utilitaires.lire_entier("Votre choix : ", 1, len(MODES))

        # Niveau de difficulté
        options_niveaux = []
        for i in range(len(NIVEAUX)):
            options_niveaux.append(f"{NIVEAUX[i]} ({NB_QUESTIONS_NIVEAUX[i]} questions)")
        print()
        afficher_menu("NIVEAU DE DIFFICULTÉ", options_niveaux)
        niveau = utilitaires.lire_entier("Votre choix : ", 1, len(NIVEAUX))
        nb_questions = NB_QUESTIONS_NIVEAUX[niveau - 1]

        # Partie
        lieux, capitales = construire_listes(mode)
        nb_bonnes = jouer_partie(lieux, capitales, nb_questions, nom)

        modes_joues.append(MODES[mode - 1])
        niveaux_joues.append(NIVEAUX[niveau - 1])
        resultats.append(nb_bonnes)
        totaux.append(nb_questions)

        print()
        rejouer = utilitaires.lire_oui_non("Voulez-vous rejouer? (o/n) : ")

    print()
    afficher_historique(nom, modes_joues, niveaux_joues, resultats, totaux)


main()



