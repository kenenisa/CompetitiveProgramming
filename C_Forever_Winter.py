from collections import Counter

t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    edges = [0] * n
    for _ in range(m):
        u,v=list(map(int,input().split()))
        edges[u-1] += 1
        edges[v-1] += 1
    c = Counter(edges)
    x = min(c,key=c.get)
    c[1] = 0
    y = max(c,key=c.get)
    print(x,y-1)