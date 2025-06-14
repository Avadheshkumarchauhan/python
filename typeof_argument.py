def greet (name,dp):
    print(f"Hi {name}")
    print(f"Are you {dp} deparment")
# possinal argument
name=input("Enter name here :")
dep=input("Enter deparment here :")

greet(name,dep)

def add(*number):
    c=0
    for i in number:
        c+=i
    print(f"sum of number is {c}")
add(3,4,5,2)
add(4,6,7,)