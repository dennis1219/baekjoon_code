"""
a = int(input())

b = 1

while  a//(b*(b+1)//2) > 1:
    b += 1

c = a - b*(b+1)//2

if b%2 == 0:
    print("%d/%d"%(b-c+2,c))
else:
    print("%d/%d"%(c,b-c+2))

print(b,c)
"""
#While coding I found out that the numbers were rows and columns of the given table. how stupid... I redesigned the algorithm...

a = int(input())
b = 1

while a > b:
    a -= b
    b += 1
    
if b%2 == 0:
    print("%d/%d"%(a,b-a+1))
else:
    print("%d/%d"%(b-a+1,a))