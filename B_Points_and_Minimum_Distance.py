import sys
input = sys.stdin.readline


def run():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    points = []
    x = a[n:]
    y = a[:n]
    s = 0
    for i in range(n):
        points.append((x[i],y[i]))
    for i in range(len(points)-1):
        one = points[i]
        two = points[i+1]
        s += abs(one[0] - two[0]) + abs(one[1] - two[1])
    print(s)
    for i,j in points:
        print(i,j)

t = int(input())
for _ in range(t):
    run()
