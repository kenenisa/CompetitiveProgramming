from collections import deque

n,m=list(map(int,input().split()))


df = {}
q = deque()

df[n] = 0
q.append(n)
while q:
    num = q.popleft()
    if num - 1 not in df:
        df[num - 1] = df[num] + 1
        if num - 1 == m: break
        q.append(num - 1)   
    if num <= m * 2 and num * 2 not in df:
        df[num * 2] = df[num] + 1
        if num * 2 == m: break
        q.append(num * 2)

print(df[m])
