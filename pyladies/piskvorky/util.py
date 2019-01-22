def tah(game, position, symbol):
    """Vrati herni plan se symbolem hrace umistenym na dane pozici"""
    
    if position >= len(game):
        raise IndexError('Position is too big for this game plan!')

    new_game = game[:position] + symbol + game[position+1:]
    return new_game

def vyhodnot(game):
    """Vyhodnoti herni stav a vrati retezec o delce 1 reprezentujici stav hry.
    Parametr je herni retezec (herni plan)."""

    if 'xxx' in game:
        return 'x'
    
    elif 'ooo' in game:
        return 'o'

    elif isGameFull(game):
        return '!'

    else:
        return '-'


def isGameFull(game):
    if '-' not in game:
        return True


def isUserPositionValid(game, move):
    try:
        move = int(move)
    
    except ValueError:
        return False

    else:
        if move < 0 or move >= len(game):
            return False

        elif game[move] != '-':
            return False

        else:
            return True

    