import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = 0
    mx = 0
    for i in range(n):
        if a[i] > mx:
            mx = a[i]
        if mx == i+1:
            result += 1
    print(result)


