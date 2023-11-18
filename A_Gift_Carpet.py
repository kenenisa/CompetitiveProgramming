t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    carpet = []
    for _ in range(n):
        carpet.append(input())
    find = ['a','k','i','v']
    for j in range(m):
        if not find: break
        for i in range(n):
            if carpet[i][j] == find[-1]:
                find.pop()
                break
    print("YES" if not find else "NO")