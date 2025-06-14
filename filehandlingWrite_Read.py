
"""
 This is  a create ,write and read. 
"""

fileName="text6.txt"
f=open(fileName,"w+")
f.write("hello \n how are you\n i am fine\n") # write a text in file
print(f.tell()) 
f.seek(0)
data=f.read() # read a text 
print(data) # print file text
f.seek(0) # This method is move 0 indext of curser  in text file
print(f.tell()) # This method  is inform possition of curser
print(f.read())
f.write("best of luck \n")
f.close()  # close opration in this file