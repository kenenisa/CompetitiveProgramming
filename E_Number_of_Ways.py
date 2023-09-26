from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
s = sum(a)
def run():
    if s%3!=0: return 0
    c = 0
    p3=s//3
    result = 0
    rsum = 0
    for i in range(n-1):
        rsum += a[i]
        if rsum == p3*2:
            result += c
        if rsum == p3:
            c += 1
    return result
  
print(run())