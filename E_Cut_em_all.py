from collections import defaultdict


def run():
    n = int(input())

    df = defaultdict(list)

    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        df[u].append(v)
        df[v].append(u)
    if n % 2 == 1:
        return -1
    size = [1] * (n+1)
    parent = [-1] * (n+1)
    parent[1] = 1
    stack = [1]
    while stack:
        u = stack[-1]
        valid = False
        for i in df[u]:
            if parent[i] == -1:
                parent[i] = u
                stack.append(i)
                valid = True
        if not valid:
            stack.pop()
            size[parent[u]] += size[u]
    ans = 0
    for i in range(2, n+1):
        if size[i] % 2 == 0:
            ans += 1
    return ans


print(run())
