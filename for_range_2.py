
# sum of number 
x=int(input("Enter number : "))
total=0
#for i in range(2,x+1 , 2):
   #or
for i in range(1,x+1):
     if i%2==0:
        total +=i
print(f"sum of 1 to {x} = {total}")     