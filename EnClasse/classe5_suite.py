
print("début")
valide = False
while not valide:
    try:
        age = int(input("quel est ton âge? : "))
        print(f" Tu as {age} ans")
        valide = True
    except:
        print("Une erreur a été détecter")

print("fin")