import turtle
screen = turtle.Screen()
screen.title("Moving Ball")
screen.bgcolor("white")
screen.setup(800, 600)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
step = 20
def left():
   if ball.xcor() > -380:
       ball.setx(ball.xcor() - step)
def right():
   if ball.xcor() < 380:
       ball.setx(ball.xcor() + step)
def up():
   if ball.ycor() < 280:
       ball.sety(ball.ycor() + step)
def down():
   if ball.ycor() > -280:
       ball.sety(ball.ycor() - step)
screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.mainloop()