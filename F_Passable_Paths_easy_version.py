from collections import deque

n = int(input())
g = [[] for i in range (n)]
for _ in range (n-1):
    u,v = [int(i)-1 for i in input().split()]
    g[u].append(v)
    g[v].append(u)
q = int(input())
for _ in range (q):
    k = int(input())
    a = [int(i)-1 for i in input().split()]
    sa = set(a)
    q = deque([a[0]])
    vis = [0]*n
    vis[a[0]]=1
    leaf = a[0]
    while(q):
        cur = q.popleft()
        if cur in sa:
            leaf = cur
        for i in g[cur]:
            if vis[i]==0:
                vis[i]=1
                q.append(i)
    
    q = deque([leaf])
    vis = [0]*n
    vis[leaf]=1
    parent = [-1]*n
    leaf1 = leaf
    while(q):
        cur = q.popleft()
        if cur in sa:
            leaf1 = cur
        for i in g[cur]:
            if vis[i]==0:
                vis[i]=1
                q.append(i)
                parent[i] = cur
    
    path = []
    cur = leaf1
    while(cur != -1):
        if cur in sa:
            path.append(cur)
        cur = parent[cur]
    if len(path)==len(a):
        print("YES")
    else:
        print("NO")