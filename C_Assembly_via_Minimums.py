t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    result = [int(-1e9)]*n
    inx = []
    k = 0
    for i in range(n):
        for j in range(i+1,n):
            result[i] = max(result[i],b[k])
            result[j] = max(result[j],b[k])
            k += 1
    print(*result)