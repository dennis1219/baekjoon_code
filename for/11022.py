import sys

n = int(input())

for k in range(n):
	a,b = map(int, sys.stdin.readline().split())
	t = ''.join(['#', f'{k+1}', ":"])
	print("Case",t, "%d + %d ="%(a,b), a+b)