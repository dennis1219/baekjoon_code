m = int(input())
n = int(input())
l = list()
count = 0

for i in range(m,n+1):
    b = 0
    if i > 1:
        for k in range(2,i):
            if i % k == 0:
                b += 1
                break
        if b == 0:
            l.append(i)
            count += 1

if count == 0:
    print("-1")
else:
    print(sum(l))
    print(min(l))