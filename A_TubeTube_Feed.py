q = int(input())
for _ in range(q):
    n,t=list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    result = -1
    most = 0
    for i in range(n):
        if a[i] <= t:
            if b[i] > most:
                result = i + 1
                most = b[i]
        t -= 1
    print(result)
    