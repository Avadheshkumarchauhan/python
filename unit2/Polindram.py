num=int(input("Enter number "));
rev=0;
n=num;
while n>0:
    d=n%10;
    rev=rev*10+d;
    n//=10;
print("Reverse : ",rev);
if num==rev:
    print(num," is a polindrome");
else:
    print(num," is not polindrome ");