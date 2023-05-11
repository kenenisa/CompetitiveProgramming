t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    result = 0
    for i in range(n):
        if a[i] != b[i]:
            result += 1
    print(result//2)


