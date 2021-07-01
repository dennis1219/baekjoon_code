a = int(input())

for i in range(a):
    b = list(map(str, input().split()))
    c = int(b[0])
    d = b[1]
    e = list(map(str, str(d)))
    f = list()
    for k in range(len(e)):
        f.append(e[k]*c)
    g = "".join(f)
    print(g)

#Study more about strinig! Too much unnecessary conversions!