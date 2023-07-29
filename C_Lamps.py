from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    df = defaultdict(list)
    result = 0
    for _ in range(n):
        a,b=list(map(int,input().split()))
        df[a].append(b)
    
    for k in df.keys():
        df[k].sort(reverse=True)
        result += sum(df[k][:k])
    print(result)
