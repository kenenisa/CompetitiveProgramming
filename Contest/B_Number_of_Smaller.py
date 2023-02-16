n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = [0] * m
i = n 
for j in range(m-1,-1,-1):
    while i > 0 and a[i-1] >= b[j]:
        i -= 1
    result[j] = i
print(*result)

