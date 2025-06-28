num1=int(input("Enetr first number : "));
oprater=input("Enetr oprater  : ");
num2=int(input("Enetr second  number : "));
if oprater =="+":
    print("Sum: ",num1+num2);
elif oprater =="-":
    print("Sub: ",num1-num2);
elif oprater =="*":
    print("Mul: ",num1*num2);
elif oprater =="/":
    print("Div: ",num1/num2);
elif oprater =="//":
    print("Div (int): ",num1//num2);
elif oprater =="%":
    print("Rem:  ",num1%num2);
else:
    print("Wrong oprater ");