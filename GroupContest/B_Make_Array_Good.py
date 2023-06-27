p = int(input())

for _ in range(p):
    n = int(input())
    a = list(map(int, input().split()))

    b = [[a[i], i+1] for i in range(n)]
    b.sort(key=lambda x:x[0])
    op = []
    for i in range(1, n):
        if not b[i][0] % b[i-1][0]:
            continue
        v = b[i-1][0] - (b[i][0] % b[i-1][0])
        b[i][0] += v
        op.append([b[i][1], v])
        
    print(len(op))
    for i in op:
        print(*i)