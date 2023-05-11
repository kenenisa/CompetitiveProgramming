n = int(input())
seg = []
flt = []
for i in range(n):
    l,r = list(map(int,input().split()))
    seg.append([l,r])
    flt.append(l)
    flt.append(r)
    
def srt(key):
    return key[0]
mi = min(flt)
mx = max(flt)
def runn(mi,mx,seg,n):
    for j in range(n):
        if seg[j][0] == mi and seg[j][1] == mx:
            return j + 1
    return -1
print(runn(mi,mx,seg,n))