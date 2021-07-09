import sys

while True:
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    a = l[0]
    b = l[1]
    c = l[2]
    if a == 0 and b == 0 and c == 0:
        break
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")