n,q=list(map(int,input().split()))
a = list(map(int,input().split()))

def incur(v, mask):
    return (v + mask) // mask * mask
for _ in range(q):
    k = int(input())
    b = a[:]
    result = 0
    for i in range(62, -1, -1):
        s = 0
        #reaa
        save = b[:]
        for j in range(n):
            if b[j] & 1 << i == 0:
                s -= b[j]
                b[j] = incur(b[j],(1 << i))
                s += b[j]
                if s > k:break
        if s > k:
            b = save[:]
        else:
            k -= s
            result += (1 << i)
            # result += s

    print(result)
