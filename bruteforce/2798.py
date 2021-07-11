import sys

n,m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = set()

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                break
            val = l[i] + l[j] + l[k]
            if val <= m:
                s.add(val)

print(max(s))