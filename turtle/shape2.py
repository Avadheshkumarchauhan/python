from turtle import Turtle,Screen
s1=Screen()
t1=Turtle()
t1.pencolor("red")
# t1.goto(-200,0)
for s in range(10):
    t1.forward(15)
    t1.penup()
    t1.forward(20)
    t1.pendown()

s1.exitonclick()