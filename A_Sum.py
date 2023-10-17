t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    a.sort()
    print("YES" if a[0] + a[1] == a[2] else "NO")