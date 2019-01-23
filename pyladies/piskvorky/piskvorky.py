import ai
import util

def vytvor_plan():
    return '-' * 20
        

def piskvorky1d():
    game = vytvor_plan()
    control = '-'
    print(game)

    while control == '-':
        move = input('Na jakou pozici chces umistit svuj symbol?: ')
        while util.isUserPositionValid(game, move) is False:
            print("Spatne zadana pozice!")
            move = input('Na jakou pozici chces umistit svuj symbol?: ')
        
        move = int(move)    # now we know it is a valid int so we can cast it
        game = util.tah(game, move, 'x')
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