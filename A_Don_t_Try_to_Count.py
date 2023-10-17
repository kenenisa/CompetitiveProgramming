def run():
    n, m = list(map(int, input().split()))
    x = input()
    s = input()
    if x == s: return 0
    k = 0
    while k < 6:
        if s in x:
            return k
        x += x
        k += 1
    return -1
t = int(input())
for _ in range(t):
    print(run())
