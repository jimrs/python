def zamen(str, pos, char):
    return str.replace(str[pos], char)
    # return retezec[:pozice] + znak + retezec[pozice + 1:]

print(zamen('palec', 0, 'v'))
print(zamen('valec', 2, 'j'))