from collections import defaultdict,deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n < 4:
        print(-1)
        continue
    b = [1] * n
    df = defaultdict(list)
    repeated = defaultdict(bool)
    for i in range(n):
        if a[i] in df:
            repeated[a[i]] = True
        df[a[i]].append(i)
    r = list(repeated.keys())
    if len(df.keys()) == 1 or len(r) < 2:
        print(-1)
        continue
    first = r[0]
    second = r[1:]
    for i in df[first][1:]:
        b[i] = 2

    for s in second:
        for i in df[s][1:]:
            b[i] = 3
    
    print(*b)
    
    