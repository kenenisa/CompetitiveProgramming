n = int(input())
def run():
    if n == 1:
        return 0
    events = []
    for _ in range(n):
        events.append(list(map(int,input().split())))
    
    def srt(key):
        return key[0]
    events.sort(key=srt)
    mry = events[0]
    count = 0
    for i in range(1,n):
        if mry[0] < events[i][0] and events[i][1] < mry[1]:
            count += 1
        else:
            mry = events[i]
    return count
print(run())
