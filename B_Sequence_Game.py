t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = [a[0]]

    for i in range(1,n):
        if a[i-1] > a[i]:
            result.append(1)
        result.append(a[i])


    print(len(result))
    print(*result)
