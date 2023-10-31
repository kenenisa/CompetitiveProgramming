from math import ceil
def run():
    a, b, c = list(map(int, input().split()))
    return ceil(abs(a-b)/2/c)
t = int(input())
for _ in range(t):
    print(run())
