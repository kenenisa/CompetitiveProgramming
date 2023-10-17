from math import gcd, sqrt, ceil
n = int(input())

result = []
for i in range(1,ceil(sqrt(n))+1):
    # print(i)
    if n % i == 0 and gcd(n//i, i) == 1:
        # print(i,n//i)
        result.append([i, n//i])
result.sort(key=lambda x: max(x))
print(*result[0])
