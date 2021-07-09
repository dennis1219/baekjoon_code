"""
import sys
import math

def f(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

k = list(range(2,5000))
l = list()

for z in k:
    if f(z):
        l.append(z)

n = int(sys.stdin.readline())

for y in range(n):
    num = int(sys.stdin.readline())
    e = list()
    g = list()
    for c in l:
        for d in range(len(l)):
            if num - c == l[d]:
                e.append(c)
                g.append(l[d])
    print(e[len(e)//2],g[len(e)//2],sep=" ")
"""
#Damn timeover... Also I reversed the list when using the code above.

import sys

l = [False, False] + [True] * 10002

for i in range(2, 10002):
    if l[i]:
        for k in range(2*i, 10002, i):
            l[k] = False

n = int(sys.stdin.readline())

for x in range(n):
    n = int(sys.stdin.readline())
    a = n // 2
    b = a
    while a > 0:
        if l[a] and l[b]:
            print(a,b,sep=" ")
            break
        else:
            a -= 1
            b += 1
#Instead of defining f(x), I used it directly to make T/F list to show all the prime numbers. Starting from the middle to solve Goldbach.