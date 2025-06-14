hieghts=input("Enter all hieghts saprated a space : ")
hieghts_list=hieghts.split()
count=0
total=0
for num in hieghts_list:
    count+=1
print(f"size {count}")
for i in range(count):
    hieghts_list[i]=int(hieghts_list[i])
    total+=hieghts_list[i]
avarag=total/count
print(avarag)
