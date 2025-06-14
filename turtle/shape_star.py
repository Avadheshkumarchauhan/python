import random,turtle,time
from turtle  import Turtle,Screen
t=Turtle()
s=Screen()
t.getscreen()
t.pensize(1.5)
t.shape("arrow")
t.color("red","yellow")
t.begin_fill()
t.speed(3)
while True:
    t.forward(500)
    t.left(170)
    if t.heading()==0:
        break
t.end_fill()
s.exitonclick()
