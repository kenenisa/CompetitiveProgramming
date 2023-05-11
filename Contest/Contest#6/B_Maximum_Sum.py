n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
s = 0
for aa in a:
    if aa < 0 and m > 0:
        s += (aa * -1)
    else:
        break
    m -= 1
print(s)