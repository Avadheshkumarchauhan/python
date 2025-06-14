w=int(input("Enter width : "))
l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(w):
        if (j==0 and i<l//2) or i==0 or (j==w-1 and i>l//2) or i==l//2 or  i==l-1:
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)