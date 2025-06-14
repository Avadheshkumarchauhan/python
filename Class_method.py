class instracter:
    fellowers=0
    
    def __init__ (self , name , subject):
        self.fname=name
        self.subject1=subject
        print("Hello, constracter ")
        print(self.fname ,subject)
    def updatefellower(self,name):
        self.fellowers+=1
        self.name=name
        print(self.name)
        
obj1=instracter("Avadhesh","Python")
print(obj1.fellowers)
print(obj1.subject1)
obj1.updatefellower("Rani")
print(obj1.fellowers)

