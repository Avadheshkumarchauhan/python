num =int(input("Enter number : "));
flag=True;
if num<=0:
    print("Please enter positive value ");
elif num==1:
    print(num," is not prime nummber ");
else:
    for i in range(2,num):
        if num%i==0:
            flag=False;
            break;
    if flag:
        print(num," is a prime");
    else:
         print(num," is not a prime");