#!/bin/python3

import sys

def gemstones(arr):
    # Complete this function
    for i in range(len(arr)-1):
        arr[i+1]= arr[i].intersection(arr[i+1])
    return len(arr[len(arr)-1])
n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr_t = set(arr_t)
   arr.append(arr_t)
result = gemstones(arr)
print(result)
