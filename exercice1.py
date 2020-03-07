
import random

nombre = random.choice(range(1,4))
choix = ""

while True:
    if not choix.isdigit() or  int(choix) != nombre:
        choix = input("Entrez un nombre comprit entre 1-3: ")
    else:
        break
