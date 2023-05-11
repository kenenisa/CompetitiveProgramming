n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()
b.sort()
i = 0
j = 0
result = 0
while i < n  and j < m:
    if abs(a[i] - b[j]) <= 1:
        result += 1
        i += 1
        j += 1
    else:
        if a[i] - b[j] < 0:
            i+=1
        else:
            j+=1
print(result)