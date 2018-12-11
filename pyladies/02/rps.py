from random import randrange

tah_pocitace_int = randrange(3)

if tah_pocitace_int == 0:
    tah_pocitace = 'kamen'
elif tah_pocitace_int == 1:
    tah_pocitace = 'nuzky'
else:
    tah_pocitace = 'papir'

tah_cloveka = input('kamen, nuzky, nebo papir? ')

if tah_cloveka == tah_pocitace:
    print('Plichta')

elif (tah_cloveka == 'kamen' and tah_pocitace == 'nuzky') or (tah_cloveka == 'nuzky' and tah_pocitace == 'papir') \
        or (tah_cloveka == 'papir' and tah_pocitace == 'kamen'):
    print('Vyhrála jsi!')

elif (tah_cloveka == 'kamen' and tah_pocitace == 'papir') or (tah_cloveka == 'nuzky' and tah_pocitace == 'kamen') \
        or (tah_cloveka == 'papir' and tah_pocitace == 'nuzky'):
    print('Počítač vyhrál.')

else:
    print('Nerozumím.')
