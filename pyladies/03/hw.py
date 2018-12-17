cislo = int(input('Zadej cislo poprve: '))
pom = cislo

cislo = int(input('Zadej cislo podruhe: '))
if cislo < pom:
    pom = cislo

cislo = int(input('Zadej cislo potreti: '))
if cislo < pom:
    pom = cislo

cislo = int(input('Zadej cislo poctvrte: '))
if cislo < pom:
    pom = cislo

cislo = int(input('Zadej cislo popate: '))
if cislo < pom:
    pom = cislo

print('Nejmensi cislo ze zadanych je:', pom)
