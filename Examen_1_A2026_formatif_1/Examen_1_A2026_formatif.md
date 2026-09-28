# Examen 1 — Exercice pratique

Nom : ______________________________________

## Pondération

L'examen 1 vaut **10%** de la note finale : **3%** pour le volet théorique, **7%** pour le volet pratique (*cet exercice*).

## Consignes générales

- Documentation personnelle **permise** pour le volet pratique seulement. Elle doit être sur le poste (OneDrive synchronisé, clé USB).
- **Aucun partage** entre étudiants, pendant et après l'examen.
- **Internet interdit**, sauf Léa pour la remise.
- **Aucun appareil mobile.**
- Outils générateurs de code (ChatGPT, Claude, Copilot, etc.) **interdits**.
- Plagiat ou partage = **zéro** pour tous les étudiants impliqués.
- Durée : **3 périodes consécutives (2 h 40)**.

## Exigences techniques

- Un seul fichier Python (`.py`) dans VS Code.
- Seulement les notions vues en classe (cours 1 à 5 et fiches *Outils*).
- Boucles : **`while` seulement** (seule boucle vue à date).
- Noms de variables significatifs.
- Constantes au début du programme.
- Messages et bulletin le plus fidèles possible à l'exemple.
- **Toute saisie est validée.** Le programme ne plante jamais.
- Saisie invalide : message d'erreur **en rouge**, puis on repose la question.
- Entête et commentaires comme vu en classe.
- Code lisible et bien organisé.

## Énoncé

La ligue des enseignants paresseux veut un programme qui produit un bulletin de session.

1. **Nom** — Demander le prénom et le nom de l'étudiant.
   - Refuser un nom vide (ou seulement des espaces).
   - Refuser un nom sans espace (prénom **et** nom requis).
   - Le prénom est avant le **premier espace**. Le nom est le reste.
   - *Suggestion* : `.find(" ")` donne la position de l'espace. Utiliser ensuite des tranches (`chaine[:position]`, `chaine[position + 1:]`) pour séparer.
2. **Notes** — Demander la note de chacun des **5 cours**, avec une **boucle `while`**.
   - Une note est un **nombre réel**, entre **0 et 100** inclusivement.
   - Le séparateur décimal est le **point** (ex. : `80.5`).
3. **Constantes** — Le nombre de cours (5), les bornes (0 et 100) et le seuil de réussite (60) sont des constantes.
4. **Calculs**
   - La **moyenne** des 5 notes.
   - La **meilleure** et la **pire** note, avec le numéro du cours. En cas d'égalité, garder le premier cours.
   - L'**écart** entre la meilleure et la pire note.
   - Le **nombre d'échecs** (note sous 60).
   - La **mention**, selon la moyenne :

     | Moyenne      | Mention   |
     | ------------ | --------- |
     | 90 et plus   | Excellent |
     | 75 à < 90    | Très bien |
     | 60 à < 75    | Réussite  |
     | moins de 60  | Échec     |

5. **Bulletin** — Afficher le bulletin, puis terminer.
   - Date du jour au format `AAAA-MM-JJ`.
   - Nom affiché sous la forme `NOM, Prénom` (ex. : `bob JAVA` → `JAVA, Bob`).
   - *Suggestion* : `.upper()` pour le nom. Pour le prénom, `.upper()` sur la 1re lettre (`prenom[0]`) et `.lower()` sur le reste (`prenom[1:]`).
   - Notes, écart et moyenne à **1 décimale**.
   - Moyenne et mention **en vert** si la moyenne est de 60 ou plus, sinon **en rouge**.
   - Échecs **en rouge** s'il y en a au moins un, sinon **en vert**.
   - Le bulletin fait **50 caractères** de large.

## Exemples d'exécution

Les valeurs saisies sont en **gras**. Les messages d'erreur s'affichent en rouge.

### Exemple 1 — Validations, mention « Très bien », 1 échec

<pre>
Prénom et nom de l'étudiant : <b></b>
Le nom ne peut pas être vide. Recommencer, SVP.
Prénom et nom de l'étudiant : <b>bob</b>
Entrer le prénom et le nom. Recommencer, SVP.
Prénom et nom de l'étudiant : <b>bob JAVA</b>
Note du cours 1 : <b>cinquante</b>
Cette note est invalide. Recommencer, SVP.
Note du cours 1 : <b>122</b>
La note doit être entre 0 et 100. Recommencer, SVP.
Note du cours 1 : <b>81,5</b>
Cette note est invalide. Recommencer, SVP.
Note du cours 1 : <b>81.5</b>
Note du cours 2 : <b>75</b>
Note du cours 3 : <b>55.5</b>
Note du cours 4 : <b>96</b>
Note du cours 5 : <b>71</b>

               BULLETIN DE SESSION
