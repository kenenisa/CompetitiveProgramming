n = int(input())
a = list(map(int,input().split()))
a.sort()
k = n//2
if n%2==0:
    small = a[:n//2]
    big = a[n//2:]
else:
    small = a[:(n//2)+1]
    big = a[(n//2)+1:]
result = []
for i in range(k):
    result.append(small.pop())
    result.append(big.pop())
result += small
valid = True
for j in range(1,n,2):
    if result[j] < result[j-1]:
        valid = False
        break
if valid:
    print(*result)
else:
    print("Impossible")