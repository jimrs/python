import ai
import util

def vytvor_plan():
    return '-' * 20


def tah_hrace(game):
    """Vrati herni plan se symbolem hrace umistenym na pozici, kterou hrac zvoli"""

    while True:
        move = input('Na jakou pozici chces umistit svuj symbol?: ')
        
        try:
            move = int(move)

        except ValueError:
            print('Zadana pozice je neplatna. Zkus to znovu!')
            print(len(game))

        else:
            if move < 0 or move >= len(game):
                print('Spatna pozice - zaporne nebo prilis velke cislo.')

            elif game[move] != '-':
                print('Spatna pozice - policko neni volne.')

            else:
                return util.tah(game, move, 'x')


def piskvorky1d():
    game = vytvor_plan()
    control = '-'
    print(game)

    while control == '-':
        game = tah_hrace(game)
        print(game)
        control = util.vyhodnot(game)

        if control != '-':
            break

        game = ai.tah_pocitace(game)
        print(game)
        control = util.vyhodnot(game)

    if control == 'x':
        print('Vyhral jsi!')
    elif control == 'o':
        print('Prohral jsi!')
    else:
        print('Remiza!')