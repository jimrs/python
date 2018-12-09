from random import randrange, uniform

a = 0
b = 5
randrange(a, b)     # nahodny INT od a do b-1
uniform(a, b)       # nahodny REAL od a do b

cislo = randrange(0, 3)  # číslo je od 0, 1, nebo 2
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:  # 2
    print('Trojúhelníček')