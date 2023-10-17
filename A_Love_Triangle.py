from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
df = defaultdict(int)
for i in range(n):
    df[i+1] = a[i]
for i in range(n):
    if df[df[df[i+1]]] == i+1:
        print("YES")
        exit(0)
print("NO")
