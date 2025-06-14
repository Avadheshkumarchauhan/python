import turtle
import time
turtle.shape("turtle")
x=300
for d in range(100):
    turtle.speed(1) # This method is move curser speed
    turtle.forward(x)  #This method is line lenth
    time.sleep(.5)
    turtle.lt(90)  #This method is tern left
    time.sleep(.5)
    x=x-4

turtle.exitonclick() # Thish method is complated , then click on the exit
#turtle.done()  #This method is complated, then screen hold  
#tuple.mainloop() # This mathod is complated then exit