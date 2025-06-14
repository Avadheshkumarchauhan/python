num=int(input("inter number (0 is quite)"))
total=0
while num>0:#print only possitive numver
    #print(num)
    total+=num
    num=int(input())
print(f"sum of number : {total}")
print("out of loop")