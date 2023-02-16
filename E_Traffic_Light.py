tests = int(input())
 
for _ in range(tests):
    n,l = input().split()
    n = int(n)
    lights = [i for i in input()]
    lights += lights
    seconds = 0
    p = 0
    targetFound = False
    s = 0
    while(p<n*2 and l != "g"):
        if lights[p] == l:
            targetFound = True
        if targetFound:
            if lights[p] == 'g':
                seconds = max(seconds,s)
                s = 0
                targetFound = False
            else:
                s += 1
        p += 1
    print(seconds)