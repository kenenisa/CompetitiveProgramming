from collections import defaultdict, deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [True] * n
    mx = -1e10
    for i in range(n):
        mx = max(mx, a[i] - b[i])
    result = []
    for i in range(n):
        if a[i]-b[i] == mx:
            result.append(i+1)
    print(len(result))
    print(*result)
