import sys

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    a,b = sys.stdin.readline().rstrip().split()
    age = int(a)
    name = str(b)
    order = i+1
    l.append((age,name,order))

l.sort(key = lambda x : (x[0],x[2]))

for k in range(len(l)):
    print(str(l[k][0])+" "+str(l[k][1]))