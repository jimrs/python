def tah(game, position, symbol):
    """Vrati herni plan se symbolem hrace umistenym na dane pozici"""
    
    new_game = game[:position] + symbol + game[position+1:]
    return new_game