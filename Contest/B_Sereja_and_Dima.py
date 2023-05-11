n = int(input())
a = list(map(int,input().split()))

s = True
sp = 0
dp = 0

left = 0
right = n-1

while left <= right:
    take = 0
    if a[left]>a[right]:
        take = a[left]
        left += 1
    else:
        take = a[right]
        right -= 1
    if s:
        sp += take
        s = False
    else:
        dp += take
        s = True
# if left == right:
#     s += a[left]
print(sp,dp)
