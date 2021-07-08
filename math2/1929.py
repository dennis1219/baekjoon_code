import sys

m,n = map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    b = 0
    if i > 1:
        for k in range(2,int(i**0.5)+1):
            if i % k == 0:
                b += 1
                break
        if b == 0:
            print(i)