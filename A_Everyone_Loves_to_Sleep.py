t = int(input())
for _ in range(t):
    n,H,M=list(map(int,input().split()))
    slept = (H*60)+M
    alarms = []
    valid = False
    for _ in range(n):
        h,m=list(map(int,input().split()))
        alarm = (h*60)+m
        alarms.append(alarm)
        if alarm == slept:
            valid = True
    if valid:
        print(0,0)
        continue
    alarms.sort()
    alarms.append(alarms[0] + (24*60))
    i = 0
    while alarms[i] < slept:
        i+=1
    diff = alarms[i] - slept
    print(diff//60,diff%60) 
