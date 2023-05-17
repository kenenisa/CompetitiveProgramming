t = int(input())
result = 0
for _ in range(t):
    a = list(map(int,input().split()))
    e = [0] * t
    for i in range(1,len(a)):
        e[a[i]-1] = 1
    print(*e)