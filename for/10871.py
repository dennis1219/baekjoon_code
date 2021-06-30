a,b = map(int, input().split())
c = list(map(int, input().split()))

for k in range(a):
	if c[k]<b:
		print(c[k], end=" ")