from turtle import *

def draw_pupil(x, y, points, line, fill):
    penup()
    goto(x,y)
    pendown()

    turn = 180 - (360 / points)

    radius = 50

    color(line, fill)


    circle(100)
    
    for i in range(points):
        penup()
        pendown()

        
        lt(350)

        
        fd(100)
        lt(turn)


        
        
        
        
        
    end_fill()

        

draw_pupil(0, 0, 36, "black", "blue")


goto(0)

done()
