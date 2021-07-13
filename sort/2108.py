import sys
import statistics

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    l.append(int(sys.stdin.readline()))

mo = statistics.multimode(l)

print(round(statistics.mean(l)))
print(round(statistics.median(l)))
print(mo[1])
print(max(l)-min(l))