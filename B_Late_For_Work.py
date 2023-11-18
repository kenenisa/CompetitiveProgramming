
t = int(input())
for _ in range(t):
    n, l = input().split()
    n = int(n)
    lights = input()
    lights += lights
    seconds = 0
    p = 0
    found = False
    s = 0
    while (p < n*2 and l != "g"):
        if lights[p] == l:
            found = True
        if found:
            if lights[p] == 'g':
                seconds = max(seconds, s)
                s = 0
                found = False
            else:
                s += 1
        p += 1
    print(seconds)
