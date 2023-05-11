t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    pos = [0] * 31
    a = list(map(int,input().split()))
    for i in range(n):
        for j in range(30,-1,-1):
            if a[i] & (1<<j):
                pos[j] += 1
    result = 0
    for j in range(30,-1,-1):
        amount = n - pos[j]
        if amount <= k:
            k -= amount
            result += (1<<j)
    print(result)
    