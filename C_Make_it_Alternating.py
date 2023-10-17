from math import factorial
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    one = list(filter(lambda x: x, s.split('0')))
    zero = list(filter(lambda x: x, s.split('1')))
    sub = one + zero
    k = len(sub)
    result = 1
    for i in range(k):
        result = result * len(sub[i])
    print(n-k, (result*factorial(n-k)) % 998244353)
