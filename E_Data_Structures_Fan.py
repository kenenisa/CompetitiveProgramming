import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    q = int(input())
    prefix = [0] * (n+1)
    one = 0
    zero = 0
    typeOne = 0
    for i in range(n):
        prefix[i+1] = prefix[i] ^ a[i]
        if s[i] == '0':
            zero = zero ^ a[i]
        else:
            one = one ^ a[i]
    result = []
    for _ in range(q):
        p = list(map(int,input().split()))
        if p[0] == 1:
            _,l,r = p
            rng = prefix[l-1] ^ prefix[r] 
            typeOne = typeOne ^ rng
        else:
            _,g = p
            typeTwo = typeOne ^ zero
            if g == 1:
                typeTwo = typeOne ^ one
            result.append(typeTwo)
    print(*result)
                
