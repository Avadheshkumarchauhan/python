w=int(input("Enter width : "))
result=""
for i in range(w+1):
    for j in range(i):
           result+="*"
           result+=" "
    result +="\n"
#print(result)
for i in range(w-1,0,-1):
    for j in range(i,0,-1):
           result+="*"
           result+=" "
    result +="\n"
    
print(result)