def solve():
    n = int(input().strip())
    s = list(map(str, input().strip().split()))
    cnt = [[0] * 50 for _ in range(11)]
    ans = 0

    for x in s:
        a, b = [0] * 2
        for i in range(len(x)):
            if i & 1:
                b += int(x[i])
            else:
                a += int(x[i])
        ans += cnt[len(x)][a - b]
        cnt[len(x)][a - b] += 1

    print(ans)


solve()
