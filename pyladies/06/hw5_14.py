radky = int(input('Zadej pocet radku: '))
sloupce = int(input('Zadej pocet sloupcu: '))

for radek in range(radky):
    for sloupec in range(sloupce):
        if radek == 0 or radek == radky-1:
            print ('X', end=' ')
        
        elif sloupec == 0 or sloupec == sloupce-1:
            print('X', end=' ')
        
        else:
            print(' ', end=' ')
    
    print()