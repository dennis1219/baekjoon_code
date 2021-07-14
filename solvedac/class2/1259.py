import sys

while True:
    a = sys.stdin.readline().rstrip()
    if a == '0':
        break
    l = list()
    s = list()
    for i in a:
        l.append(i)
        s.append(i)
    l.reverse()
    if s == l:
        print("yes")
    else:
        print("no")