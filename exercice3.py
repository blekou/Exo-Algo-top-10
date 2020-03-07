
nmb_dep = ''

while not nmb_dep.isdigit():
    nmb_dep = input("Entrez un nombre de depart: ")

nmb_dep = int(nmb_dep)
print("Les dix nombres suivants sont: ")

nmb_fin = nmb_dep+10

while nmb_dep < nmb_fin:
    nmb_dep += 1
    print(nmb_dep)
