from collections import defaultdict
from heapq import *
n, m = list(map(int, input().split()))

df = defaultdict(list)
for _ in range(m):
    u, v, w = list(map(int, input().split()))
    df[u].append((v, w))
    df[v].append((u, w))

inf = int(1e6 + 1)
distance = [inf for _ in range(n+1)]
distance[1] = 0
h = [(0, 1)]
valid = False
while h:
    w, u = heappop(h)
    if u == n:
        valid = True
        break
    for v, x in df[u]:
        wi = w+x
        if wi < distance[v]:
            distance[v] = wi
            heappush(h, (wi, v))
if not valid:
    print(-1)
    exit()
result = []
visited = set()
def dfs(node):
    if node not in visited:
        result.append(node)
        min_node = None
        min_val = inf
        for v, _ in df[node]:
            if distance[v] < min_val:
                min_node = v
        visited.add(node)
        dfs(min_node)
dfs(n)
print(*result)
