
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = 0
    for i in range(n):
        result |= a[i]

    print(result)
