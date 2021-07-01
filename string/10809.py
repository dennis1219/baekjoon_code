import string

k = input()

for a in string.ascii_lowercase:
    print(k.find(a), end = " ")