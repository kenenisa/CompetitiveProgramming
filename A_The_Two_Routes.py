import sys
from collections import defaultdict, deque
input = sys.stdin.readline
df = defaultdict(set)
n, m = list(map(int, input().split()))

for _ in range(m):
    u, v = list(map(int, input().split()))
    df[u].add(v)
    df[v].add(u)

universal = set(range(1, n+1))
# 1 bus
# 0 train
q = deque([(1, 0, 0), (1, 1, 0)])
vehicles = [float('inf'), float('inf')]
busVisited = set([1])
trainVisited = set([1])

while q:
    u, vehicle, distance = q.popleft()
    if u == n:
        vehicles[vehicle] = min(vehicles[vehicle],distance)
        continue
    if vehicle == 0:
        for v in df[u]:
            if v not in trainVisited:
                q.append((v, vehicle, distance+1))
                trainVisited.add(v)
    else:
        for v in universal.difference(df[u]):
            if v not in busVisited:
                q.append((v, vehicle, distance+1))
                busVisited.add(v)
if float('inf') in vehicles:
    print(-1)
else:
    print(max(vehicles))
