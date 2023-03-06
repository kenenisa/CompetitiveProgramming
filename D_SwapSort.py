n = int(input())
a = list(map(int,input().split()))

result = []
for i in range(n):
    m = i
    swap = False
    for j in range(i+1,n):
        if a[j] < a[m]:
            m = j
            swap = True
    if swap:
        result.append([i,m])
        a[i],a[m] = a[m],a[i]
print(len(result))
for i in range(len(result)):
    print(*result[i])