import json

meilleurs_scores = [
    ["Abby", 1250],
    ["Éloi", 980],
    ["Zoé", 875],
]

with open("EnClasse\scores.json", "w", encoding="utf-8") as fichier:
    json.dump(meilleurs_scores, fichier, indent=4, ensure_ascii=False)


with open("EnClasse\scores.json", "r", encoding="utf-8") as fichier:
    meilleurs_scores = json.load(fichier)

for rangee in meilleurs_scores:
    print(f"{rangee[0]:<10}{rangee[1]:>6}")

print(type(meilleurs_scores[0][1]))