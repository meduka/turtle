from turtle import *
import math

ted = Turtle()

fred = Turtle()



def draw_eye(x, y, line, fill):
    penup()
    
    ted.goto(x, y)
    
    pendown()

    color(line, fill)

    begin_fill()

    for i in range(1):
        
        ted.lt(45)
        ted.fd(100)
        ted.rt(45)
        ted.fd(100)
        ted.rt(45)
        ted.fd(100)
        ted.rt(90)
        ted.fd(50)
        ted.rt(45)
        ted.fd(170)
        ted.rt(45)
        ted.fd(50)
    end_fill()



    


def draw_pupil(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        fd(100)
        lt(turn)
    end_fill()


speed(10)






def blink(x, y):

    clear()

    ted.hideturtle()

    ted.goto(x, y)

    for i in range(10):
        #placeholder
        ted.fd(100)
        ted.lt(90)
        #placeholder

    ted.showturtle()




draw_eye(-100, 0, "white", "white")

draw_pupil(-50, 5, 36, "black", "blue")


def drawLogarithmicSpiral(a, b, line):
  # This sets the turtle cursor to the center of the screen and readies it for drawing
    ted.up()
    ted.setpos(0, 0)
    ted.down()

    color(line)


    # This is an arbitrary range that seems to make the prettiest spirals
    # The last parameter is the amount the cursor moves per step. Feel free to mess around with the numbers
    # and see what happens!
    for i in range(0, 3000, 5):
      # Draw a spiral 
        t = math.radians(i)
        x = a*math.exp(b*t)*math.cos(t)
        y = a*math.exp(b*t)*math.sin(t)
        # Since our turtle is down, we'll be drawing the spiral as we move positions.
        ted.setpos(x, y)
        

# These two values for a and b are very arbitrary, change them up and see what happens!
drawLogarithmicSpiral(0.20, 0.20, "white")

