t = int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    a = list(map(int,input().split()))
    prefix = [0]
    for aa in a:
        prefix.append(prefix[-1] + aa)
    total = sum(a)
    for _ in range(m):
        l,r,k=list(map(int,input().split()))
        amount = (r - l + 1) * k
        g = (total - (prefix[r] - prefix[l-1])) + amount
        if g % 2:
            print("YES")
        else: 
            print("NO")