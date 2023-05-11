t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = [a[0]]
    for i in range(1,n):
        if (result[-1] < 0 and a[i] < 0) or (result[-1] > 0 and a[i] > 0):
            result[-1] = max(result[-1],a[i])
        else:
            result.append(a[i])
    print(sum(result))