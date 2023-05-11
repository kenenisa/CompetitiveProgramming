n,D=list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()


left = 0
right = n - 1
result = 0
while left <= right:
    high = a[right]
    while left <= right and high <= D:
        high +=  a[right]
        left += 1
    if high > D and left <= right:
        result += 1
    right -= 1
print(result)
