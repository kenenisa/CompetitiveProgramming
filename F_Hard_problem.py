n = int(input())
a = list(map(int,input().split()))
x = 0
for i in range(n):
    if i == 0:
        prev = input()
        y = a[i]
        continue
    cur = input()
    tx = ty = -1
    if cur >= prev:
        tx = x
    if cur >= prev[::-1]:
        if tx == -1: tx = y
        else: tx = min(tx, y)
    if cur[::-1] >= prev:
        ty = x+a[i]
    if cur[::-1] >= prev[::-1]:
        if ty == -1: ty = y+a[i]
        else:ty = min(ty, y+a[i])
    x = tx
    y = ty
    prev = cur
if x == y == -1:
    print(-1)
else:
    if x < y:
        print(x)
    else:
        print(y)
