t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    left = 0
    right = n - 1
    result = []
    while left < right:
        result.append(a[left])
        result.append(a[right])
        left += 1
        right -= 1
    if left == right:
        result.append(a[left])
    print(*result)