from turtle import *
import math

colormode(255)

ted = Turtle()
fred = Turtle()
boye = Turtle()
spinnie = Turtle()


bgcolor(0, 0, 0)

fred.speed(10)

ted.shapesize(5)

ted.pensize(2)
fred.pensize(2)
spinnie.pensize(2)


spinnie.shape("circle")

spinnie.pencolor(255, 255, 255)


def draw_eye(x, y, line, fill):
    ted.penup()
    ted.goto(x, y)
    ted.pendown()

    ted.color(line, fill)
    boye.color(line, fill)

    ted.begin_fill()

    

    ted.lt(45)
    ted.fd(100)

    for i in range(2):
        ted.rt(45)
        ted.fd(100)
        
    ted.rt(90)
    ted.fd(50)
    ted.rt(45)
    ted.fd(170)
    ted.rt(45)
    ted.fd(50)

    ted.end_fill()

    

    boye.penup()
    boye.goto(-85, 80)
    boye.pendown()
    
    boye.begin_fill()
    
    for i in range(3):
        boye.forward(50) 
        boye.left(120)
        boye.forward(50) 
        boye.left(120)
        boye.forward(50) 
        boye.left(120)

        boye.penup()
        boye.fd(75)
        boye.pendown()

    boye.end_fill()

    

        
        

        
    


def draw_pupil(x, y, points, line, fill):
    fred.penup()
    fred.goto(x, y)
    fred.pendown()

    turn = 180 - (360 / points)

    fred.color(line, fill)

    fred.begin_fill()
    for i in range(points):
        fred.fd(100)
        fred.lt(turn)
    fred.end_fill()





def blink():

    fred.clear()
    
    fred.hideturtle()
    boye.hideturtle()
    ted.hideturtle()

    fred.speed(100)

    for i in range(2):
        fred.clear()
        draw_pupil(-50, 0, 36, "black", "blue")
        fred.clear()
        draw_pupil(-25, 0, 36, "black", "blue")
        fred.clear()
        draw_pupil(0, 0, 36, "black", "blue")
        fred.clear()
        draw_pupil(-25, 0, 36, "black", "blue")
        fred.clear()
        draw_pupil(-50, 0, 36, "black", "blue")
    

    for i in range(10):
        ted.circle(10)
        ted.penup()
        ted.lt(75)
        ted.forward(20)
        ted.pendown()

    fred.showturtle()


def sparkle(points, line, fill):

    for i in range(5):
        if fred.isvisible() == True:
            fred.shapesize(10)
            fred.penup()
            fred.goto(150, -50)
            fred.pendown()

            turn = 180 - (360 / points)

            fred.color(line, fill)

            fred.begin_fill()
            
            for i in range(points):
                fred.fd(20)
                fred.lt(turn)
                fred.end_fill()

                
            turn = 180 - (360 / points)

            fred.color("black", fill)

            fred.begin_fill()
            
            for i in range(points):
                fred.fd(20)
                fred.lt(turn)
                fred.end_fill()


    while fred.shapesize(10) == True:
        fred.pensize(0)

    while fred.isvisible() == True:
        fred.shape("turtle")
        fred.hideturtle()

    if fred.isvisible() == False:
        fred.clear()
        

    


draw_eye(-110, -10, "white", "white")

draw_pupil(-50, 0, 36, "black", "blue")

blink()

sparkle(18, "white", "yellow")


def drawLogarithmicSpiral(a, b):
  # This sets the turtle cursor to the center of the screen and readies it for drawing
    spinnie.up()
    spinnie.setpos(0, 0)
    spinnie.down()

    # This is an arbitrary range that seems to make the prettiest spirals
    # The last parameter is the amount the cursor moves per step. Feel free to mess around with the numbers
    # and see what happens!
    for i in range(0, 3000, 5):
      # Draw a spiral 
        t = math.radians(i)
        x = a*math.exp(b*t)*math.cos(t)
        y = a*math.exp(b*t)*math.sin(t)
        # Since our turtle is down, we'll be drawing the spiral as we move positions.
        spinnie.setpos(x, y)
        

# These two values for a and b are very arbitrary, change them up and see what happens!
drawLogarithmicSpiral(0.20, 0.20)
# The turtle.mainloop() function prevents the program from quitting after the drawing has been made.
