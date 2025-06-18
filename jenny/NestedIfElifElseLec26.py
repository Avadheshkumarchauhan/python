height =int(input("Enter height in feet : "));
if height>=3:
    print("You can ride ");
    age=int(input("What is your age : "));
    if age<=12:
        print("please pay 150 rupee ");
    elif age<=18:
        print("Please pay 250 rupee");
    else:
        print("Please pay 500 rupee");
else:
    print("You can't ride ");
print("Bye .....");
