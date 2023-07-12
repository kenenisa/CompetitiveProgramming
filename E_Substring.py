from collections import *
def run():
    n,m=list(map(int,input().split()))
    s = input()
    df = defaultdict(list)
    edges = [0]*(n+1)
    for _ in range(m):
        u,v=list(map(int,input().split()))
        df[u].append(v)
        edges[v] += 1
    dp = [[0]*26 for _ in range(n+1)]
    q = deque()
    for i in range(1, n+1):
        if edges[i] == 0:
            q.append(i)
    visited = 0
    while q and visited < n:
        u = q.popleft()
        visited += 1
        pos = ord(s[u-1])-ord('a')
        dp[u][pos] += 1
        for v in df[u]:
            for j in range(26):
                dp[v][j] = max(dp[v][j], dp[u][j])
            edges[v] -= 1
            if edges[v] == 0:
                q.append(v)
    if visited != n:
        return "-1"
    return max([max(dp[i]) for i in range(1,n+1)])
print(run())