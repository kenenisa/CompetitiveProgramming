t = int(input())
for _ in range(t):
    n = int(input())
    s = set()
    sets = []
    for _ in range(n):
        a = list(map(int,input().split()))
        k = a[0]
        sets.append(set(a[1:]))
        for i in range(1,k+1):
            s.add(a[i])
    result = 0
    for i in list(s):
        m = set()
        for se in sets:
            if i not in se:
                m = m.union(se)
        result = max(result,len(m))
    print(result)

    