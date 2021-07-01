a = set(list(range(1,10001)))
s = set()

def self(n):
    z = 0
    l = list(map(int, str(n)))
    z = n + sum(l)
    s.add(z)

for k in range(1,10001):
    self(k)

c = a - s
d = list(c)
list.sort(d)

for i in range(len(d)):
    print(d[i])

#Studied Python for 6 hours. Solving this problem gives me confidence.