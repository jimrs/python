from logika_piskvorky import *

def piskvorky1d():
    game = vytvor_plan()
    control = '-'
    print(game)

    while control == '-':
        game = tah_hrace(game)
        print(game)
        control = vyhodnot(game)

        if control != '-':
            break

        game = tah_pocitace(game)
        print(game)
        control = vyhodnot(game)

    if control == 'x':
        print('Vyhral jsi!')
    elif control == 'o':
        print('Prohral jsi!')
    else:
        print('Remiza!')

piskvorky1d()
