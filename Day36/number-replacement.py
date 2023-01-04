tests = int(input())
for _ in range(tests):
    n = int(input())
    a = list(map(int,input().split()))
    s = [i for i in input()]
    valid = True
    df = {}
    for i in range(n):
        found = df.get(a[i])
        if found and found != s[i]:
            valid = False
            break
        df[a[i]] = s[i]
    print("YES" if valid else "NO")