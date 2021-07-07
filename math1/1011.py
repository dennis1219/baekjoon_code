"""

t = int(input())

for i in range(t):
    x,y = map(int, input().split())
    a = (y-x)//2
    if y-x == 1:
        print("1")
    elif (y-x)%2 == 0:
        print(a+1)
    else:
        print(a+2)

"""
#Didn't read the problem properly. Trying again.

import math

t = int(input())

for i in range(t):
	x,y = map(int, input().split())
	if y-x <= 3:
		print(y-x)
	else:
		a = int(math.sqrt(y-x))
		if y-x == a**2:
			print(2*a-1)
		elif a**2 < y-x <= a**2 + a:
			print(2*a)
		elif a**2 + a < y-x <= a**2 + 2*a:
			print(2*a+1)