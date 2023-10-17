def check(mid, n, x, y):
    return mid // x + mid // y >= n
n, x, y = map(int, input().split())
n-=1
if x > y:
    x, y = y, x
l = 0
r = n * x
while r - l > 1:
    mid = (l + r) // 2
    if check(mid, n, x, y):
        r = mid
    else:
        l = mid
print(r + min(x,y))
