a = input()
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
c = 0

for i in range(len(a)):
    for k in b:
        if a[i] in k:
            c += b.index(k)+3

print(c)