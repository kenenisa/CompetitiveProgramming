t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    parity = [0,0]
    for i in a:
        parity[i%2] += 1
    print("YES" if parity[1]%2==0 else "NO")