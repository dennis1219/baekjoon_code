import sys
import math

k,n = map(int, sys.stdin.readline().split())
l = list()

for i in range(k):
    a = int(sys.stdin.readline())
    l.append(a)

ans = list()

for sol in range(round(sum(l)/n + 1),math.floor(min(l)/n + 1),-1):
    if sol == 0:
        continue
    sum_list = list()
    for k in l:
        sum_list.append(k//sol)
    if sum(sum_list) >= n:
        print(sol)
        break

#Binary search required, but used PyPy3 to bypass.