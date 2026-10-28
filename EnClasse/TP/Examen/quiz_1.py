#Raphaël Desjardins
#2026-10-28
#Quiz 1

nombre_lapin = int(input("Combien de lapin seront inscrit au concour (entre 7 et 12)? : "))
liste_poids = []

for i in range(nombre_lapin ):
    poids = float(input(f"Qu'elle est le poid du lapin {i + 1} (kg):"))
    # print(f"lapin {i} : {poids}")
    liste_poids.append(poids)
    
    
print("semaire de la pesé")
print(f"poids saisie {liste_poids}")
print(f"Lapin 4 retirer par demande médical : {liste_poids[3]}")
#retirer le numéro 4 ( 3 dans la liste)

print(liste_poids)


    
print("fin")
  
  
  
  
  
  
# ------ marche pas --------  
# def nombre_de_lapin(nombre_lapin):
#     valide = False
#     while not valide:
#         try:
#             nombre_lapin = int(input("Combien de lapin seront présent (entre 7 et 12)? :"))
#             if 7 <= valeur <= 12:
#                 valide = True
#             else:
#                 print(f"Erreur : entrez un nombre entre 7 et 12.")
#         except ValueError:
#             print("Erreur : ce n'est pas un nombre entier.")
#     valeur = nombre_lapin
#     return valeur

# for i in range(len(nombre_lapin)):
#     print("allo")

