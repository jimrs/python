cisla_string = input('Zadej 3 cisla oddelena mezerou: ')

cisla = cisla_string.split()

sum = 0

for num in cisla:
    sum += int(num)

if sum > 10:
    print('Soucet je vetsi nez 10.')

else:
    print('Sum je mensi nebo rovno 10.')