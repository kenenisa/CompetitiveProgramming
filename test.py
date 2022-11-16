tests = int(input())
def validStone(r1,r2,d):
    return d <= r1 - r2 or d == r1 + r2
def sortDistance(val):
    return val[0]
for _ in range(tests):
    r1,r2 = list(map(int,input().split()))
    stones = []
    n = int(input())
    for i in range(n):
        x,y = list(map(int,input().split()))
        d = math.sqrt(2 * (x + y))
        if validStone(r1,r2,d):
            stones.append([d,'red'])
    m = int(input())
    for i in range(m):
        z,w = list(map(int,input().split()))
        d = math.sqrt(2 * (z + w))
        if validStone(r1,r2,d):
            stones.append([d,'yellow'])
    stones.sort(key=sortDistance)
    
    print('Case #' + str(_) +': ' + str(result))