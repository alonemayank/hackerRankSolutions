#!/bin/python3

import sys


n = int(input().strip())

something = "{0:b}".format(n)
prev = 0
curr = 0
count = 0
max = 0
for i in something:
    #print(i,end=' ')
    if i == '1':
        count+=1
        if(max<count):
            max=count
    else:
        count = 0
print(max)