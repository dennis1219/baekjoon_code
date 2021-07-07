n = int(input())

a = n // 5

for i in range(a,-1,-1):
    b = n - 5*i
    if b % 3 == 0:
        print(i + b//3)
        break
    elif i == 0 and n % 3 != 0:
        print("-1")
        break