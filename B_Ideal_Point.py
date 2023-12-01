t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    prefix = [0]*(52)
    for _ in range(n):
        l,r=list(map(int,input().split()))
        if l <= k <= r:
            prefix[l] += 1
            prefix[r+1] -= 1
    for i in range(1,51):
        prefix[i] += prefix[i-1]
    x = prefix[k]
    prefix[k] = 0
    y = max(prefix)
    if x > y:
        print("YES")
    else:
        print("NO")