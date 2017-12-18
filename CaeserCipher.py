#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
k = k%26
q = ""
for i in range(len(s)):
    if(s[i].isalpha()== True):
        if(s[i].isupper()==False) :
            q = q+chr((ord(s[i])+k-97)%26 + 97)
        elif (s[i].isupper()==True):
            q = q + chr((ord(s[i]) + k - 65)%26 + 65)
        else:
            q = q + chr(ord(s[i]) + k)
    else:
        q = q+s[i]
print(q)