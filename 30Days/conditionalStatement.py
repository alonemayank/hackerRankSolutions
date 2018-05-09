#!/bin/python3

import sys


N = int(input().strip())

print("Not Weird") if (N>20 and N%2==0) or N==2 or N==4 else print("Weird")

