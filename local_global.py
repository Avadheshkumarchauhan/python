a=10 # global variabal
def display():
    a=15 # local varaibal
    print(a)
    def sow():
        global a
        a=30
        print(f"value of a before calling sow() function is {a}")
    sow()
    print(f"value of a before calling sow() function is {a}")

display()
print(a)

name ="python"
def show():
    global name
    name=name + " programing "
    print(name)
show()
print(name)