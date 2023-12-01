t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 1
    m = a[-1]
    for i in range(n-2,-1,-1):
        if a[i] <= a[i+1]:
            m = min(m,a[i])
            count += 1
        else:
            break
    valid = True
    for i in range(n-count-1,-1,-1):
        if a[i] <= m:
            valid = False
    if not valid:
        print(-1)
    else:
        print(n-count)

    
