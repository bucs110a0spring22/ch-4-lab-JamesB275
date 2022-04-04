import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
#Part A
def drawSineCurve(turtle=None):
 for radian in range(-360,361):
    y = math.sin(math.radians(radian))
    turtle.goto(radian,y)
    turtle.pendown()
#Part B
def setupWindow(mywindow=None):
  mywindow=turtle.setworldcoordinates(-360,-1,360,1)
def setupAxis(myturtle):
  myturtle.goto(-360,0)
  myturtle.goto(360,0)
  myturtle.goto(0,0)
  myturtle.goto(0,1)
  myturtle.goto(0,-1)
  myturtle.penup()
  
def drawCosineCurve(turtle=None):
  turtle.penup()
  for radian in range(-360,361):
    y = math.cos(math.radians(radian))
    turtle.goto(radian,y)
    turtle.pendown()

def drawTangentCurve(turtle=None):
  turtle.penup()
  for radian in range(-360,361):
    y = math.tan(math.radians(radian))
    turtle.goto(radian,y)
    turtle.pendown()

def raiseNumber(response=None,power=None):
  result=math.pow(response,power)
  return result

def evenOrOdd(pow_result=None):
  if (pow_result%2)==0:
    result_number=print("The resulting number is even")
  else:
    result_number=print("The resulting number is odd")

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
    response=int(input("input a number to be raised to a power: "))
    power=int(input("input a power to raise the number by: "))
    pow_result=raiseNumber(response,power)
    evenOrOdd(pow_result)
    wn.exitonclick()
main()
