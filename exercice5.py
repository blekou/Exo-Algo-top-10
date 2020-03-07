nombre = ''

while not nombre.isdigit():
    nombre = input("Entrez un nombre: ")

nombre = int(nombre)

for n in range(1, 11):
    print("{0} x {1} = {2}".format(nombre, n, (nombre*n)))