"""
import sys

n = int(sys.stdin.readline())

#좌표 x 다르고 y 다르고 대각X/전체 경우를 해서 n으로 나누기 ㄱㄱ

sol = set()
l = list()

for x in range(n):
    for y in range(n):
        l.append((x+1,y+1))
       
tempsol = set()

def queen(p,q):
    tempsol.add((p,q))
    for a in range(n):
        for b in range(n):
            templ = l
            if p == a+1:
                repx = templ.replace(templ[a:a+7], (0,0))
            if q == b+1:
                repy = templ.replace(templ[b+1::n], (0.0))
            if p == a+1 and q == b+1:
                repxy = templ.replace()
# 리스트에서 퀸 좌표 다 지우고 고르기 ㄱ
"""
#Ughhh.. I've been going the hard way..
"""
answer=[0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596]
print(answer[int(input())])
"""
#Just kidding lol...

import sys


n = int(sys.stdin.readline())
x = [0] * n
result = 0

def queen(t):
    for i in range(t):
        if x[t] == x[i] or abs(x[t] - x[i]) == abs(t - i):
            return False
    return True

def dfs(z):
    global result

    if z == n:
        result += 1
    else:
        for i in range(n):
            x[z] = i
            if queen(z):
                dfs(z+1)


dfs(0)

print(result)

#Used depth-first search algorithm... Simplest way to solve this problem.