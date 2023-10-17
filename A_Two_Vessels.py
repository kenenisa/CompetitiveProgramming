from math import ceil
t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    diff = abs(a-b)/2
    print(ceil(diff/c))
