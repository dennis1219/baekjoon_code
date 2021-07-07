n = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    b = 0
    if i > 1:
        for k in range(2,i):
            if i % k == 0:
                b += 1
                break
        if b == 0:
            count += 1

print(count)