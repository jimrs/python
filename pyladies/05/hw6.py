prijmeni = input('Zadej prijmeni: ')

if len(prijmeni) < 4:
    print('to je nejake divne jmeno')

else:

    if prijmeni.endswith('á') or prijmeni.endswith('a'):
        print('je to zenska!!!')
    else:
        print('buzna')