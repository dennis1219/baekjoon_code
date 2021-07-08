"""
import sys

n = int(sys.stdin.readline())
l = list()

if n == 1:
    print()

for i in range(0,n+1):
    b = 0
    if i > 1:
        for k in range(2,i):
            if i % k == 0:
                b += 1
                break
        if b == 0:
            l.append(i)

for z in l:
    while n % z == 0:
        print(z)
        n = n//z
"""
#Making the list of prime numbers and divinding it individually seems to cause timeover.

n = int(input())
a = 2

while n != 1:
    if n % a == 0:
        print(a)
        n = n // a
    else:
        a += 1