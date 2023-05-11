from functools import cache
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    prefix = [0]
    for aa in a:
        prefix.append(aa + prefix[-1])
    mi = float('inf')
    @cache
    def recur(start,end):
        global mi
        if start >= n:
            return
        end = min(end,n)
        mi = min(mi,prefix[end] - prefix[start])
        recur(end,end+18)
        recur(end,end+12)
    recur(0,18)
    recur(0,12)
    print(mi)
