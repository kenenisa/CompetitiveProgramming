from collections import defaultdict,deque,Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    df = Counter(a)
    result = 0
    for k,v in df.items():
        if k > 2: 
            result += (v*(v-1))//2
    ot = df[1] + df[2]
    result += (ot*(ot-1))//2
    print(result)
