n,k = map(int, input().split())
a = k
num = list(i for i in range(1,n+1))
l = list()

for j in range(n):
    l.append(num[a-1])
    del num[a-1]
    a += k-1
    while True:
        if len(num) == 0:
            break
        elif a > len(num):
            a -= len(num)
        else:
            break

print("<"+", ".join(map(str,l))+">")