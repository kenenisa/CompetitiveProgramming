from collections import deque
s = input()
n = len(s)
d = deque()
for i in range(n-1,-1,-1):
    if s[i] == 'l':
        d.append(i+1)
    else:
        d.appendleft(i+1)
for i in d:
    print(i)


