l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(l):
        if (j==0 and i!=l//2) or (j==l-1 and i!=l//2)or i==l//2 and j==l//2 :
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)