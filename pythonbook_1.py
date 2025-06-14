print("hello")
print('\a')
x=65 # 65 is a ASCII value
print(chr(x)) #A, ASCCII value to convert charater 
y="a"
print(ord(y)) #97 is a ASCII value, charater to convert ASCII VALUE 
print("........SMALL LETTER .....")
for x in range(ord('a'),ord('z')+1):  # print a to z alphabate
    print(chr(x),end=" ")
print("\n...... CAPITAL LATTER ......")
for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end=" ")
    
print()
for y in range(0,10100): # print Symbole
    print(f"A[{y}]={chr(y)} : ",end=" ")
    
print("\n Welcome ")
sx="\\"
print(sx) #print \
sx="\ab"
print(sx ) #b
print("\ab ",len(sx))
a="seema\'s pen"
print(a)
s='\"'
print(s)
print(len(s))
w="xy\
yz"
print(w)
print(len(w))
p='''xy
yz'''
print(p)
print(len(p))
text="Welcome\
to\
python"
print(text) 
print(len(text))
text1="""Welcome
To
python
"""
print(text1)
print(len(text1))
num=input("Enter number : ")
double=int(num)*2
print(double)
FLOAT=.17E-03
print(FLOAT)
w=4
print(w)
x=40
y=x+1
x=20,x+y,5,6
print(x,y)
a,b=12,13
print(print(a+b))
print(
float(input("enter ")))
str(print("hello"))+"one"