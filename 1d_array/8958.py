n = int(input())
for i in range(n):
	b = list(input())
	c = 0
	d = 0

	for i in b:
		if i=='O':
			d+=1
			c+=d
		elif i=='X':
			d=0
		else:
			break

	print(c)