n = int(input())

for i in range(n):
	a = list(map(int, input().split()))
	z = sum(a[1:])/a[0]
	c = 0

	for k in a[1:]:
		if k>z:
			c+=1
		else:
			c+=0
	r = f'{(c/(len(a)-1)*100):0.3f}'
	print(r+"%")