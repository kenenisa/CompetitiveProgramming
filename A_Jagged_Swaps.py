t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = min(a)
    if a[0] != m:
        print("NO")
    else:
        print("YES")