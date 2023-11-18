import sys
input = sys.stdin.readline

def run():
    x,y,k=list(map(int,input().split()))
    if x == y: return 0
    if x > y: return x
    if x+k >= y: return y
    s = x+k
    s += (y - (x+k))*2
    return s

t = int(input())
for _ in range(t):
    print(run())
