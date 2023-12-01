from sys import stdin
input = stdin.readline
t = int(input())
def countBits(n):
    c = 0
    for i in range(32):
        if n & (1<<i):
            c +=1
    return c
for _ in range(t):
    n = int(input())
    print(pow(3,countBits(n)))

