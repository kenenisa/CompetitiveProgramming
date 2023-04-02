import sys
sys.setrecursionlimit(2 * (10 ** 5))
n, m = map(int, input().split())
cats = list(map(int, input().split()))
tree = [[] for _ in range(n)]



for i in range(n - 1):
    x, y = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)

def recur(node, path, parent):
    catsCount = 0
    if cats[node] == 0:
        catsCount = 0
    else:
        catsCount = path + cats[node]
    if catsCount > m:
        return 0
    leaf = True
    valid = 0
    for j in tree[node]:
        if j == parent:
            continue
        leaf = False
        valid += recur(j, catsCount, node)
    if leaf:
        return 1
    return valid

print(recur(0, 0, -1))