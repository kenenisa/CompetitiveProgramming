from collections import defaultdict
n,m=list(map(int,input().split()))
graph = defaultdict(list)
for _ in range(m):
    u,v=list(map(int,input().split()))
    graph[u].append(v)
