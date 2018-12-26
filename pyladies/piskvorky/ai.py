from random import randrange

import util

def tah_pocitace(game):
    """Vrati herni plan se symbolem pocitace umistenym na pozici vybrane podle jednoduche strategie"""

    move = randrange(20)
    return util.tah(game, move, 'o')