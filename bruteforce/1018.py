import sys

x,y = map(int, sys.stdin.readline().split())
l = list()
sol = list()
for i in range(x):
    l.append(sys.stdin.readline())

for a in range(x-7):
    for b in range(y-7):
        count1 = 0
        count2 = 0
        for c in range(a,a+8):
            for d in range(b,b+8):
                if (c+d) % 2 == 0:
                    if l[c][d] != "W":
                        count1 += 1
                    if l[c][d] != "B":
                        count2 += 1
                else:
                    if l[c][d] != "B":
                        count1 += 1
                    if l[c][d] != "W":
                        count2 += 1
        sol.append(count1)
        sol.append(count2)

print(min(sol))