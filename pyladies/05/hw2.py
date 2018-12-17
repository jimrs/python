from turtle import left, right, forward, exitonclick
from math import sqrt

def nakresli_dum(zed):
    forward(zed)
    left(135)
    forward(sqrt(2) * zed)
    right(90)
    forward((sqrt(2) * zed) / 2)
    right(90)
    forward((sqrt(2) * zed) / 2)
    right(135)
    forward(zed)
    left(90)
    forward(zed)
    left(135)
    forward(sqrt(2) * zed)
    right(135)
    forward(zed)

zed_arg = int(input('Zadej velikost zdi: '))
nakresli_dum(zed_arg)
exitonclick()

