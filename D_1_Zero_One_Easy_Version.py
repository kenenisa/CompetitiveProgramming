t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split()))
    a = input()
    b = input()
    result = 0
    diff = 0
    pairCount = 0
    lastDiff = -1
    l2 = -1
    for i in range(n):
        if a[i] != b[i]:
            diff += 1
            if lastDiff == -1:
                lastDiff = i
            else:
                if lastDiff + 1 == i:
                    pairCount += 1
                    l2 = lastDiff
                    lastDiff = -1
                else:
                    lastDiff = i
    if diff % 2 == 1:
        print(-1)
        continue
    elif diff == 0:
        print(0)
        continue
    two = diff//2
    if diff == 2:
        if pairCount == 1:
            result = min(x, 2*y)
        else:
            result = min((lastDiff - l2) * x, y)
    else:
        result = two * y
    # loner = abs(two - pairCount)
    # result += (loner * y)
    # if x > y*2:
    #     result += (pairCount * (y*2))
    # else:
    #     result += (pairCount * x)
    print(result)
