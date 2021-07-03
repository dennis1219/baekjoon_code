a = int(input())-2
k = (a//6)

if a == -1:
    print("1")
else:
    p = 2*k
    n = round(((-1)+(1+4*p)**0.5)//2)
    print(n+2)