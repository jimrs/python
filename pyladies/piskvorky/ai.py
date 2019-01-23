from random import randrange

import util

def tah_pocitace(game, symbol):
    """Vrati herni plan se symbolem pocitace umistenym na pozici vybrane podle jednoduche strategie"""

    if util.isGameFull(game):
        raise Exception('Game plan is full! The AI cannot move!')

    move = randrange(20)
    return util.tah(game, move, symbol)