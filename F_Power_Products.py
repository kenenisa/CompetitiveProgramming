from math import floor, ceil
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
result = 0


def is_perfect(num, power):
    candidate = num ** (1/power)
    lo_candidate = int(floor(candidate))
    hi_candidate = int(ceil(candidate))
    return num == lo_candidate**power or num == hi_candidate**power


for i in range(n):
    for j in range(i+1, n):
        mul = a[i] * a[j]
        if is_perfect(mul, k):
            result += 1
print(result)
