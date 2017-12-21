#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    Num = ""
    flag = False
    Temp = 0

    for i in range(1, (len(s) // 2)+2):
        if(len(s)==1):
            flag= False
            break
        N = int(s[len(s)-i:len(s)])
        Num = str(N)
        for j in range(1,(len(s))):
            if(N-j>0):
                Num = str(N-j) + Num
                Temp= N-j
            if(s==Num):
                print("YES" +" " +str(Temp))
                flag = True
                break
        if flag==True:
            break
    if flag == False:
        print("NO")