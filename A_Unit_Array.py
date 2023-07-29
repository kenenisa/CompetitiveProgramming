t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    neg = a.count(-1)
    pos = n - neg
    result = 0
    while ((neg * -1) + pos) < 0:
        neg -= 1
        pos += 1
        result += 1
    p = 1
    if neg % 2 == 1:
        result += 1
    print(result)