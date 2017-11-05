import sys
import math

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
# For K > N we can reduce the problem by taking mod
k = k%n
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for a0 in range(q):
    m = int(input().strip())
    if(m>=k):
        print(a[m-k])
    elif (m<k):
        print(a[n-k+m])