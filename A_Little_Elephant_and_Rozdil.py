n = int(input())
a = list(map(int,input().split()))

m = float('inf')
i = -1
c = 0

for j in range(n):
    if a[j] < m:
        m = a[j]
        i = j
        c = 1
    elif a[j] == m:
        c += 1
    
if c > 1:
    print("Still Rozdil")
else:
    print(i+1)