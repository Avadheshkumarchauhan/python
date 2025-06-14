w=int(input("Enter width : "))
l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(w):
        if j==0 or (i==0 and j!=w-1) or (i==l-1 and j!=w-1) or (j==w-1 and 0<i<l-1):
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)