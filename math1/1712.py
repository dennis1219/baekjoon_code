a,b,c = map(int, input().split())

if b==c:
    print("-1")

else: 
    d = (a//(c-b))+1

    if d>=0:
        print(d)
    else:
        print("-1")