#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    count = 0
    str = "hackerrank"
    flag = False
    j=0
    for i in range(len(s)):
        if (s[i]==str[j]):
            j= j + 1
        if(j==10):
            break
    if (j == 10):
        print("YES")
    else:
        print("NO")