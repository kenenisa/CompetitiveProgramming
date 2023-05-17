t = int(input())
result = 0
for _ in range(t):
    a = list(map(int,input().split()))
    e = [sum(a)]
    for i in range(len(a)):
        if a[i] == 1:
            e.append(i+1)
    print(*e)
