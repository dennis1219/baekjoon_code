a = int(input())
b = list(map(int, input().split()))
c = max(b)
d = (100/c*(sum(b)))/a
print(d)