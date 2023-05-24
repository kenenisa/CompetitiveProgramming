from collections import defaultdict
n,m=list(map(int,input().split()))
names = set()
df = defaultdict(int)
for _ in range(n):
    b = input()
    df[b] += 1
    names.add(b)
for _ in range(m):
    x,y = input().split()
    if x in names and y in names:
        if df[x] > df[y]:
            names.remove(x)
        else:
            names.remove(y)
print(len(names))
for a in sorted(list(names)):
    print(a)
