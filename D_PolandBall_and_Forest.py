from collections import defaultdict
n = int(input())
p = list(map(int,input().split()))

df = defaultdict(list)

for i in range(n):
    df[i+1].append(p[i])
    df[p[i]].append(i+1)

color = 1
result = set()
visited = set()
def dfs(item,c):
    if item in visited: return 
    result.add(c)
    visited.add(item)
    for x in df[item]:
        dfs(x,c)

for i in range(1,n+1):
    dfs(i,i)
print(len(result))


