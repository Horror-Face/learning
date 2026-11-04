#Raphael Desjardins
#2026-10-21
#avion

liste_avion = []

#rajoute des valeur
liste_avion.append("A-10")
liste_avion.append("A-20")

#place la donner a une position donnée
liste_avion.insert(0, "A-30")

liste_avion.append("A-40")

print(liste_avion)

#nombre de valeur dans la liste
print(len(liste_avion))

#print juste les 2 premier ( le nombre après les 2 point est toujours exclu)
print(liste_avion[0:2])

# avion = liste_avion.pop(0)

# print(f"Avion {avion} décolle")
# print("fin")

# avion = input("Quel avion voulez-vous faire décoller? : ")
# if avion in liste_avion:
#     liste_avion.remove(avion)
#     print("c'est partie")
# else:
#     print("l'avion n'exite pas ou n'est pas rentré")

while len(liste_avion) > 0:
    avion = liste_avion.pop()
    print(f"Avion {avion} décolle!")

print("fin")


