a = int(input())

def hansoo(n):
    count = 0
    for z in range(110,n+1):
        k = list(map(int, str(z)))
        if k[2]-k[1] == k[1]-k[0]:
            count += 1
    return count

if a < 100:
    print(a)
elif 100 <= a <= 110:
    print("99")
else:
    x = int(hansoo(a))
    print(99+x)