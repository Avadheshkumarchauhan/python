
n=int(input("Enter start range: "));
num=int(input("Enter end number : "));

c=0;
if num<=0:
    print("Sorry ! please positive number ");
else:
    for i in range(n,num+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break;
            else:
                c+=1;
                print(i ,end=" ");
                
    print();
print(f" {n} to {num}  number of prime : {c} ");