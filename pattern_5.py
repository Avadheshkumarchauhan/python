
l=int(input("Enter lenth more than 3 : "))
print()
result=""
for i in range(l):
    for j in range(l):
        if i==0 or i==l-1 or i+j==l-1:
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)

print("reverse Z ")

result=""
for i in range(l):
    for j in range(l):
        if i==0 or i==l-1 or i==j:
           # print("*" ,end="")
           result+="*"
        else:
           # print(" ",end ="")
           result+=" "
   # print()
    result +="\n"
    
print(result)