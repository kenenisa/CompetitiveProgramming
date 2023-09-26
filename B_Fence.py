n, k = list(map(int, input().split()))
h = list(map(int, input().split()))


s = 0
for i in range(k):
    s += h[i]
mx = s
result = 0
for i in range(k, n):
    s -= h[i-k]
    s += h[i]
    if s <= mx:
        result = i-k+1
        mx = s
print(result+1)
