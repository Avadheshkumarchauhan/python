num=int(input("Enter fectorial number : "));
fec=1;
if num<0:
    print("Sorry ! please enter positive value");
elif num==0:
   print(f"Fectorial of {num} is {fec}");
else:
    for i in range(1,num+1):
        fec*=i;
    print(f"Fectorial of {num} is {fec}");