n = int(input())
a = list(map(int,input().split()))
odd = False
even = False
i = 0
while (not odd or not even) and i < n:
    if a[i]%2 == 0:
        even = True
    else:
        odd = True
    i+=1
if even and odd:
    a.sort()
print(*a)