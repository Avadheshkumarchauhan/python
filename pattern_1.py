w=int(input("Enter width : "))
l=int(input("Enter lenth : "))
result=""
for i in range(l):
    for j in range(w):
        if (j==w-1 and i!=0) or( j==0 and i>0 ) or (i==0 and 1<=j<w-1 ) or i==int(l/2):
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)