num=int(input("inter number (0 is quite)"))
total=0
while num!=0:#print all possitive ans negative numver without 0
    #print(num)
    total+=num
    num=int(input())
print(f"sum of number : {total}")
print("out of loop")