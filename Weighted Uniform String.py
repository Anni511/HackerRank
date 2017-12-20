#!/bin/python3

import sys

s = input().strip()
n = int(input().strip())
USS_Sum = set()
j=1
for i in range(len(s)-1):
    USS_Sum.add((ord(s[i])-96)*(j))
    if(s[i]==s[i+1]):
        j=j+1
    else:
        j=1
USS_Sum.add((ord(s[len(s)-1])-96)*j)

for a0 in range(n):
    x = int(input().strip())
    if (x in USS_Sum):
        print("Yes")
    else:
        print("No")