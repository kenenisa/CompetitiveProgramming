t = int(input())
for _ in range(t):
    dishes=list(map(int,input().split()))
    dishes.sort(reverse=True)
    pos = [
        [0],
        [1],
        [2],
        [0,1],
        [0,2],
        [1,2],
        [0,1,2],
    ]
    count = 0
    def r(cur):
        valid = True
        for p in cur:
            if dishes[p] <= 0:
                valid = False
                break
        if valid: 
            for p in cur:
                dishes[p] -= 1
            return True
        return False
        

    for p in pos:
        if r(p):
            count += 1
    print(count)
# 3 2 2

# 2 2 2
# 2 1 2
# 2 1 1
# 1 0 1
# 0 0 0