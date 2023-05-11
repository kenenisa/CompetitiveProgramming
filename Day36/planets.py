from collections import defaultdict
tests = int(input())
for _ in range(tests):
    n,c=list(map(int,input().split()))
    a = list(map(int,input().split()))
    df = defaultdict(int)
    for i in range(n):
        df[a[i]] += 1
    cost = 0
    for orbit,planets in df.items():
        if planets > c:
            cost += c
        else:
            cost += planets
    print(cost)

