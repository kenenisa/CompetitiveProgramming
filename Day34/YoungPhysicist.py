test = int(input())
xd = []
yd = []
zd = []
for _ in range(test):
    x,y,z = list(map(int,input().split()))
    xd.append(x)
    yd.append(y)
    zd.append(z)

print("YES" if sum(xd) == 0 and sum(yd) == 0 and sum(zd) == 0 else "NO")
