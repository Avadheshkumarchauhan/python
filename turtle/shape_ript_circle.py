import random,turtle
from turtle import Turtle,Screen
t=Turtle()
s=Screen()
turtle.colormode(255)
t.getscreen()
t.shape()
t.pensize(1.5)
t.speed(0)
while True:
    r=random.randrange(0,255)
    b=random.randrange(0,255)
    g=random.randrange(0,255)
    t.pencolor((r,g,b))
    t.circle(100)
    t.left(4)
    if t.heading()==0:
        break
s.exitonclick()