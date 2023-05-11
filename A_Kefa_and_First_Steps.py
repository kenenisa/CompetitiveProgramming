def run():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        return 1
    left = 0
    result = 0
    for right in range(n):
        if a[right-1] > a[right]:
            left = right
        result = max(result,right - left + 1)
    return result
print(run())