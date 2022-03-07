import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
#Part A
def drawSineCurve(turtle):
 for radian in range(-360,360):
    y = math.sin(math.radians(radian))
    turtle.goto(radian,y)  
#Part B
def setupWindow(mywindow=None):
  mywindow=turtle.setworldcoordinates(0,-1.5,360,1.5)
def setupAxis(myturtle=None):
   myturtle=turtle.setup(startx=0,starty=0)
  





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    #drawCosineCurve(dart)
    #drawTangentCurve(dart)
    wn.exitonclick()
main()
