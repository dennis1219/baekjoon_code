import sys

n = int(sys.stdin.readline())
l = list()
for i in range(n):
    word = sys.stdin.readline().rstrip()
    l.append((word,len(word)))

words = list(set(l))

words.sort(key = lambda x : (x[1],x[0]))

for k in range(len(words)):
    print(words[k][0])