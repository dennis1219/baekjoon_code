"""
a,b,c = map(int, input().split())

height = 0
day = 0

while True:

	if height >= c:
		print(day)
		break
	elif height < c:
		if height + a >= c:
			day += 1
			print(day)
			break
		else:
			height += a-b
			day += 1
"""
#Time over. Need to find other way to solve this problem.

import sys

a,b,c = map(int, sys.stdin.readline().split())

if (c-b)%(a-b) != 0:
    print(((c-b)//(a-b))+1)
else:
    print(((c-b)//(a-b)))