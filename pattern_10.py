w=int(input("Enter width : "))
l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(w):
        if j==0 or i==l-1 :
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)