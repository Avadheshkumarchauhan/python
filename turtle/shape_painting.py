import turtle,time,random
from turtle import Turtle , Screen
s1=Screen   ()
t=Turtle()
t.shape()
turtle.colormode(255)
s1.screensize(500,500)  #This method is scren Size
t.penup()
t.speed(0)
for x in range(1000):
    r=random.randrange(0,255)
    b=random.randrange(0,255)
    g=random.randrange(0,255)
    t.pencolor((r,g,b))
    t.goto(random.randint(-500,500),random.randint(-500,500))
    t.dot(20) #This method is create a bubbols
    #time.sleep(.5)

s1.exitonclick()