import sys
import statistics

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

mo = statistics.multimode(l)

print(round(statistics.mean(l)))
print(round(statistics.median(l)))
if len(mo) == 1:
    print(mo[0])
else:
    print(mo[1])
print(max(l)-min(l))