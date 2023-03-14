n,k=list(map(int,input().split()))
a = list(map(int,input().split()))
seg = []

lastDiff = -1
for i in range(n-1):
    diff = abs(a[i] - a[i+1])
    if lastDiff > -1:
        if lastDiff + diff <= k:
            seg[-1][1] = i+2
            lastDiff += diff
            continue
    if diff <= k:
        seg.append([i+1,i+2])
        lastDiff = diff
mx = 0
for sg in seg:
    mx = max(mx,(sg[1] - sg[0])+1)
if len(seg) > 0:
    print(mx,len(seg))
else:
    print(1,n)
    for i in range(n):
        print(i+1,i+1)
for sg in seg:
    print(*sg)

