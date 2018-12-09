from turtle import forward, left, right, exitonclick

forward(50)
left(60)

for hexagon in range(6):
    for hrana in range(3):
        forward(50)
        left(60)
    right(120)

left(120)
forward(50)

for hexagon in range(6):
    for hrana in range(2):
        right(60)
        forward(50)

    left(180)
    forward(50)

exitonclick()
