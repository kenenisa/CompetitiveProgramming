t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(0)
        continue
    a.sort()
    mx = a[0]
    mi = a[0]
    valid = True
    for i in range(n):
        mx = max(mx,a[i])
        mi = min(mi,a[i])
        if valid and a[0] != a[i]:
            valid = False
    if valid:
        print(0)
        continue    
    median = a[n // 2]  
    operations = 0
    chosen_x = []
    
    while mx != mi:
        x = mx - mi
        maxx = -1
        minn = int(1e9)+1 
        for i in range(n):
            a[i] = (a[i] + x) // 2
            maxx = max(maxx,a[i])
            minn = min(minn,a[i])
        mx = maxx
        mi = minn
        operations += 1
        if operations <= n:
            chosen_x.append(x)
    print(operations)
    
    if operations <= n:
        print(*chosen_x)
