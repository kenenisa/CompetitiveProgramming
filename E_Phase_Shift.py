def cycle(df1, df2, a, n):
    if n > 26:
        return False
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
            ix = 0
            while cycle(df, {i: 0}, alpha[ix], 0):
                ix += 1
            result.append(alpha[ix])
            df[i] = alpha[ix]
            lookup.add(alpha[ix])
            alpha.remove(alpha[ix])
        else:
            ix = 0
            while alpha[ix] == i:
                ix += 1
            result.append(alpha[ix])
            df[i] = alpha[ix]
            lookup.add(alpha[ix])
            alpha.remove(alpha[ix])
    print("".join(result))
