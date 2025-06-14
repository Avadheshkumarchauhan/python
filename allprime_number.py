def prime_checker(number):
    np=0
    p=0
    for n in range(2,number+1):          
        for i in range( 2, number+1):
            if n%i==0:             
                break
        if n==i:
            p+=1
        else:
            np+=1
             
    print(f"Number of 2 to {number} prime numer = {p}")
    print(f"Number of 2 to {number} not prime = {np}")
                
num=int(input("Enter number 1 to n prime ! "))

prime_checker(number = num) 


