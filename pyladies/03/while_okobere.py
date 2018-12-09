from random import randrange

body = 0

while True:
    print('Mas', body, 'bodu.')
    answer = input('Chces pokracovat? ')

    if answer == 'ne':
        if body == 21:
            print('Mas 21 bodu, jsi borec.')
        else:
            print('Hodne stesti priste.')

        break
    
    elif answer == 'ano':
        karta = randrange(2, 11)
        print('Vylosoval jsi kartu s hodnotou', karta)
        body += karta

        if body > 21:
            print('Prohral jsi, mas', body, 'bodu.')
            break
    
    else:
        print('Spatna odpoved.')
    
print('Konec hry.')