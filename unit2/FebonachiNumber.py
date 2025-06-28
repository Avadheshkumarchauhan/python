num=int(input("Enter febonachi number : "));
a,b=0,1;
feb=0;
if num<=0:
    print("Sorry Neagative value not febonachi number! Enter positive value");
elif(num==1):
    print(a,end=" ");
else:
    print( a,",",b,end=" ");
    for i in range(3,num+1):
        feb =a+b;
        a=b;
        b=feb;
        print(",",feb,end=" ");