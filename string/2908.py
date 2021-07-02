a,b = map(int, input().split())

if str(a)[::-1] > str(b)[::-1]:
    print(str(a)[::-1])
else:
    print(str(b)[::-1])