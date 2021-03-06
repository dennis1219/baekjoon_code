import sys

n = int(sys.stdin.readline())
l = list()

a = 666

while True:
    if len(l) == n:
        break
    else:
        digits = list()
        for i in str(a):
            digits.append(i)
        if digits.count("6") < 3:
            a += 1
            continue
        for k in range(len(digits)-2):
            if digits[k] == "6":
                if digits[k+1] == "6":
                    if digits[k+2] == "6":
                        l.append(a)
                        break
        a += 1

print(l[n-1])

#I know that this problem can be solved by just checking if 666 is in the string. However, I wanted to try some serious brute force to see how long it takes to run.