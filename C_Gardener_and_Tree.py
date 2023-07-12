from collections import *
t = int(input())
for _ in range(t):
    input()
    n,k=list(map(int,input().split()))
    df = defaultdict(list) 
    edges = [0]*(n+1)
    depth = [float('inf')]*(n+1)
    for _ in range(n-1):
        u,v=list(map(int,input().split()))
        u-=1
        v-=1
        edges[u] += 1           
        edges[v] += 1
        df[u].append(v)
        df[v].append(u)
    q = deque()
    for i in range(n):
        if edges[i] < 2:
            q.append(i)
            depth[i] = 0
    while q:
        u = q.popleft()
        for v in df[u]:
            edges[v] -= 1
            if edges[v] == 1:
                depth[v] = depth[u] + 1
                q.append(v)
    result = 0
    for i in range(n):
        if depth[i] >= k:
            result += 1
    print(result)