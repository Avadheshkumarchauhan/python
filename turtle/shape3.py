import time ,random
from turtle import Turtle,Screen
s1=Screen()
t2=Turtle()
cl=["red","green","yellow","pink","blue","gray","orange","brown",]
t2.pencolor(("green"))
for i in range(3,9):
    ang=360/i
    
    t2.pencolor(random.choice(cl))
    for d in range(i):
       t2.pensize(2)
       t2.speed(1)
       t2.forward(100)
       t2.lt(ang)
       time.sleep(.5)

s1.exitonclick() 