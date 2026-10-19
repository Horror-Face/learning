

sac = ["gourde", "livre"]
sac.append("crayon")
sac.insert(1, "lunch")
sac.remove("livre")
sac[0] = "bouteille"
objet = sac.pop()
sac.append(objet.upper())
print(sac)