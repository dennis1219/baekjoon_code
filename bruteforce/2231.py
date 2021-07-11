import sys

n = int(sys.stdin.readline())
l = list()

for i in range(1,999955):
    val = i + sum(map(int, str(i)))
    l.append(val)

while True:
    try: 
        print(1 + l.index(n))
        break
    except:
        print("0")
        break