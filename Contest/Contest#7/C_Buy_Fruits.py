from collections import defaultdict
n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
df = defaultdict(int)
for _ in range(m):
    df[input()] +=1
fruits = sorted(list(df.items()),key=lambda x: x[1],reverse=True)
mi = 0
mx = 0
for i in range(len(fruits)):
    mi += a[i] * fruits[i][1]
    mx += a[(i+1) * -1] * fruits[i][1]


print(mi,mx)
