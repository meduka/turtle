from turtle import *

def draw_face(x, y, points, line, fill):
    penup()
    goto(x,y)
    pendown()

    color(line, fill)

    for i in range(points):
        fd(100)
        rt(45)
        fd(50)
        lt(60)


draw_face(0, 0, 1, "black", "blue")

go(0)

done()
