from random import randrange

def vyhodnot(game):
    """Vyhodnoti herni stav a vrati retezec o delce 1 reprezentujici stav hry.
    Parametr je herni retezec (herni plan)."""

    if 'xxx' in game:
        return 'x'
    
    elif 'ooo' in game:
        return 'o'

    elif '-' not in game:
        return '!'

    else:
        return '-'

def tah(game, position, symbol):
    """Vrati herni plan se symbolem hrace umistenym na dane pozici"""
    new_game = game[:position] + symbol + game[position+1:]
    return new_game

def tah_hrace(game):
    """Vrati herni plan se symbolem hrace umistenym na pozici, kterou hrac zvoli"""

    while True:
        move = input('Na jakou pozici chces umistit svuj symbol?: ')
        
        if move.isnumeric():
            move = int(move)    # vime, ze je cislo, prevedeme na int pro porovnavani s dalsimi cisly

            if move < 0 or move > 19:
                print('Spatna pozice - zaporne nebo prilis velke cislo.')

            elif game[move] != '-':
                print('Spatna pozice - policko neni volne.')

            else:
                return tah(game, move, 'x')
        
        else:
            print('Spatna pozice - neni cislo.')

def tah_pocitace(game):
    """Vrati herni plan se symbolem pocitace umistenym na pozici vybrane podle jednoduche strategie"""
    
    control = 0

    while control < 20:
        if 'x' in game:
            move = game.index('x', control) - 1     # control nam pomuze postupne hledat volne misto vedle 'x', budeme ho ++

            if move > -1 and game[move] == '-':
                return tah(game, move,'o')
            
            elif move+2 < 20 and game[move+2] == '-':
                return tah(game, move+2, 'o')

            else:
                control = control + 1
        
        else:
            move = randrange[20]
            return tah(game, move, 'o')

def vytvor_plan():
    return '-' * 20