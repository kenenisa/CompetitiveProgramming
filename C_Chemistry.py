# r = ['YES',
# 'NO','YES','YES','YES','YES','NO','NO','YES','YES','YES','YES','NO','YES']
from collections import defaultdict,deque,Counter

t = int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    s = input()
    df = Counter(s)
    odds = 0
    for v in df.values():
        if v%2==1:
            odds+=1
    if odds > k+1:
        print("NO")
    else:
        print("YES")
    