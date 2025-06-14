w=int(input("Enter width : "))
l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(w):
        if (j==0 and i<l-1)  or  (i==l-1 and 1<=j<w-1) or (j==w-1 and i!=l-1):
               result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)