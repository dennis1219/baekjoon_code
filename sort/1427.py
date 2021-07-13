import sys

n = int(sys.stdin.readline())
l = list()

for i in str(n):
    l.append(int(i))

l.sort(reverse=True)

print(''.join(map(str, l)))