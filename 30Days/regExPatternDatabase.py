#!/bin/python3

import sys
import re

list = []
regex = r".*@gmail.com"
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if(re.search(regex,emailID)):
        list.append(firstName)
list.sort()
for i in list:
    print(i)