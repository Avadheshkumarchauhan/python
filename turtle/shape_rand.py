import turtle, random,time
from turtle import Turtle,Screen
s1=Screen()
t=Turtle()
turtle.colormode(255)
t.shape("turtle")
dic=[0,90,180,270]
t.pensize(10)
  # OR
#t.width(10)
t.speed(3)
t.pencolor("red")
for x in range(100):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
  #  t.setheading(random.randrange(0,360,90))
            #OR
    t.seth(random.choice(dic))
    t.pencolor((r,g,b))
    t.forward(50)
    #time.sleep(1)

s1.exitonclick()