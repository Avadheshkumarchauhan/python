num1=int(input("Enetr first number : "));
num2=int(input("Enetr second number : "));
num3=int(input("Enetr third number : "));
if num1>num2:
    if num1>num3:
        print("First number is big");
    else:
        print("Third number is big");
else:
    if num2>num3:
        print("Second number is big");
    else:
        print("Third number is big");