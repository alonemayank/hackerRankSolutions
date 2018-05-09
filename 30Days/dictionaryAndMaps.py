lines = int(input())
dict = {}
for i in range(0,lines):
    key,value = input().split(" ")
    dict[key] = value

for i in range(lines):
    key = input()
    if (key in dict):
        print("{}={}".format(key,dict[key]))
    else:
        print("Not found")