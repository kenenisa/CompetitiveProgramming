import sys
from collections import defaultdict
sys.setrecursionlimit(2 * (10 ** 5))
n, m = map(int, input().split())
cats = list(map(int, input().split()))
tree = [[] for _ in range(n)]
tree = defaultdict(list)

for i in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def recur(node, path, parent):
    catsCount = 0
    if cats[node-1] == 1:
        catsCount = path + cats[node-1]
    if catsCount > m:
        return 0
    valid = 0
    leaf = True
    for i in tree[node]:
        if i == parent:
            continue
        leaf = False
        valid += recur(i, catsCount, node)
    if leaf:
        return 1
    return valid

print(recur(1, 0, -1))