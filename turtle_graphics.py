from turtle import *

def draw_pupil(x, y, points, line, fill):
    penup()
    goto(x,y)
    pendown()

    turn = 180 - (360 / points)

    radius = 50

    color(line, fill)


    circle(50)
    
    for i in range(points):
        penup()
        lt(90)
        fd(50)
        pendown()
        
        rt(180)
        fd(50)
        
    end_fill()

        

draw_pupil(0, 0, 36, "black", "blue")


goto(0)

done()
