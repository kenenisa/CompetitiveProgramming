cases = input()
for line in range(int(cases)):
    s = input()
    n = len(s)
    m = 3
    if n < m: 
        print(0)
        continue
    pat = [0] * 256
    st = [0] * 256
    for i in range(0, m): pat[ord("123"[i])] += 1
    start = 0
    si = -1 
    ml = float('inf')
    c = 0 
    for j in range(0, n):
        st[ord(s[j])] += 1
        if (st[ord(s[j])] <= pat[ord(s[j])]):
            c += 1
        if c == m:
            while pat[ord(s[start])] == 0 or st[ord(s[start])] > pat[ord(s[start])]:
                if (st[ord(s[start])] > pat[ord(s[start])]):
                    st[ord(s[start])] -= 1
                start += 1
            lw = j - start + 1
            if ml > lw:
                ml = lw
                si = start
    if si == -1:
        print(0)
        continue
    print(len(s[si: si + ml]))