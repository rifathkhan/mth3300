#******************************************************************************
# windows.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import turtle

num_windows = int(input("Enter the number of windows: "))
panes = int(input("Enter the number of panes: "))

tscr = turtle.Screen() 
crush = turtle.Turtle()
crush.shape("turtle")
crush.color("green")
crush.pencolor("blue")

def setPosition(distance):
    crush.pu()
    crush.backward(distance)
    crush.pd()

def drawPanes (panes):
    for i in range(panes):
            for n in range(2):
                crush.forward(25)
                crush.left(90)
                crush.forward(50)
                crush.left(90)
            crush.forward(25)

def moveTurtleUp() :
    crush.left(90)
    crush.pu()
    crush.forward(100)
    crush.right(90)
    crush.pd()
    
def moveTurtleDown() :
    crush.right(90)
    crush.pu()
    crush.forward(100)
    crush.left(90)
    crush.pd()
    
setPosition(300)
crush.speed(1000)
    
for window in range(1,num_windows+1):
    drawPanes(panes)
    if window % 2 != 0:
        moveTurtleUp()
    else:
        moveTurtleDown()

crush.hideturtle()

tscr.mainloop()
turtle.bye()  


