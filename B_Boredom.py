from collections import defaultdict,deque

n = int(input())
a = list(map(int,input().split()))
df = defaultdict(int)

for i in a:
    df[i] += i

cur = 0
prev = 0
for i in range(int(1e5 + 1)):
    temp = cur
    cur = max(cur,prev+df[i])
    prev = temp
print(cur)
2
2
1
0
1
0
1
1
1
1
1
4
0
4
3