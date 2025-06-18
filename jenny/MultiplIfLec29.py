height=int(input("What is your height : "));
if height>3:
    bill=0;
    print("You can ride ");
    age=int (input("What is your age : "));
    if age<12:
        bill=150;
        print(f"Ticket price is {bill} Rs.");
    elif age<18:
        bill=250;
        print(f"Ticket price is {bill} Rs.");
    else:
        bill=500;
        print(f"Ticket price is {bill} Rs.");
    photo=input("You want to take photo (Y/N) ? : ");
    if photo.upper() =="Y":
        bill+=50;
    print(f"Your total bill is {bill} Rs.");
else:
    print("You can't ride ");
print("Thank you . Enjoy the ride ")