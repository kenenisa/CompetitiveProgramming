import math
t = int(input())
for _ in range(t):
    n, P, l, t = list(map(int, input().split()))
    weeks = (n - n % 7) // 7 + 1
    if n%7 == 0:
        weeks -= 1
    left = 1 
    right = weeks
    result = weeks
    while (left <= right):
        mid = (left + right) // 2
        if (P <= (mid + 1) // 2 * l + t * mid):
            result = mid
            right = mid-1
        else:
            left = mid+1
    #check if result works
    w = (result + 1) // 2
    find = (w * l) + (t * result)
    P = P - find
    mid = w
    if P > 0:
        mid += (P // l)
        mid += (P % l != 0)
    print(n-mid)