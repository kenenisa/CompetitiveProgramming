from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()
    df = defaultdict(int)
    for i in range(n):
        df[p1[i]] += 1
        df[p2[i]] += 1
        df[p3[i]] += 1
    result = [0,0,0]
    def score(sc):
        if sc == 1:
            return 3
        else:
            return 3 - sc
    for i in range(n):
        result[0] += score(df[p1[i]]) 
        result[1] += score(df[p2[i]]) 
        result[2] += score(df[p3[i]]) 
    print(*result)

        
