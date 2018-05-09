import math
lines = int(input())
numbers = []
for i in range(0,lines):
    numbers.append(int(input()))


for i in numbers:
    # print(i)
    if int(i) == 1:
        print("Not prime")
    elif int(i) == 2:
        print("Prime")
    else:
        flag=False
        for j in range(2,int(math.sqrt(i)+1)):
            if int(i)%j == 0:
                print("Not prime")
                flag=True
                break
        if flag == False:
            print("Prime")