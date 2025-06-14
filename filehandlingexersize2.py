f=open("calculater.py")
str1=" "
Ssize=0
lsize=0
print("Line of code : ",len(f.readlines()))
f.seek(0)
while str1:
    str1=f.readline()
    lsize+=len(str1)
    Ssize+=len(str1.strip())
print("Remove all EOL then charater  size : ",lsize)
print("Total charater size : ",Ssize)
f.close()

