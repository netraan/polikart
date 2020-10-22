import random
import turtle
t=turtle.Turtle()
t.hideturtle()
turtle.colormode(255)
for i in range(75):
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.forward(random.randint(1,100))
  t.dot(random.randint(1,85))
  t.right(random.randint(1,350))
  t.pensize(random.randint(1,15))
turtle.done()
