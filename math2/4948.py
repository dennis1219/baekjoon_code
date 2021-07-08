"""
import sys
import math

while True:
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        if i > 1:
            for k in range(2,int(math.sqrt(i)+1)):
                if i % k == 0:
                    break
            else:
                count += 1
    print(count)
"""
#Timeover 1

"""
from math import sqrt

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1,2*n+1):
        if i == 1:
            continue
        elif i == 2:
            count += 1
            continue
        else:
            for k in range(2,int(sqrt(i)+1)):
                if i % k == 0:
                    break
            else:
                count += 1
    print(count)
"""
#Timeover 2

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

k = list(range(2,246912))
l = list()

for z in k:
    if f(z):
        l.append(z)

t = int(sys.stdin.readline())

while t != 0:
    count = 0
    for y in l:
        if t < y <= t*2:
            count += 1
    print(count)
    t = int(sys.stdin.readline())
#Finally... Need a bit of rest... Uhh...