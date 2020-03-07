
import random

nombre = random.choice(range(10, 21))
choix = ""

while True:
    while not choix.isdigit():
        choix = input("Entrez un nombre comprit entre 10 et 20: ")
    if int(choix) != nombre:
        if int(choix) > 20:
            print("C'est plus petit !")
        elif int(choix) < 10:
            print("C'est plus grand !")
        choix = ""
    else:
        break
