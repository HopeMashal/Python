import turtle

wind = turtle.Screen()   #Window (Screen)
wind.title("Ping Pong Game") #set the title of the window
wind.bgcolor("black") #set the background color of the window
wind.setup(width=800,height=600) #set the width and height of the window
wind.tracer(0)  #stops the window from updating automatically

#Madrab #1
madrab_1 = turtle.Turtle()  #initializes turtle objects(shape)
madrab_1.speed(0) # set the speed of the animation
madrab_1.shape("square") #set the shape of the object
madrab_1.color("blue") #set the color of the shape
madrab_1.shapesize(stretch_wid=5,stretch_len=1) #stretch the shape to meet the size
madrab_1.penup() #stops the object from drawing lines
madrab_1.goto(-350,0) #set the position of the object

#Madrab #2
madrab_2 = turtle.Turtle()
madrab_2.speed(0)
madrab_2.shape("square")
madrab_2.color("red")
madrab_2.shapesize(stretch_wid=5,stretch_len=1)
madrab_2.penup()
madrab_2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Functions
def madrab_1_up():
  y = madrab_1.ycor() #get the y coordinate of the madrab #1
  y += 20  
  madrab_1.sety(y) #set the y of the madrab #1 to the new y coordinate
def madrab_1_down():
  y = madrab_1.ycor()
  y -= 20
  madrab_1.sety(y)

def madrab_2_up():
  y = madrab_2.ycor()
  y += 20
  madrab_2.sety(y)
def madrab_2_down():
  y = madrab_2.ycor()
  y -= 20
  madrab_2.sety(y)

#keyboard bindings
wind.listen()  #tell the window to expect keyboard input
wind.onkeypress(madrab_1_up, "w")  # when pressing w the function madrab_1_up is invoked
wind.onkeypress(madrab_1_down, "s")

wind.onkeypress(madrab_2_up, "Up")
wind.onkeypress(madrab_2_down, "Down")

#main game loop
while True:
  wind.update()  #update the screen every time the loop run

