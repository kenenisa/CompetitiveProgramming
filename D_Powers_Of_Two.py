n,k=list(map(int,input().split()))

def run(n,k):
    if bin(n).count("1") > k:
        return "NO"
    bits = [1]*k
    n -= sum(bits)
    for i in range(k):
        while bits[i] <= n:
            # print(n,bits,i)
            n-=bits[i]
            bits[i] *= 2
    if n == 0:
        print("YES")
        return " ".join(map(str,bits))
    else:
        return "NO"


print(run(n,k))