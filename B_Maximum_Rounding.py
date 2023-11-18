t = int(input())
for _ in range(t):
    s = list(map(int, list(input())))
    n = len(s)
    j = n-1
    start = n
    while j >= 0:
        if s[j] >= 5:
            start = j
            s[j] = 0
            if j-1 < 0:
                s =[1]+s
            else:
                s[j-1] += 1
        j-=1
    for i in range(start+1,len(s)):
        s[i] = 0
    print("".join(map(str, s)))
