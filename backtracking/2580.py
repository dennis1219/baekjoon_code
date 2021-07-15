"""
import sys

for i in range(9):
    given = list(map(int, sys.stdin.readline().rstrip().split()))
    num = [1,2,3,4,5,6,7,8,9]
    removed = list(set(given))
    for k in range(9):
        num.remove(removed[k])
    if len(num) == 0:
        continue
    elif len(num) == 1:
        given.replace(0,num[0])
    else:
"""

#While solving this problem I realized the importance of coding efficiently. Need to study more before solving this problem.