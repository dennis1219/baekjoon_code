n = int(input())
l = list()

for i in range(n):
    a = int(input())
    l.append(a)

l.sort()

for k in l:
    print(k)