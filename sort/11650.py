import sys

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    a,b  = map(int, sys.stdin.readline().split())
    l.append([a,b])

l.sort()

for k in range(len(l)):
    print(str(l[k][0])+" "+str(l[k][1]))