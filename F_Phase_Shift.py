def cycle(df1, df2, a, n):
    if a not in df1:
        return False
    if df1[a] in df2:
        return True
    n += 1
    df2[df1[a]] = 0
    return cycle(df1, df2, df1[a], n)
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    df = {}
    lookup = set()
    result = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ix = 0
    for i in s:
        ix = 0
        if i in df:
            result.append(df[i])
        elif len(alpha) == 1:
            result.append(alpha[0])
            df[i] = alpha[0]
            lookup.add(alpha[0])
            alpha.remove(alpha[0])
        elif i in lookup:
            for a in alpha:
                if not cycle(df, {i: 0}, a, 0):
                    result.append(a)
                    df[i] = a
                    lookup.add(a)
                    alpha.remove(a)
                    break
        else:
            for a in alpha:
                if a != i:
                    result.append(a)
                    df[i] = a
                    lookup.add(a)
                    alpha.remove(a)
                    break
    print("".join(result))