++++++++++++++++++++++++++++++++++++++++++++++++++
| Date                :               2026-10-01 |
| Étudiant            :                JAVA, Bob |
| Meilleure note      :           96.0 (cours 4) |
| Pire note           :           55.5 (cours 3) |
| Écart               :              40.5 points |
| Moyenne (5 cours)   :              75.8 points |   ← vert
| Mention             :                Très bien |   ← vert
| Échecs              :                  1 cours |   ← rouge
++++++++++++++++++++++++++++++++++++++++++++++++++
</pre>

### Exemple 2 — Mention « Excellent », aucun échec

<pre>
Prénom et nom de l'étudiant : <b>alice TREMBLAY</b>
Note du cours 1 : <b>92</b>
Note du cours 2 : <b>88.5</b>
Note du cours 3 : <b>95</b>
Note du cours 4 : <b>90</b>
Note du cours 5 : <b>99</b>

               BULLETIN DE SESSION
++++++++++++++++++++++++++++++++++++++++++++++++++
| Date                :               2026-10-01 |
| Étudiant            :          TREMBLAY, Alice |
| Meilleure note      :           99.0 (cours 5) |
| Pire note           :           88.5 (cours 2) |
| Écart               :              10.5 points |
| Moyenne (5 cours)   :              92.9 points |   ← vert
| Mention             :                Excellent |   ← vert
| Échecs              :                  0 cours |   ← vert
++++++++++++++++++++++++++++++++++++++++++++++++++
</pre>

### Exemple 3 — Mention « Échec », plusieurs échecs, nom en plusieurs mots

<pre>
Prénom et nom de l'étudiant : <b>jean de la Fontaine</b>
Note du cours 1 : <b>45</b>
Note du cours 2 : <b>62</b>
Note du cours 3 : <b>58.5</b>
Note du cours 4 : <b>40</b>
Note du cours 5 : <b>71</b>

               BULLETIN DE SESSION
++++++++++++++++++++++++++++++++++++++++++++++++++
| Date                :               2026-10-01 |
| Étudiant            :     DE LA FONTAINE, Jean |
| Meilleure note      :           71.0 (cours 5) |
| Pire note           :           40.0 (cours 4) |
| Écart               :              31.0 points |
| Moyenne (5 cours)   :              55.3 points |   ← rouge
| Mention             :                    Échec |   ← rouge
| Échecs              :                  3 cours |   ← rouge
++++++++++++++++++++++++++++++++++++++++++++++++++
</pre>

### Exemple 4 — Mention « Réussite » malgré 2 échecs, notes égales

<pre>
Prénom et nom de l'étudiant : <b>SARAH côté</b>
Note du cours 1 : <b>80</b>
Note du cours 2 : <b>55</b>
Note du cours 3 : <b>80</b>
Note du cours 4 : <b>55</b>
Note du cours 5 : <b>65</b>

               BULLETIN DE SESSION
++++++++++++++++++++++++++++++++++++++++++++++++++
| Date                :               2026-10-01 |
| Étudiant            :              CÔTÉ, Sarah |
| Meilleure note      :           80.0 (cours 1) |
| Pire note           :           55.0 (cours 2) |
| Écart               :              25.0 points |
| Moyenne (5 cours)   :              67.0 points |   ← vert
| Mention             :                 Réussite |   ← vert
| Échecs              :                  2 cours |   ← rouge
++++++++++++++++++++++++++++++++++++++++++++++++++
</pre>

> Exemple 4 : en cas d'égalité, on garde le **premier** cours (80 aux cours 1 et 3 → cours 1; 55 aux cours 2 et 4 → cours 2).

## Grille de correction

| Critère | Points |
| --- | :---: |
| Déclaration et utilisation des constantes, variables appropriées | 2 |
| Saisie et validation du nom (vide, prénom + nom) | 3 |
| Saisie des 5 notes dans une boucle `while` | 3 |
| Validation des notes (type, intervalle) | 4 |
| Calculs (moyenne, meilleure/pire + cours, écart, échecs) | 4 |
| Mention (conditions enchaînées) | 2 |
| Bulletin : date, nom formaté, couleurs, alignement | 4 |
| Professionnalisme (entête, commentaires, nomenclature, lisibilité) | 3 |
| **TOTAL** | **25** |

## Remise

Remettre **seulement le fichier `.py`** dans la boîte de remise Léa.

Remise en retard = refusée. **Prévoyez votre remise à l'avance.**

Bon travail!