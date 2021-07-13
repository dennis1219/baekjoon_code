import sys

n = int(sys.stdin.readline())
sol = [0 for i in range(10001)]

for k in range(n):
    a = int(sys.stdin.readline())
    sol[a] += 1

for x in range(len(sol)):
    for y in range(sol[x]):
        print(x)