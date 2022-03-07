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
    turtle.down()
#Part B
def setupWindow(mywindow=None):
  mywindow=turtle.setworldcoordinates(-360,-1,360,1)
def setupAxis(myturtle):
  myturtle.goto(-360,0)
  myturtle.goto(360,0)
  myturtle.goto(0,0)
  myturtle.goto(0,1)
  myturtle.goto(0,-1)
  myturtle.up()
  
def drawCosineCurve(turtle):
  turtle.down()
  turtle.up()
  for radian in range(-360,360):
    y = math.cos(math.radians(radian))
    turtle.goto(radian,y)
    turtle.down()

def drawTangentCurve(turtle):
  turtle.down()
  turtle.up()
  for radian in range(-360,360):
    y = math.tan(math.radians(radian))
    turtle.goto(radian,y)
    turtle.down()




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
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
