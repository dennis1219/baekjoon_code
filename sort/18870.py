import sys

n = int(sys.stdin.readline())
l = (list(map(int, sys.stdin.readline().split())))
s = list(set(l))

s.sort()

"""
for i in l:
    print(s.index(i), end = ' ')
"""
#Index function causes timeover.

dic = {s[i]:i for i in range(len(s))}

print(dic)

for k in l:
    print(dic[k], end=' ')