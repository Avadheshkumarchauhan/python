import turtle
import time
turtle.getscreen()
turtle.shape("turtle")
for x in range(4):
    turtle.forward(100)
    time.sleep(.9)
    turtle.left(90)
    time.sleep(1) 


turtle.exitonclick()