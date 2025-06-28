import math;
def isPerfectSquare(x):
    s=int(math.sqrt(x));
    return s*s==x;
def isFebonach(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4);
i=int(input("Enter febonachhi number : "));
if isFebonach(i)==True:
    print(f"{i} is a febonachhi number ");
else:
    print(f"{i} is not a febonachhi number ");
    