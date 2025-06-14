numbers=input("Enter list numbers:")
num_list=numbers.split()
#print(num_list)
count=0
for n in num_list:
    count+=1
print(f"The lenth of the list is : {count}")
for i in range(count):
    num_list[i]=int(num_list[i])
print(num_list)
max_number=num_list[0]
for num in num_list:
    if num > max_number:
        max_number=num
print(f"maximum number is : {max_number}")