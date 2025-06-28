num=int(input("Enter number : "));
n=num;
arm=0;
while n>0:
    dig=n%10;
    arm+=dig**3;
    n//=10;
if arm==num:
    print(num," is armstrong number");
else:
    print(num," is not armstrong number");
