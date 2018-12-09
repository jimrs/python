from turtle import forward, left, exitonclick, pendown, penup

for i in range(20):
    forward(i)
    penup()
    forward(5)
    pendown()

exitonclick()