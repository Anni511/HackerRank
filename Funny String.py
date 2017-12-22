#!/bin/python3

import sys

def funnyString(s,r):
    for i in range(1,len(s)):
        if abs(ord(r[i])-ord(r[i-1]))!= abs(ord(s[i])-ord(s[i-1])):
            return "Not Funny"
    return "Funny"
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    r = s[::-1]
    result = funnyString(s,r)
    print(str(result))