import math

def prime_checker(number):
    prime=True
    if number==1:
        prime=False
    for i in range(2,math.ceil( number/2)+1):
        if number%i==0:
            prime=False
            
    if prime==True:
        print(" It is a prime number " )
    else:
        prime("It is not a prime number ")
        
num=eval(input("Enter number here! "))

prime_checker(number=num)
        