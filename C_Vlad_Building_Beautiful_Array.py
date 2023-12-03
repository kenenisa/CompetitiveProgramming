t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    firstIsEven = a[0]&1==0
    valid = True
    if firstIsEven:
        for i in a:
            if i&1:
                valid = False
                break
    print("YES" if valid else "NO")
