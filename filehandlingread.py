"""
read(n)method is return all text,
and n=size of string  
readline() method is return 1 line
redlines() method is return full text in list
read a file only
""" 
#f=open("text1.txt")  # or
f=open("text1.txt","r")
data=f.read() # read file text
print(data) # print text which that text in file
f.close() # opration is close not read this file
#print(f.read())  # when opration close then file not read .. Valueerror :I/O poration on close file

