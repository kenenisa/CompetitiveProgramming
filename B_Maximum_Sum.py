t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort() #O(NlogN)
    s = 0
    for i in range(n-k):
        s += a[i]
    result = s
    for i in range(k):
        s -= a[i*2]
        s -= a[i*2+1]
        s += a[n-k+i]
        result = max(result, s)
    print(result)
