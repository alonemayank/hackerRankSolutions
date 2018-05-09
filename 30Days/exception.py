!/bin/python3

import sys


S = input().strip()
#print(type(S))

try:
    print(int(S))
except Exception:
    print("Bad String")
    