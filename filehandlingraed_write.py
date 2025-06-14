"""
 this is not a create ,  read and write only
    """

fileName="text1.txt"
f=open(fileName,"r+")
print(f.tell()) # This method  is inform possition of curser
f.write("My") # write a text in file
print(f.tell()) 
data=f.read() # read a text 
print(data) # print file text
print(f.tell())
f.seek(0) # This method is move 0 indext of curser  in text file
print(f.tell())
print(f.read())
print(f.tell())
f.write(" Best of luck \n")
f.close()  # close opration in this file