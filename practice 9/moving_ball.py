import turtle
import time
screen = turtle.Screen()
screen.title("Clock")
screen.bgcolor("white")
screen.setup(500, 300)
pen = turtle.Turtle()
pen.hideturtle()
while True:
   pen.clear()
   t = time.strftime("%M:%S")
   pen.write(t, align="center", font=("Arial", 40, "bold"))
   time.sleep(1)