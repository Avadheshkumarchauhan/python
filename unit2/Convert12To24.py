str1=input("Enter Time formate(09:45:33 PM) : ");

def Convert24(str1):
    if  str1[-2:].upper()=="AM" and str1[:2].upper() =="12":
        return "00"+str1[2:-2];
    elif str1[-2:].upper()=="AM":
        return str1[:-2];
    elif str1[-2:].upper()=="PM" and str1[:2]=="12":
        return str1[:-2];
    else:
        return str(int(str1[:2])+12)+str1[2:-2];
print(Convert24(str1));