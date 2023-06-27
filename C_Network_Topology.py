from collections import defaultdict,deque
n,m=list(map(int,input().split()))
edges = [0]*n
df = defaultdict(list)
for i in range(m):
    u,v=list(map(int,input().split()))
    df[u].append(v)
    df[v].append(v)
    edges[u-1] += 1
    edges[v-1] += 1

one = edges.count(1)
two = edges.count(2)

visited = set()

q = deque([2])

# while q:
#     node  = q.popleft()
#     visited.add(node)
#     # edges[node-1] += 1
#     for v in df[node]:
#         if v not in visited:
#             q.append(v)
if one == 2 and two == n-2: print("bus topology")
elif one == 0 and two == n: print("ring topology")
elif one == n-1: print("star topology")
else: print("unknown topology")
