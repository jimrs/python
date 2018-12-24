from math import sqrt, ceil

def sito (n):
    if n == 1:
        return [1]

    cisla = list(range(2, n+1))
    podminka = int(sqrt(n))

    for i in cisla:
        if i > podminka:
            return cisla
        
        for j in range(i, int(n/i) + 1):
            if i*j in cisla:
                cisla.remove(i*j)
            else:
                continue

prime = int(input('Zadej n, na kterem chces provest test prvociselnosti: '))
candidates = sito(prime)
if prime in candidates:
    print('Zadane cislo je prvocislo.')
else:
    print('Zadane cislo neni prvocislo.')