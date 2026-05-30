import turtle
import random

#Game window
segments = []

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) #turn off automatic animation

#Pause and resume feature
pause = False
def toggle_pause():
  global paused
  paused = not paused
screen.onkey(toggle_pause, "p") #Press P to pause or resume.
  
#Create the snake
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction ="stop"

#Control the game using keyboard(W-A-S-D)
def go_up():
  if head.direction != "down":
    head.direction ="up"
def go_down():
  if head.direction !="up":
    head.direction ="down"
def go_left():
  if head.direction !="left":
    head.direction ="right"
def go_right():
  if head.direction !="right":
    head.direction ="left"

screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "d")
screen.onkey(go_right, "a")

#Add food to game
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)

#Move the snake, each move is 20pixels
def move():
  if head.direction == "up":
    head.sety(head.ycor() + 20)
  if head.direction =="down":
    head.sety(head.ycor() - 20)
  if head.direction =="left":
    head.setx(head.xcor() - 20)
  if head.direction =="right":
    head.setx(head.xcor() +20)



#main game loop
import time

while True:
  screen.update()

  if not pause:

#move the snake body
   for index in range(len(segments) - 1, 0, -1):
    x =segments[index - 1].xcor()
    y =segments[index - 1].ycor()
    segments[index].goto(x, y)

  if len(segments) > 0:
    segments[0].goto(head.xcor(), head.ycor())  

  #check snake collision with food
  if head.distance(food) < 20:
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)
    move()
    delay -=0.001 # increased speed slightly.


#Collision with wall(game over)
  if abs(head.xcor()) >290 or abs(head.ycor()) >290:
   time.sleep(1)
   head.goto(0, 0)
   head.direction = "stop"

   new_segment =turtle.Turtle()
   new_segment.shape("square")
   new_segment.color("green")
   new_segment.penup()
   segments.append(new_segment)
   segments.clear()
   
    

  for segment in segments:
    segment.goto(1000, 1000)#Make the snake grow

  delay = 0.1

  move()
  delay = 0.1
  time.sleep(delay)