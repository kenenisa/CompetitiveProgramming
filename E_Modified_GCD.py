from math import gcd, ceil, sqrt
a, b = list(map(int, input().split()))
common = gcd(a, b)
divisors = []
for i in range(1, ceil(sqrt(common))+1):
    if common % i == 0:
        divisors.append(i)
        divisors.append(common//i)
# print(divisors)
n = int(input())
for _ in range(n):
    low, high = list(map(int, input().split()))
    valid = False
    result = []
    for d in divisors:
        if low <= d <= high:
            result.append(d)
    if not result:
        print(-1)
    else:
        result.sort()
        print(result[-1])
