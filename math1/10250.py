t = int(input())

for i in range(t):
	h,w,n = map(int, input().split())
	a = n%h
	b = (n//h)+1
	if a == 0:
		a = h
		b -= 1
	print(100*a+b)
"""
	if a == 0 and b<10:
		print(f'{h}0{b-1}')
	elif a == 0 and b>=10:
		print(f'{h}{b-1}')
	elif a != 0 and b<10:
		print(f'{a}0{b}')
	else:
		print(f'{a}{b}')
"""
#Fixed