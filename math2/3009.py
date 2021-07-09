a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())
l = list()

if a == c:
    l.append(e)
elif a == e:
    l.append(c)
else:
    l.append(a)

if b == d:
    l.append(f)
elif d == f:
    l.append(b)
else:
    l.append(d)

print(l[0],l[1],sep=" ")