#Raphaël
#2026-08-30
#essaie perso pytho


#code généré par IA pour comprendre Python
#nom
while True:
    name = input("What is your name? ")
    if name.strip() == "":
        print("Name cannot be empty. Try again.\n")
        continue
    #name.replace est pour les noms composés, on enlève les espaces pour vérifier si le reste est alphabétique
    if not name.replace(" ", "").isalpha():
        print("Name should only contain letters. Try again.\n")
        continue
    break

while True:
    age_input = input("What is your age? ")
    try:
        age = int(age_input)
    except ValueError:
        print("That's not a valid number. Try again.\n")
        continue
    if age < 0 or age > 120:
        print("Please enter a realistic age (0-120).\n")
        continue
    break

print(f"\nNice to meet you, {name}! You are {age} years old.")
