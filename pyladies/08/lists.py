def vyber_spravne(seznam):
    spravne_zaznamy = []
    spravna_jmena = []

    for polozka in seznam:
        cele_jmeno = polozka.split()
        
        for jmeno in cele_jmeno:
            if jmeno[0].isupper():
                spravna_jmena.append(jmeno)

        if len(spravna_jmena) == 2:         # pokud je spravna_jmena delky 1, tak je spravne bud jen prijmeni, nebo krestni jmeno
            spravne_zaznamy.append(polozka)
        else:
            spravna_jmena.clear()

    return spravne_zaznamy


def vyber_chybne(seznam):
    chybne_zaznamy = []
    chybna_jmena = []

    for polozka in seznam:
        cele_jmeno = polozka.split()
        
        for jmeno in cele_jmeno:
            if jmeno[0].islower():
                chybna_jmena.append(jmeno)

        if len(chybna_jmena) > 0:
            chybne_zaznamy.append(polozka)
            chybna_jmena.clear()

    return chybne_zaznamy


def oprav_zaznamy(seznam):
    opravene_zaznamy = []
    opravena_jmena = []

    for polozka in seznam:
        cele_jmeno = polozka.split()
        
        for jmeno in cele_jmeno:
                opravena_jmena.append(jmeno.capitalize())

        opravene_cele_jmeno = ' '.join(opravena_jmena)
        opravene_zaznamy.append(opravene_cele_jmeno)
        opravena_jmena.clear()

    return opravene_zaznamy


zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy) # → ['Jiří Sládek']

opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy) # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']

