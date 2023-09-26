t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key=lambda x: [x % 2, x])
    print(*a)