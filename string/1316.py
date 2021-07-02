"""
a = int(input())
z = 0

for i in range(a):
    b = input()
    c = list()
    for j in range(len(b)-1):
        if b[j] != b[j+1]:
            c.append(b[j])
    if b[len(b)-1] != b[len(b)-2]:
        c.append(b[len(b)-1])
    x = 0
    for k in range(len(c)):
        if c.count(c[k]) == 1:
            x += 1
    if x == len(c):
        z += 1

print(z)
"""
#I can't find the reason why this code is wrong. After speding few hours trying to figure out what mistake I've done, I decided to move on by solving this problem with another algorithm. I decided to compare the value of find/index for alphabets to solve this problem.

a = int(input())
b = a

for i in range(a):
    c = input()
    for k in range(len(c)-1):
        if c.find(c[k]) > c.find(c[k+1]):
            b -= 1
            break

print(b)