from collections import defaultdict
from heapq import *
n, m = list(map(int, input().split()))

df = defaultdict(list)
for _ in range(m):
    u, v, w = list(map(int, input().split()))
    df[u].append((v, w))
    df[v].append((u, w))

inf = float('inf')
distance = [(inf,None) for _ in range(n+1)]
distance[1] = (0,None)
h = [(0, 1)]
valid = False
while h:
    w, u = heappop(h)
    if u == n:
        valid = True
        break
    for v, x in df[u]:
        wi = w+x
        if wi < distance[v][0]:
            distance[v] = (wi,u)
            heappush(h, (wi, v))
if not valid:
    print(-1)
    exit()
result = []
i = n
while i:
    result.append(i)
    i = distance[i][1]
result.reverse()
print(*result)
