"""
import sys

a = list(sys.stdin.readline().upper())
k = list()

for i in range(len(a)):
    c = a.count(a[i])
    k.append(c)

if k.count(max(k)) == max(k):
    print(a[str(a).find(str(max(k)))])
else:
    print("?")

Time over. Tried to simplify it twelve times but didn't work. Need to figure out aanother algorithm to meet the conditions given in the problem.
"""

a = input().upper()
b = list(set(a))
s = list()

for i in b:
    c = a.count(i)
    s.append(c)

if s.count(max(s)) == 1:
    print(b[(s.index(max(s)))])
else:
    print("?")

#While coding with function set, I figured out the sys.stdin.readline will add value "\n" to the set...