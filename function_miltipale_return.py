import statistics,os,time
def mean_mode_median(list1):
    
    return [statistics.median(list1),statistics.mean(list1),statistics.mode(list1)]

result=mean_mode_median([2,3,5,6,8,4,9])
print(result)
a,b,c=result
print(f"Median is {a} \n Mean is {b} \n Mode is {c}")

delay=time.sleep(6)
clear=os.system("cls")

def add(x,y):
    if x==0 and y==0:
        return
    else:
        return a+b
    
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
sum=add(a,b)
print(f"sum = { sum}")

time.sleep(8)
os.system('cls')        