
nmb_dep = ''

while not nmb_dep.isdigit():
    nmb_dep = input("Entrez un nombre de depart: ")

nmb_dep = int(nmb_dep)
print("Les dix nombres suivants sont: ")
for i in range(nmb_dep+1, nmb_dep+11):
    print(i)
