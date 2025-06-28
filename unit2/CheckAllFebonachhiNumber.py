import math;
def isPerfectSquare(x):
    s=int(math.sqrt(x));
    return s*s==x;
def isFebonach(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4);
i=int(input("Enter febonachhi number : "));
for k in range(0,i+1):
    if isFebonach(k)==True:
        print(f"{k} is a febonachhi number ");
    else:
        print(f"{k} is not a febonachhi number ");
    