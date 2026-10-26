liste_eleves = [
    [10,10,10],
    [20,20,30],
    [40,40,10],
    [50,60,100]
]

print(liste_eleves[3][2])

for i in range(len(liste_eleves)):
    for j in range(len(liste_eleves[i])):
        print(liste_eleves[i][j])