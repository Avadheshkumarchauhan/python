import os,time
f=open("calculater.py","r")
for i in f:
 print(i)  
 # or
 #print(i.strip()) #this method is print Script
 time.sleep(.8)
time.sleep(10)
os.system('cls')
f.close()
