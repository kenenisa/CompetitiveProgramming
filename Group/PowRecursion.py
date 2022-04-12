x = 2
n = -2

# b = 2
# n = 3
# o = n


def pow(b, e):
    if(e == 0):
        return 1
    if(e < 0):
        return pow(1/b,n*-1)
    print(e)
    half = pow(b, int(e/2))
    print(half)
    if(e % 2):
        return half * half * b
    return half * half



print(pow(x, n))
