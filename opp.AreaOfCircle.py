class Circle:
    pi=3.14
    def __init__(self,r=7):
        self.radius=r
    def cercumferance(self):
        return 2*self.pi*self.radius
    def area(self):
        return Circle.pi*self.radius**2
            
obj=Circle(6)
print("circumferance : ", obj.cercumferance())
print("Circle of Area : ", obj.area() )
