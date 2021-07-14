import sys
import itertools

n,r = map(int, sys.stdin.readline().split())
l = list()

for i in range(n):
    l.append(i+1)

sol = list(itertools.permutations(l,r))


for j in sol:
    print(*j)

#Used * to unpack.