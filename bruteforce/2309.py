import sys

l = list(int(sys.stdin.readline().rstrip()) for i in range(9))
l.sort()
z = list()

for a in range(9):
    for b in range(9):
        if a == b:
            continue
        for c in range(9):
            if a == c or b == c:
                continue
            for d in range(9):
                if a == d or b == d or c == d:
                    continue
                for e in range(9):
                    if a == e or b == e or c == e or d == e:
                        continue
                    for f in range(9):
                        if a == f or b == f or c == f or d == f or e == f:
                            continue
                        for g in range(9):
                            if a == g or b == g or c == g or d == g or e == g or f == g:
                                continue
                            else:
                                if l[a]+l[b]+l[c]+l[d]+l[e]+l[f]+l[g] == 100:
                                        z.extend([l[a], l[b], l[c], l[d], l[e], l[f], l[g]])
                                        break

for i in range(7):
    print(z[i])