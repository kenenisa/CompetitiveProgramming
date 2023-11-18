from collections import defaultdict,deque

n = int(input())
s = input()
q = deque()
f = n%2==1
for i in range(n):
    if f:
        q.append(s[i])
    else:
        q.appendleft(s[i])
    f = not f
print("".join(q))