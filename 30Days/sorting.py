#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps=0
for i in range(0,len(a)-1):
    flag=False
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            flag=True
            swaps+=1
    if flag == False:
        break

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {} \nLast Element: {}".format(a[0],a[n-1]))
