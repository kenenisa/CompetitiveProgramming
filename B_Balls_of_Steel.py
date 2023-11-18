t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    points = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        points.append((x, y))

    edges = [0]*(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                if abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) <= k:
                    edges[i] += 1
    valid = False
    for i in range(n):
        if edges[i] == n-1:
            valid = True
            break
    if valid:
        print(1)
    else:
        print(-1)
