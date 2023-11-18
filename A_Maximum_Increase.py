n = int(input())
a = list(map(int, input().split()))

left = 0
right = 1
result = 1
while right < n:
    while right < n and a[right] > a[right-1]:
        right += 1
    result = max(result, right - left)
    left = right
    right += 1
print(result)
