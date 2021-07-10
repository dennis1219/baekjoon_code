import sys
import math

n = int(sys.stdin.readline())

l = [["*"]*n for i in range(n)]

a = round(math.log(n,3))

for k in range(a):
    blank = [y for y in range(n) if (y // 3 ** k) % 3 == 1]
    for y in blank:
        for x in blank:
            l[y][x] = " "

print('\n'.join([''.join([str(y) for y in z]) for z in l]))