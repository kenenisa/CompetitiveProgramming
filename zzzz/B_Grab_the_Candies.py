t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    m = 0
    for aa in a:
        if aa % 2 == 0:
            m += aa
    
    if m > (s - m):
        print("YES")
    else:
        print("NO")