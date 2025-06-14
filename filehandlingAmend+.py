"""
This mode is create file ,read and write in the last index of privius text
"""
f=open("text5.txt","a+")
f2=open("text4.txt","r")
for i in f2:
    
  f.write(i)
f.seek(0)
print(f.read())

f2.close()
f.close()