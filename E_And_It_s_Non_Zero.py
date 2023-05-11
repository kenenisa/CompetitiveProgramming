pre = [[0]*20] * ((2 * (10 ** 5) + 1))
for i in range(1,2 * (10 ** 5) + 1):
    pre[i] = pre[i-1][::]
    for j in range(19,-1,-1):
        if i & (1<<j):
            pre[i][j] += 1 

t = int(input())
for _ in range(t):
    l,r=list(map(int,input().split()))
    m = 0
    for j in range(19,-1,-1):
        m = max(m,pre[r][j]-pre[l-1][j])
    n = r - l + 1
    print(n - m)