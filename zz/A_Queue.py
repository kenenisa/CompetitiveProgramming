n = int(input())
a = list(map(int,input().split()))
a.sort()
s = 0
result = 0
for i in range(n):
    if s <= a[i]:
        result += 1
        s += a[i]
print(result)