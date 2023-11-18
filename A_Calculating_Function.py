from sys import stdin
input = stdin.readline
n = int(input())
if n & 1 == 1:
    print(-((n+1)//2))
else:
    print(n//2)
