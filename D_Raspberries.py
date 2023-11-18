def run():
    n,k=list(map(int,input().split()))
    a = list(map(int,input().split()))
    if k != 4:
        return min([(k - f%k)%k for f in a])
    count=0
    for i in a:
        if i%2==0:
            count+=1
        if count == 2:
            return 0
    return min(min([(k - f%k)%k for f in a]),2-count)
t = int(input())
for _ in range(t):
    print(run())
# 2
# 2
# 1
# 0
# 2
# 0
# 1
# 2
# 0
# 1
# 1
# 4
# 0
# 4
# 3
    
            