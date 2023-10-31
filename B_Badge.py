n = int(input())
p = list(map(int,input().split()))

def dfs(node,visited):
    if node in visited:
        return node
    visited.add(node)
    return dfs(p[node-1],visited)
result = []

for i in range(1,n+1):
    result.append(dfs(i,set()))
print(*result)