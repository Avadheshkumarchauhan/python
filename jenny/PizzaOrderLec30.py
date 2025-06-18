size=input("What pizza size you want (S/M/L) ? : ");
bill=0;
if size.lower() =='s':
    bill +=100;
    print(f"Small size pizza price is {bill} Rs.");
elif size.lower() =='m':
    bill +=200;
    print(f"Small size pizza price is {bill} Rs.");
else:
    bill +=300;
    print(f"Small size pizza price is {bill} Rs.");
pepporoni=input("Do you want pepporoni(Y/N) ? : ");
if pepporoni.lower() =='y':
    if size=='s':
        bill+=20;
    else:
        bill+=30;
extraChize=input("Do you want Extra chize (Y/N) ? : ");
if extraChize.lower()=='y':
    bill+=50;
print(f"Your pizza  total bill is {bill} Rs.")