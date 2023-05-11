t = int(input())
def count_twos(n):
    if n % 2 == 1: return 0
    return 1 + count_twos(n//2)
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    aku = []
    for i in range(n):
        count += count_twos(a[i])
        aku.append(count_twos(i+1))
    if count >= n:
        print(0)
        continue
    if sum(aku) + count < n:
        print(-1)
        continue
    aku.sort(reverse=True)
    i = 0
    while count < n:
        count += aku[i]
        i += 1
    print(i)

    
