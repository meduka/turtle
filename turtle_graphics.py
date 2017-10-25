from turtle import *

import math

boi = Turtle()

boi2 = Turtle()



boi2.fd(100)

boi.shapesize(10)

def draw_pupil(x, y, points, line, fill):
    penup()
    boi.goto(x,y)
    pendown()

    turn = 180 - (360 / points)

    radius = 50

    color(line, fill)


    circle(100)
    
    for i in range(points):
        penup()
        pendown()

        
        lt(60)

        
        fd(100)
        lt(turn)


        
        
        
        
        
    end_fill()

        

draw_pupil(0, 0, 36, "black", "blue")


goto(0)



degrees(2*math.pi)
done()
