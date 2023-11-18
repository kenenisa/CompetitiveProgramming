t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    # if n == 1: 
    #     print(a[0])
    #     continue
    result = float('-inf')
    par = -1
    s = 0
    for i in range(0,n):
        if a[i]%2==par:
            s = a[i]
        else:
            s = max(a[i],s+a[i])
        result = max(result,s)
        par = a[i]%2
    print(result)


