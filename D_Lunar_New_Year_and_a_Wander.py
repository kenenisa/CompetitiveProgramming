from heapq import *
from collections import defaultdict

n,m=list(map(int,input().split()))
df = defaultdict(list)
for _ in range(m):
    u,v=list(map(int,input().split()))
    df[u].append(v)
    df[v].append(u)
visited = set()
visited.add(1)
h=[1]
result = []
while h:
    u=heappop(h)
    result.append(u)
    for v in df[u]:
        if v not in visited:
            visited.add(v)
            heappush(h,v)
print(*result)