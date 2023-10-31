from collections import *
t = int(input())
df = defaultdict(str)
originals = []
seen = set()
for _ in range(t):
    old,new = input().split()
    df[old] = new 
    if old not in seen:
        originals.append(old)
    seen.add(old)
    seen.add(new)
def dfs(node):
    if df[node] == "":
        return node
    return dfs(df[node])
print(len(originals))
for o in originals:
    print(o,dfs(o))
