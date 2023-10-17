t = int(input())


def getWater(h, a):
    al = 0
    for el in a:
        if h > el:
            al += h - el
    return al


for _ in range(t):
    def run():
        n, x = list(map(int, input().split()))
        a = list(map(int, input().split()))
        if n == 1:
            return a[0] + x
        left = 1
        right = 1e18

        while left <= right:

            mid = (right + left) // 2
            water = getWater(mid, a)
            if water == x:
                return int(mid)
            elif water < x:
                left = mid+1
            else:
                right = mid-1
        wl = getWater(left, a)
        wr = getWater(right, a)
        waterLeft = abs(wl - x)
        waterRight = abs(wr - x)
        if wr <= x and waterRight < waterLeft:
            return int(right)
        return int(left) if wl <= x else int(right)
    print(run())
