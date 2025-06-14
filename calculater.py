import os

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b
opration_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
}

def calculator():
    number1=eval(input("Enter  first number : "))
    for symbol in opration_dict:
        print(symbol) 
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an opration : ")
        number2=eval(input("Enter second number : "))
        calculator_function=opration_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        shoud_continue=input(f"Enter 'y' to continue calcutation with {output} or 'n' to start a new calculation or  'x' to exit : ").lower()
        if shoud_continue=='y':
            number1=output
        elif shoud_continue=='n':
            continue_flag=False
            os.system("cls")
            calculator()
        else:
            continue_flag=False
            print("Ashish RAj....... Aman Raj")
            
            
calculator()