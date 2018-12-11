from turtle import left, right, forward, exitonclick
from math import sqrt

n = int(input('zadej pocet hran n-uhelniku: '))
strana = 100/n


for hrana in range(n):
    forward(strana)
    strana += strana
    #left(180 - (180 * (1-2/n)))
    left(90)

exitonclick()
