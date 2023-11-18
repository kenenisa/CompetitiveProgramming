from collections import defaultdict, deque
from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ss = sum(a)
    if ss < s:
        print(-1)
        continue
    if ss == s:
        print(0)
        continue
    window = 0
    j = 0
    result = 0
    for i in range(n):
        window += a[i]
        while window > s:
            window -= a[j]
            j += 1
        if window == s:
            result = max(result,i-j+1)
    print(n-result)
            
        
