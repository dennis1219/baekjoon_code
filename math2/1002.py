n = int(input())

for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    max = r1 + r2
    min = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print("-1")
        else:
            print("0")
    else:
        if d == max or d == min:
            print("1")
        elif d < max and d > min:
            print("2")
        else:
            print("0")