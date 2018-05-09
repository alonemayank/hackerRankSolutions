lines = int(input())

for i in range(lines):
    string = input()
    temp = list(string)
    temp1= ""
    temp2 = ""
    for j in range(0,len(string)):
        if j%2==0:
            temp1 += str(temp[j])
        else:
            temp2 +=  str(temp[j])
    print(temp1+" "+temp2)
