"""
    create file and write opration    
    """
f=open("text2.txt","w") # create file  
string1=input("Enter string : ") #inut string user daynamicaly
f.write(string1) # write text in text file
f.close() # close opration mode 
#f.write(" hello , How are you ? ")  # ValueError : I/O opration on close file because file is close 
