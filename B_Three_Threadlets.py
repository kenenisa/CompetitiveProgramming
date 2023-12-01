from math import ceil
t = int(input())
    
def check(a):
    a.sort()
    count = 0
    for i in range(1,3):
        if a[i] != a[i-1]:
            x = ceil(a[i]/a[i-1])
            count += x-1
            a[i] = a[i]//x
            if a[i] != a[i-1] or count > 3:
                return False
    return True
for _ in range(t):
    a = list(map(int,input().split()))
    if a[0] == a[1] == a[2] or check(a):
        print("YES")
    else:
        print("NO")