from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    
    for i in range(points):
        fd(700)
        lt(turn)
    end_fill()


speed(10)

draw_star(0, 0, 180, "orange", "blue")

go(90)


done()
