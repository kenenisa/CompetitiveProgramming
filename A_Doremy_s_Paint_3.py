from collections import defaultdict

def run():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        return "Yes"
    df = defaultdict(int)
    for i in a:
        df[i] += 1
    keys = list(df.keys())
    if len(keys) > 2:
        return "No"
    elif len(keys) == 1:
        return "Yes"
    a = df[keys[0]]
    b = df[keys[1]]
    if n%2==0:
        return "Yes" if a==b else "No"
    return "Yes" if abs(a-b)==1 else "No"
t = int(input())
for _ in range(t):
    print(run())
    

        
        
    
