from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    elm = [0] * 1001

    for i in range(n):
        elm[a[i]] = max(elm[a[i]],i+1) 
    result = -1
    for i in range(1,1001):
        for j in range(i,1001):
            if gcd(i,j) == 1 and elm[i] > 0 and elm[j] > 0:
                result = max(result,elm[i]+elm[j])
    print(result)
